import pandas as pd
import numpy as np

class Macro:

    def __init__(self, name, value=None):
        self.name = name
        self.value = value

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
        self.quantity = quantity
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

    def __init__(self, name, ingredient_list=None):
        self.name = name
        self.ingredient_db = self.get_db()
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
        nutrition = np.zeros(4)
        for ingredient in self.ingredient_list:
            macro_list = ingredient.get_macros()
            macro_values = [macro.get_value() for macro in macro_list]
            nutrition += np.array(macro_values)
        return nutrition

    def remove_ingredient(self, ingredient):
        self.ingredient_list = [x for x in self.ingredient_list if x.get_name() != ingredient]

    def get_high_macros(self):
        kcals = []
        proteins = []
        carbs = []
        fats = []
        ingredients = self.get_ingredient_list()
        for ingredient in ingredients:
            macro_list = ingredient.get_macros()
            macro_values = [macro.get_value() for macro in macro_list]
            kcals.append(macro_values[0])
            proteins.append(macro_values[1])
            carbs.append(macro_values[2])
            fats.append(macro_values[3])

class Day:

    def __init__(self, name, meal_list=None):
        self.name = name
        self.meal_list = meal_list

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

    def print_nutrition(self):
        print('|' + self.name + '|' + '\n')
        for meal in self.get_meal_list():
            meal_nutri = meal.get_nutrition().tolist()
            print(meal.__str__())
            print('--------')
            print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f} \n'.format(meal_nutri[0],
                                                                                         meal_nutri[1],
                                                                                         meal_nutri[2],
                                                                                         meal_nutri[3]))

        total_nutri = self.get_total_nutrition().tolist()
        print('Total:')
        print('----------')
        print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f} \n'.format(total_nutri[0],
                                                                                    total_nutri[1],
                                                                                    total_nutri[2],
                                                                                    total_nutri[3]))
