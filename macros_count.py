from meal_planner import *
from keto_meals import *

lunch = Meal('Lunch', lunch_ingr_2, is_keto=True)
dinner = Meal('Dinner', dinner_ingr_2, is_keto=True)
keto_day = Day('Keto Day', [lunch, dinner], show_micros=True, show_price=True)

lunch_2 = Meal('Lunch', nandos, is_keto=True)
dinner_2 = Meal('Dinner', dinner_ingr_4, is_keto=True)
nandos_day = Day('Nandos day', [lunch_2, dinner_2], show_micros=True, show_price=True)

app_lunch = Meal('Lunch', appleton_1, is_keto=True)
app_dinner = Meal('Dinner', appleton_2, is_keto=True)
appleton_day = Day('Appleton day', [app_lunch, app_dinner], show_micros=True, show_price=True)

# New plan
lunch_weights = Meal('Lunch Weights', lunch_weights_ingr, is_keto=True)
dinner_weights = Meal('Dinner Weights', dinner_weights_ingr, is_keto=True)
weights_day = Day('Weights Day', [lunch_weights, dinner_weights], show_micros=True, show_price=True)
weights_day.get_nutrition()

lunch_cardio = Meal('Lunch Cardio', lunch_cardio_ingr, is_keto=True)
dinner_cardio = Meal('Dinner Cardio', dinner_cardio_ingr, is_keto=True)
cardio_day = Day('Cardio Day', [lunch_cardio, dinner_cardio], show_micros=True, show_price=True)
#cardio_day.get_nutrition()

lunch_off = Meal('Lunch Day Off', lunch_off_ingr, is_keto=True)
dinner_off = Meal('Dinner Day Off', dinner_off_ingr, is_keto=True)
off_day = Day('Day Off', [lunch_off, dinner_off], show_micros=True, show_price=True)
# off_day.get_nutrition()
