import pandas as pd
import numpy as np
from operator import add

class Macro:

    def __init__(self, name, value=None):
        self.name = name
        self.value = float(value)

    def __str__(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def update_value(self, factor):
        self.value = self.value * factor
        return self

class Ingredient:

    def __init__(self, name, unit, quantity, macro_list):
        self.name = name
        self.unit = unit
        self.quantity = int(quantity)
        self.macro_list = macro_list

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_unit(self):
        return self.unit

    def get_quantity(self):
        return self.quantity

    def get_macros(self):
        return self.macro_list

    def change_quantity(self, quantity):
        factor = quantity/self.quantity
        self.quantity = quantity
        # Update macros
        self.macro_list = [m.update_value(factor) for m in self.macro_list]


class Meal:

    def __init__(self, name, ingredient_list=None, is_keto=False, exclude=None):
        self.name = name
        self.is_keto = is_keto
        self.ingredient_db = self.get_db()
        if exclude is not None:
            ingredient_list = self.exclude_ingredients(exclude, ingredient_list)
            self.ingredient_list = [self.get_ingredient(x) for x in ingredient_list]
        else:
            self.ingredient_list = [self.get_ingredient(x) for x in ingredient_list]

    def __str__(self):
        return self.name

    def copy(self):
        return self

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)

    def add_ingredient_raw(self, ingredient, quantity):
        self.ingredient_list.append(self.get_ingredient((ingredient, quantity)))

    def get_db(self):
        if self.is_keto:
            nutrition_csv = pd.read_csv('keto-micros.csv', header=None, sep='\t')
            ingredient_db = []
            N, D = nutrition_csv.shape
            for idx in range(1, N):
                name = nutrition_csv[0][idx]
                unit = nutrition_csv[1][idx]
                quantity = nutrition_csv[2][idx]
                kcal = Macro('kcal', nutrition_csv[3][idx])
                protein = Macro('protein', nutrition_csv[4][idx])
                carbs = Macro('carbs', nutrition_csv[5][idx])
                fat =  Macro('fat', nutrition_csv[6][idx])
                net_carbs = Macro('net_carbs', float(nutrition_csv[5][idx]) - float(nutrition_csv[7][idx]))
                macro_list = [kcal, protein, carbs, fat, net_carbs]
                ingredient = Ingredient(name, unit, quantity, macro_list)
                ingredient_db.append(ingredient)
        else:
            nutrition_csv = pd.read_csv('nutrition.csv', header=None, sep='\t')
            ingredient_db = []
            N, D = nutrition_csv.shape
            for idx in range(N):
                name = nutrition_csv[0][idx]
                unit = nutrition_csv[1][idx]
                quantity = nutrition_csv[2][idx]
                kcal = Macro('kcal', nutrition_csv[3][idx])
                protein = Macro('protein', nutrition_csv[4][idx])
                carbs = Macro('carbs', nutrition_csv[5][idx])
                fat =  Macro('fat', nutrition_csv[6][idx])
                macro_list = [kcal, protein, carbs, fat]
                ingredient = Ingredient(name, unit, quantity, macro_list)
                ingredient_db.append(ingredient)

        return ingredient_db

    def get_ingredient(self, ingredient_tuple):
        for ii in self.ingredient_db:
            if ii.get_name() == ingredient_tuple[0]:
                ingredient = ii
                ingredient.change_quantity(ingredient_tuple[1])
                return ingredient

        print('Ingredient {} not in db'.format(ingredient_tuple[0]))
        return None

    def get_ingredient_list(self):
        return self.ingredient_list

    def get_nutrition(self):
        if self.is_keto:
            nutrition = np.zeros(5)
        else:
            nutrition = np.zeros(4)
        for ingredient in self.ingredient_list:
            macro_list = ingredient.get_macros()
            macro_values = [macro.get_value() for macro in macro_list]
            nutrition += np.array(macro_values)
        return nutrition

    def get_micros(self):
        micros_csv = pd.read_csv('keto-micros.csv', header=None, sep='\t')
        sodium = 0
        potassium = 0
        magnesium = 0
        omega3 = 0
        for ingredient in self.ingredient_list:
            factor = ingredient.get_quantity() / float(micros_csv[micros_csv.iloc[:, 0] == ingredient.get_name()].iloc[:,2].values[0])
            sodium += float(micros_csv[micros_csv.iloc[:, 0] == ingredient.get_name()].iloc[:,8].values[0])*factor
            potassium += float(micros_csv[micros_csv.iloc[:, 0] == ingredient.get_name()].iloc[:,9].values[0])*factor
            magnesium += float(micros_csv[micros_csv.iloc[:, 0] == ingredient.get_name()].iloc[:,10].values[0])*factor
            omega3 += float(micros_csv[micros_csv.iloc[:, 0] == ingredient.get_name()].iloc[:,11].values[0])*factor
        return [sodium, potassium, magnesium, omega3]


    def remove_ingredient(self, ingredient):
        self.ingredient_list = [x for x in self.ingredient_list if x.get_name() != ingredient]

    def exclude_ingredients(self, exclude_list, ingredient_list):
        for ingr in exclude_list:
            if isinstance(ingr, str):
                ingredient_list = [x for x in ingredient_list if x[0] != ingr]
            else:
                ingredient_list = [(x[0], x[1]-ingr[1]) if x[0] == ingr[0] else x for x in ingredient_list]
        return ingredient_list

    def get_high_macros(self):
        kcals = []
        proteins = []
        carbs = []
        net_carbs = []
        fats = []
        ingredients = self.get_ingredient_list()
        for ingredient in ingredients:
            macro_list = ingredient.get_macros()
            macro_values = [macro.get_value() for macro in macro_list]
            kcals.append(macro_values[0])
            proteins.append(macro_values[1])
            carbs.append(macro_values[2])
            fats.append(macro_values[3])
            if self.is_keto:
                net_carbs.append(macro_values[4])

