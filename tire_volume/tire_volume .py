import math
from datetime import datetime, timedelta
from webbrowser import open_new

userTime = datetime.now()

tireWidth = int(input("Please enter the tire width in mm "))
tireRatio = int(input("Please enter the tire aspect ratio in mm "))
tireDiameter = int(input("Please enter the tire diameter in mm "))

tireVolume = (math.pi * (tireWidth ** 2) * tireRatio * (tireWidth * tireRatio + 2540 * tireDiameter)) / 10000000000

print(f"The approximate volume is {round(tireVolume, 2)} liters.")

userPrompt = str(input("Would you like to purchase tires? Enter Y for YES or N for NO: "))

with open ("volume.txt" , "at") as volumes_file:
    print(f"{userTime:%Y-%m-%d}, {tireWidth}, {tireRatio}, {tireDiameter}, {round(tireVolume, 2)}" , file=volumes_file)

if userPrompt == 'Y':
    userNumber = str(input("Please enter your number: "))
    with open ("volume.txt" , "at") as volumes_file:
        print(f"User's Phone number: {userNumber}" , file=volumes_file)

elif userPrompt == 'N':
    print('Okay, Have a nice day!')