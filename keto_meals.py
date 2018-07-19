from meal_planner import *

lunch_ingr_1 = [('Egg', 4),
                ('Lettuce', 150),
                ('Mustard', 15),
                ('GreekYoghurt', 150),
                ('CheddarCheese', 50),
                ('Almonds', 23)]

breakfast_1 = Meal('Lunch', lunch_ingr_1, is_keto=True)
# dinner_1 = Meal('Dinner', dinner_ingr_1)
keto_day_1 = Day('Keto 1', [breakfast_1])

keto_day_1.get_nutrition()
