from meal_planner import *

'''
-- Description
This script is a demo for the meal_planner program.

This program allows you to pull data from a database nutrition.csv /
keto-nutrition.csv and create a daily meal plan, allowing you to keep track of
important macros.

-- Usage:
$ python meals-demo.py

To build your own, create a new meals.py file and replicate the example below
with your own ingredients, meals and days.

-- Database format
The database is a csv file separated by tabs ('\t') with the following format:
<Name> <Measurement> <Quantity> <kcal> <protein> <carbs> <fat>

In the case of the keto-nutrition.csv there is an extra column <fibre>

-- Ingredients format
[('Ingredient_1', Quantity_1), ('Ingredient_2', Quantity_2), ..., ('Ingredient_N', Quantity_N)]

-- Meal format
Meal(Name, Ingredients)

-- Day format
Day(Name, Meal_List)
'''

# breakfast_ingredients = [('EggWhite', 5),
#                            ('BrownBread', 4),
#                            ('Egg', 1),
#                            ('SoyMilk', 300),
#                            ('Mushrooms', 125),
#                            ('Potatoes', 200),
#                            ('Oil', 1),
#                            ('Onion', 1),
#                            ('Almond', 5),
#                            ('Pecan', 5),
#                            ('Raisins', 14),
#                            ('Weetabix', 2),
#                            ('Apple', 1)]
#
# dinner_ingredients = [('Huel', 125),
#                         ('Blueberries', 33),
#                         ('Raspberries', 33),
#                         ('Blackberries', 50),
#                         ('Banana', 1)]
#
# breakfast = Meal('Breakfast', breakfast_ingredients)
# dinner = Meal('Dinner', dinner_ingredients)
# normal_day = Day('Demo', [breakfast, dinner])
#
# normal_day.get_nutrition()

breakfast_ingredients = [('EggWhite', 5),
                         ('Egg', 1),
                         ('Mushrooms', 125),
                         ('Oil', 1),
                         ('Onion', 1),
                         ('Almond', 5),
                         ('Pecan', 5)]

dinner_ingredients = [('Tuna', 125),
                      ('Lettuce', 100),
                      ('Cucumber', 0.5),
                      ('Blueberries', 33),
                      ('Raspberries', 33),
                      ('Blackberries', 50)]

breakfast = Meal('Breakfast', breakfast_ingredients, is_keto=True)
dinner = Meal('Dinner', dinner_ingredients, is_keto=True)
keto_day = Day('Keto Demo', [breakfast, dinner])

keto_day.get_nutrition()