class Day:

    def __init__(self, name, meal_list=None, is_keto=False, show_price=False, show_micros=False):
        self.name = name
        self.meal_list = meal_list
        self.is_keto = is_keto or meal_list[0].is_keto
        self.show_price = show_price
        self.show_micros = show_micros

    def __str__(self):
        return self.name

    def get_total_nutrition(self):
        if self.meal_list:
            total_nutrition = np.zeros(self.meal_list[0].get_nutrition().shape[0])
            for meal in self.meal_list:
                total_nutrition += meal.get_nutrition()
            return total_nutrition
        else:
            print('No meals today!')
            return None

    def get_meal_list(self):
        return self.meal_list


    def get_nutrition(self):

        print(self.name)
        print(len(self.name)*'#' + '\n')
        total_micros = [0, 0, 0, 0]
        for meal in self.get_meal_list():
            meal_nutri = meal.get_nutrition().tolist()
            self.print_nutrition(meal.__str__(), meal_nutri)
            self.print_percentages(meal_nutri)
            if self.show_micros:
                meal_micros = meal.get_micros()
                total_micros = list(map(add, meal_micros, total_micros) )
                self.print_micros(meal_micros)

        total_nutri = self.get_total_nutrition().tolist()
        self.print_nutrition('Total', total_nutri)
        self.print_percentages(total_nutri)
        if self.show_micros:
            self.print_micros(total_micros)
            print('Micros goals: sodium: [3000, 5000], potassium: +47000, magnesium: +400mg')
        if self.show_price:
            self.print_price()

    def print_nutrition(self, title, nutrition_list):
        if self.is_keto:
            print(title + ':')
            print(len(title)*'-')
            print('kcal: {0:.2f}, protein: {1:.2f}gr, '
            'carbs: {2:.2f}gr, fats: {3:.2f}gr, net_carbs: {4:.2f}gr'.format(nutrition_list[0],
                                                                          nutrition_list[1],
                                                                          nutrition_list[2],
                                                                          nutrition_list[3],
                                                                          nutrition_list[4]))
        else:
            print(title + ':')
            print(len(title)*'-')
            print('kcal: {0:.2f}, protein: {1:.2f}gr, '
            'carbs: {2:.2f}gr, fats: {3:.2f}gr'.format(nutrition_list[0],
                                                      nutrition_list[1],
                                                      nutrition_list[2],
                                                      nutrition_list[3]))
    def print_micros(self, micros_list):
        print('sodium: {0:.2f}mg, potassium: {1:.2f}mg, '
        'magnesium: {2:.2f}mg, omega3: {3:.2f}mg\n'.format(micros_list[0],
                                                          micros_list[1],
                                                          micros_list[2],
                                                          micros_list[3]))

    def print_percentages(self, nutrition_list):
        if self.is_keto:
            kcal = nutrition_list[0]
            protein = nutrition_list[1]
            carbs = nutrition_list[2]
            fats = nutrition_list[3]
            net_carbs = nutrition_list[4]
            # calculate percentages
            protein_percent = protein * 4 * 100 / kcal
            carbs_percent = carbs * 4 * 100 / kcal
            fats_percent = fats * 9 * 100 / kcal
            net_carbs_percent = net_carbs * 4 * 100 / kcal
            print('kcal: {0:.2f}%, protein: {1:.2f}%, carbs: {2:.2f}%, '
            'fats: {3:.2f}%, net_carbs: {4:.2f}%'.format(100,
                                                      protein_percent,
                                                      carbs_percent,
                                                      fats_percent,
                                                      net_carbs_percent))
        else:
            kcal = nutrition_list[0]
            protein = nutrition_list[1]
            carbs = nutrition_list[2]
            fats = nutrition_list[3]
            # calculate percentages
            protein_percent = protein * 4 * 100 / kcal
            carbs_percent = carbs * 4 * 100 / kcal
            fats_percent = fats * 9 * 100 / kcal
            print('kcal: {0:.2f}%, protein: {1:.2f}%, carbs: {2:.2f}%, '
            'fats: {3:.2f}%\n'.format(100,
                                      protein_percent,
                                      carbs_percent,
                                      fats_percent))


    def print_statistics(self):
        print('Top 3 Ingredients per Macro:')
        print('----------------------------' + '\n')
        statistics = self.get_statistics()
        for key, value in statistics.items():
            print(key + ': ' + value + '\n')

    def print_price(self):
        total_price = 0
        price_csv = pd.read_csv('keto-price.csv', header=None, sep='\t')
        print('\nPrice')
        print('-----')
        for meal in self.get_meal_list():
            meal_price = 0
            for ingr in meal.get_ingredient_list():
                factor = ingr.get_quantity() / price_csv[price_csv.iloc[:,0] == ingr.get_name()].iloc[:,1].values[0]
                price = price_csv[price_csv.iloc[:,0] == ingr.get_name()].iloc[:,2].values[0] * factor
                meal_price += price
            print('{0}: £{1:.2f}'.format(meal.__str__(), meal_price))
            total_price += meal_price
        print('Total: £{0:.2f}'.format(total_price))
