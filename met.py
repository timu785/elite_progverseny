import random

# 2 = teli, 1 = félig, 0 = üres
fuel:int = 2
location:int = 0
# az "űrt" minding "_____"-el jelöljük, vagyis 5*_
map:str = ["Thorodin", "Ydalir", "Vidar", "_____", "Folkvang"]
# százalékban, a landoláskor való felrobbanás esélye
chanceofexplosion:int=30

def status():
    print(f"change of explosion on landing: {chanceofexplosion}%")
    print(f"location: {map[location]}")
    print(f"map: {map}")
    print(f"fuel: {fuel}")

def travel():
    destination:str = str(input("where do you want to travel: "))
    print("")
    global location
    global fuel
    global chanceofexplosion
    if(destination == "_____"):
        print("there isnt a planet here")
    elif(destination == map[location]):
        print("you are already on this planet")
    elif(destination in map):
        fuelconsumption:int = abs(location-map.index(destination))
        if(fuelconsumption > fuel):
            print("you dont have enough fuel")
        else:
            if(random.randrange(1, 101) <= chanceofexplosion):
                print("you exploded")
                print("Press Enter to exit...")
                input()
                exit()
            else:
                fuel = fuel - fuelconsumption
                location=map.index(destination) 
                chanceofexplosion -= 1
    else: print("destination does not exist")
    status()

def buy():
    ...
