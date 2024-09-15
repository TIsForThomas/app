from raid_values import *
from entity_health import *
print(garageDoor)

























selectedEntity = input("Please select the the number that corresponds to the entity you are trying to : 1=Wood Door, 2=Metal Door, 3=Garage Door, 4=Armored Door")

if selectedEntity == "1":
    print("You selected: Wood Door")
elif selectedEntity == "2":
    print("You selected: Metal Door")
elif selectedEntity == "3":
    print("You selected: Garage Door")
elif selectedEntity == "4":
    print("You selected: Armored Door")
else:
    print("invalid Input")
