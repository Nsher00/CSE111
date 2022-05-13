import math

tireWidth = int(input("Please enter the tire width in mm "))
tireRatio = int(input("Please enter the tire aspect ratio in mm "))
tireDiameter = int(input("Please enter the tire diameter in mm "))

tireVolume = (math.pi * (tireWidth ** 2) * tireRatio * (tireWidth * tireRatio + 2540 * tireDiameter)) / 10000000000

print("The tire volume is approximately" , round(tireVolume , 2), "liters.")