from meal_planner import *
from keto_meals import *

lunch = Meal('Lunch', lunch_ingr_3, is_keto=True)
dinner = Meal('Dinner', dinner_ingr_3, is_keto=True)
keto_day = Day('Keto Day', [lunch, dinner])
keto_day.get_nutrition()
