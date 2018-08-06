from meal_planner import *
from keto_meals import *

lunch = Meal('Lunch', lunch_ingr_1, is_keto=True)
dinner = Meal('Dinner', dinner_ingr_1, is_keto=True)
keto_day = Day('Keto Day', [lunch, dinner], show_micros=True, show_price=True)

lunch_2 = Meal('Lunch', nandos, is_keto=True)
dinner_2 = Meal('Dinner', dinner_ingr_4, is_keto=True)
nandos_day = Day('Nandos day', [lunch_2, dinner_2], show_micros=True, show_price=True)

app_lunch = Meal('Lunch', appleton_1, is_keto=True)
app_dinner = Meal('Dinner', appleton_2, is_keto=True)
appleton_day = Day('Appleton day', [app_lunch, app_dinner], show_micros=True, show_price=True)
appleton_day.get_nutrition()
