from meal_planner import *

breakfast_ingredients_1 = [('EggWhite', 5),
                           ('Egg', 1),
                           ('Mushrooms', 125),
                           ('Oil', 1),
                           ('Almond', 5),
                           ('Pecan', 5)]

breakfast_1 = Meal('Breakfast', breakfast_ingredients_1)
normal_day = Day('Standard', [breakfast_1])

normal_day.print_nutrition()
