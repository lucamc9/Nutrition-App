from meal_planner import *

# Standard
breakfast_ingredients_1 = [('EggWhite', 5),
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
                           ('Apple', 1)]

dinner_ingredients_1 = [('Huel', 125),
                        ('Blueberries', 33),
                        ('Raspberries', 33),
                        ('Blackberries', 50),
                        ('Banana', 1)]

breakfast_1 = Meal('Breakfast', breakfast_ingredients_1)
dinner_1 = Meal('Dinner', dinner_ingredients_1)
normal_day = Day('Standard', [breakfast_1, dinner_1])

# 20/4/18
breakfast_ingredients_2 = [('EggWhite', 3),
                           ('BrownBread', 2),
                           ('Egg', 1),
                           ('SoyMilk', 300),
                           ('Oil', 1),
                           ('Almond', 5),
                           ('Pecan', 5),
                           ('Raisins', 14),
                           ('Weetabix', 2),
                           ('Apple', 1)]
lunch_ingredients_2 = [('Huel', 125),
                       ('Blueberries', 33),
                       ('Raspberries', 33),
                       ('Blackberries', 50),
                       ('Banana', 1)]

dinner_ingredients_2 = [('Mushrooms', 125),
                        ('Onion', 1),
                        ('Pasta', 125),
                        ('ChickenBreast', 300),
                        ('NutBar', 1)]

breakfast_2 = Meal('Breakfast', breakfast_ingredients_2)
lunch_2 = Meal('Lunch', lunch_ingredients_2)
dinner_2 = Meal('Dinner', dinner_ingredients_2)
day_20_4 = Day('20/4/18', [breakfast_2, lunch_2, dinner_2])

# New training plan
wrap = [('Tortilla', 2),
        ('ChickenBreast', 300),
        ('Lettuce', 3),
        ('Cucumber', 0.5),
        ('Hummus', 80),
        ('Tomatoes', 2)]
breakfast_weights = Meal('Breakfast', breakfast_ingredients_1)
breakfast_weights.remove_ingredient('BrownBread')
breakfast_weights.add_ingredient_raw('ProteinShake', 1)
dinner_weights = Meal('Dinner', wrap)
weights_day = Day('Weight Lifting', [breakfast_weights, dinner_weights])


breakfast_thai = Meal('Breakfast', breakfast_ingredients_1)
breakfast_thai.remove_ingredient('BrownBread')
dinner_thai = Meal('Dinner', dinner_ingredients_1)
dinner_thai.add_ingredient_raw('Tuna', 120)
dinner_thai.add_ingredient_raw('BrownBread', 2)
thai_day = Day('Thai Training', [breakfast_thai, dinner_thai])




new_routine = [weights_day, thai_day]

for day in new_routine:
    day.print_nutrition()
