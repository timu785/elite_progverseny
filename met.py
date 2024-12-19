import random

# százalékban, a landoláskor való felrobbanás esélye
chance_of_explosion:int=30
fuel:int = 2
# hol vagyunk a térképen, vagyis a string lista indexe
location:int = 0
# térkép, vagyis bolygók listája, az űrt 5*_-al jelöljük
map:str = ["Thorodin", "Ydalir", "Vidar", "_____", "Folkvang"]

# az üzemanyagtartály mérete, a jelenlegi üzemanagy + venni kívánt üzemanyag ezt nem haladhatja meg
size_of_tank:int = 2

def status():
    print("-----------------------STAUTS-----------------------")
    print(f"change of explosion on landing: {chance_of_explosion}%")
    #print(f"location: {map[location]}")
    #print(f"map: {map}")
    print(f"map: {gps()}")
    print(f"fuel: {fuel}")
    print("----------------------------------------------------")

# visszatér egy olyan térképpel ami mutatja hol vagyunk jelenleg
def gps():
    list:str=[]
    for i in range(len(map)):
        if(i == location): list.append(f"({map[i]})")
        else: list.append(map[i])
    return list

def travel():
    destination:str = str(input("where do you want to travel: "))
    global location
    global fuel
    global chance_of_explosion
    if(destination == "_____"):
        print("there isnt a planet here")
    elif(destination == map[location]):
        print("you are already on this planet")
    elif(destination in map):
        fuelconsumption:int = abs(location-map.index(destination))
        if(fuelconsumption > fuel):
            print("you dont have enough fuel")
        else:
            if(random.randrange(1, 101) <= chance_of_explosion):
                print("GAME OVER: you exploded")
                print("Press Enter to exit...")
                input()
                exit()
            else:
                #sikeres utazásnál az üzemanyaghasználat levonódik
                fuel = fuel - fuelconsumption
                #utazunk, vagyis a helyszínt átállítjuk a célpontra
                location=map.index(destination) 
                #sikeres utazásonként a felrobbanás esélye eggyel csökken
                chance_of_explosion -= 1
    else: print("destination does not exist")
    status()

def buy():
    ...
