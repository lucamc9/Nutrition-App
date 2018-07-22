from meal_planner import *
from keto_meals import *

lunch = Meal('Lunch', lunch_ingr_2, is_keto=True)
dinner = Meal('Dinner', dinner_ingr_2, is_keto=True)
keto_day = Day('Keto Day', [lunch, dinner], show_price=True)
keto_day.get_nutrition()