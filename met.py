import random
import os

# százalékban, a landoláskor való felrobbanás esélye
chance_of_explosion:int=30
fuel:int = 2
# az üzemanyagtartály mérete, a jelenlegi üzemanagy + venni kívánt üzemanyag ezt nem haladhatja meg
size_of_tank:int = 2
# hol vagyunk a térképen, vagyis a térkép string lista indexe
location:int = 0
# térkép, vagyis bolygók listája, az űrt 5*_-al jelöljük
map:str = ["Thorodin", "Ydalir", "Vidar", "_____", "Folkvang"]
# Technikaifejlettség, az űrt 0-val jelöljük, min 1 és max 15
# a map-al "együtt műkődik" szóval a map[0] bolygó technikaifejlettsége ennek a listának a [0] eleme
tech_level:int = [2, 4, 10, 0, 6]

def status():
    os.system('cls')
    print("O----------------------STAUTS----------------------O")
    print(f"change of explosion on landing: {chance_of_explosion}%")
    #print(f"location: {map[location]}")
    #print(f"map: {map}")
    print(f"map: {gps()}")
    print(f"tech: {tech_level}")
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
    global location
    global fuel
    global chance_of_explosion
    destination:str = str(input("where do you want to travel: "))
    if(destination == "_____"):
        print("you cant land here")
    elif(destination == map[location]):
        print("you are already on this planet")
    elif(destination in map):
        # az üzemanyaghasználat a helyünk és a célünk különbségének abszolútértéke
        fuelconsumption:int = abs(location-map.index(destination))
        if(fuelconsumption > fuel):
            print("you dont have enough fuel")
        else:
            if(random.randrange(1, 101) <= chance_of_explosion):
                print("\nGAME OVER: you exploded\n")
                print("Press Enter to exit...")
                input()
                exit()
            else:
                #sikeres utazásnál az üzemanyaghasználat levonódik
                fuel = fuel - fuelconsumption
                #utazunk, vagyis a helyt átállítjuk a célra
                location=map.index(destination) 
                #sikeres utazásonként a felrobbanás esélye eggyel csökken
                chance_of_explosion -= 1
    else: print("destination does not exist")

# generál egy új bolygót, és hozzáadja a térképhez
def add_new_planet():
    global map
    global tech_level
    VOWELS:str = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS:str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    # 40% esélye van, hogy űrt generálunk
    if(random.randrange(1,101) <= 40):
        planet_name:str = "_____"
    else:
        # beállítjuk map[0]-ra, hogy belépjen a while ciklusba
        planet_name:str = map[0]
        # ellenőrízzük hogy ne forduljon elő már a "map"-ban, erre kicsi az esély, de elengedhetetlen a játék korrekt működéséhez
        while(planet_name in map):
            planet_name:str = ""
            # a bolygó random nevének generálása, hossza random, min 2 és max 6
            for i in range(random.randrange(2, 7)):
                # Kezdőbetű: a bolygó neve 80% eséllyel mássalhangzóval kezdődik
                if(len(planet_name) == 0):
                    if(random.randrange(1, 101) <= 80):
                        planet_name = planet_name + random.choice(CONSONANTS).upper()
                    else:
                        planet_name = planet_name + random.choice(VOWELS).upper()
                # Folytatás: a magánhangzókat mássalhangzók követik, és fordítva
                else:
                    if(planet_name[-1].lower() in VOWELS):
                        planet_name = planet_name + random.choice(CONSONANTS)
                    else:
                        planet_name = planet_name + random.choice(VOWELS)
    map.append(planet_name)
    if(planet_name == "_____"):
        tech_level.append(0)
    else:
        tech_level.append(random.randrange(1, 16))


def explore():
    ...

def buy():
    ...



def tech_level_avarage():
    ...