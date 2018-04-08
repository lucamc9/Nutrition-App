from meal_planner import *

# New main diet
breakfast_1 = Meal('Breakfast', [('EggWhite', 5),
                               ('BrownBread', 4),
                               ('Egg', 1),
                               ('SoyMilk', 300),
                               ('Mushrooms', 125),
                               ('Potatoes', 200),
                               ('Oil', 1),
                               ('Onion', 1),
                               ('Almond', 5),
                               ('Pecan', 5),
                               ('Raisins', 14),
                               ('Weetabix', 2),
                               ('Apple', 1)])

dinner_1 = Meal('Dinner', [('Huel', 125),
                         ('Blueberries', 33),
                         ('Raspberries', 33),
                         ('Blackberries', 50),
                         ('Banana', 1)])
# 20/4/18
breakfast = Meal('Breakfast', [('EggWhite', 3),
                                ('BrownBread', 2),
                                ('Egg', 1),
                                ('SoyMilk', 300),
                                ('Oil', 1),
                                ('Almond', 5),
                                ('Pecan', 5),
                                ('Raisins', 14),
                                ('Weetabix', 2),
                                ('Apple', 1)])

lunch = Meal('Dinner', [('Huel', 125),
                         ('Blueberries', 33),
                         ('Raspberries', 33),
                         ('Blackberries', 50),
                         ('Banana', 1)])

dinner = Meal('Dinner', [('Mushrooms', 125),
                         ('Onion', 1),
                         ('Pasta', 125),
                         ('ChickenBreast', 300),
                         ('NutBar', 1)])

day_20_4 = Day('20/4/18', [breakfast, lunch, dinner])
normal_day = Day('standard', [breakfast_1, dinner_1])

# breakfast_nutri = breakfast.get_nutrition().tolist()
# dinner_nutri = dinner.get_nutrition().tolist()
# # total_nutri = (breakfast.get_nutrition() + dinner.get_nutrition()).tolist()
# day_one = Day('One', [breakfast, dinner])
# total_nutri = day_one.get_total_nutrition().tolist()

for meal in normal_day.get_meal_list():
    meal_nutri = meal.get_nutrition().tolist()
    print(meal.__str__())
    print('--------')
    print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f}'.format(meal_nutri[0],
                                                                                 meal_nutri[1],
                                                                                 meal_nutri[2],
                                                                                 meal_nutri[3],))
total_nutri = normal_day.get_total_nutrition().tolist()
print('Total:')
print('----------')
print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f}'.format(total_nutri[0],
                                                                             total_nutri[1],
                                                                             total_nutri[2],
                                                                             total_nutri[3],))
# print('Breakfast:')
# print('----------')
# print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f}'.format(breakfast_nutri[0],
#                                                                              breakfast_nutri[1],
#                                                                              breakfast_nutri[2],
#                                                                              breakfast_nutri[3],))
# print('Dinner:')
# print('----------')
# print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f}'.format(dinner_nutri[0],
#                                                                              dinner_nutri[1],
#                                                                              dinner_nutri[2],
#                                                                              dinner_nutri[3],))
# print('Total:')
# print('----------')
# print('kcal: {0:.2f}, protein: {1:.2f}, carbs: {2:.2f}, fat: {3:.2f}'.format(total_nutri[0],
#                                                                              total_nutri[1],
#                                                                              total_nutri[2],
#                                                                              total_nutri[3],))
