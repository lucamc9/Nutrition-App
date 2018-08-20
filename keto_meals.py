from meal_planner import *

# 1 Standard work day
lunch_ingr_1 = [('Egg', 4),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('KalaOlives', 35),
('Oil', 15),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Salt', 2)]

dinner_ingr_1 = [('TunaSunOil', 1),
('Avocado', 170),
('PistachiosSalted', 15),
('SunflowerSeeds', 30),
('Spinach', 50),
('Kale', 50),
('Oil', 15),
('ParmesanCheese', 30),
('Blueberries', 25),
('Salt', 2)]

# 2 Saturday & Sundays
lunch_ingr_2 = [('RoastChicken', 0.25),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('KalaOlives', 35),
('Avocado', 170),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Oil', 15),
('Salt', 2)]

dinner_ingr_2 = [('RoastChicken', 0.25),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('SunflowerSeeds', 30),
('Oil', 15),
('PistachiosSalted', 30),
('Blueberries', 40),
('Jerky', 35),
('Salt', 2)]

# 3 Special work day (1)
lunch_ingr_3 = [('RumpSteak', 252),
('Butter', 20),
('Spinach', 20),
('CeaserDressing', 1),
('Almonds', 25)]

dinner_ingr_3 = [('Avocado', 1),
('CheddarCheese', 60),
('Salami', 25),
('Spinach', 50),
('SunflowerSeeds', 25),
('Pistachios', 15),
('Oil', 1)]

# nandos
nandos = [('NandosHalfChix', 1),
('AlmondsSalted', 30),
('Olives', 70)]

dinner_ingr_4 = [('Avocado', 340),
('Oil', 30),
('AlmondsSalted', 30)]

# appleton
appleton_1 = [('Spinach', 100),
('ParmesanCheese', 100),
('Olives', 35),
('Avocado', 170),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Oil', 20),
('BaconTesco', 35),
('RoastBeefTesco', 90),
('Salt', 2)
]
appleton_2 = [('Spinach', 100),
('ParmesanCheese', 100),
('Olives', 35),
('SunflowerSeeds', 30),
('BaconTesco', 35),
('RoastBeefTesco', 90),
('Oil', 20),
('Salt', 2),
('AlmondsSalted', 30),
]

"""
Month 1: W - , BF -
Gym 5 days a week plan (70%, 25%, 5%):
- 3 weight lifting : {Chest, biceps, obliques}, {Legs, shoulders, abs}, {Back, triceps, obliques} (2500 kcal)
- 2 cardio: {Run, Skipping, Boxing, abs} x2 (2750 kcal)
- 2 weekend rest days (2250 kcal)
All <£9 a day

Month 2: +250 kcals
"""

# Weight lifting days
lunch_weights_ingr = [('Egg', 4),
('ParmesanCheese', 50),
('Spinach', 50),
('Kale', 50),
('KalaOlives', 35),
('Oil', 20),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Salt', 2)]

dinner_weights_ingr = [('Tuna', 204),
('Avocado', 170),
('PistachiosSalted', 15),
('SunflowerSeeds', 30),
('Spinach', 50),
('Kale', 50),
('Oil', 20),
('ParmesanCheese', 50),
('Blueberries', 50),
('Salt', 2)]

# Cardio days
lunch_cardio_ingr = [('Egg', 4),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('KalaOlives', 35),
('Oil', 15),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Salt', 2)]

dinner_cardio_ingr = [('TunaSunOil', 1),
('Avocado', 170),
('PistachiosSalted', 15),
('SunflowerSeeds', 30),
('Spinach', 50),
('Kale', 50),
('Oil', 15),
('ParmesanCheese', 30),
('Blueberries', 25),
('Salt', 2)]

# Days off
lunch_off_ingr = [('RoastChicken', 0.25),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('KalaOlives', 35),
('Avocado', 170),
('SunflowerSeeds', 30),
('AlmondsSalted', 30),
('Oil', 15),
('Salt', 2)]

dinner_off_ingr = [('RoastChicken', 0.25),
('ParmesanCheese', 30),
('Spinach', 50),
('Kale', 50),
('SunflowerSeeds', 30),
('Oil', 15),
('PistachiosSalted', 30),
('Blueberries', 40),
('Jerky', 35),
('Salt', 2)]
