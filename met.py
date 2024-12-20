import random
import os

cheats:bool = False

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
tech_levels:int = [2, 4, 10, 0, 6]

def status():
    clear_screen()
    print("O----------------------STATUS----------------------O")
    print(f"change of explosion on landing:  {chance_of_explosion}%")
    print(f"fuel:  {fuel}")
    #print(f"location: {map[location]}")
    #print(f"map: {map}")
    print(f"map:  {gps()}")
    print(f"tech:  {tech_levels}")
    print(f"avarage tech level:  {tech_levels_avarage(tech_levels)}")
    print("----------------------------------------------------")
    print("possible inputs:  travel, buy, explore")
    if(cheats): print("cheats:  /planet, /fuel, /explosion chance")
    print("----------------------------------------------------")

def travel():
    global location
    global fuel
    global chance_of_explosion
    destination:str = str(input("where do you want to travel: "))
    if(destination == "_____"):
        print("\n---you cant land here---\n")
        print("Press Enter to continue.")
        input()
    elif(destination == map[location]):
        print("\n---you are already on this planet---\n")
        print("Press Enter to continue.")
        input()
    elif(destination in map):
        # az üzemanyaghasználat a helyünk és a célünk különbségének abszolútértéke
        fuelconsumption:int = abs(location-map.index(destination))
        if(fuelconsumption > fuel):
            print("\n---you dont have enough fuel---\n")
            print("Press Enter to continue.")
            input()
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
    else:
        print("\n---destination does not exist---\n")
        print("Press Enter to continue.")
        input()

def buy():
    ...

def telescope():
    ...



# visszatér egy olyan térképpel ami mutatja hol vagyunk jelenleg
def gps():
    list:str=[]
    for i in range(len(map)):
        if(i == location): list.append(f"({map[i]})")
        else: list.append(map[i])
    return list

# generál egy új bolygót, hozzá egy technikaifejlettségi szintet, és hozzáadja a térképhez
def add_new_planet():
    global map
    global tech_levels
    VOWELS:str = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS:str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    # 40% esélye van, hogy űrt generálunk, ha a "map" utolsó 3 eleme között van bolygó
    if(random.randrange(1,101) <= 40 and (map[-1] != "_____" or map[-2] != "_____" or map[-3] != "_____")):
        planet_name:str = "_____"
        tech_levels.append(0)
    else:
        # a bolygó nevének random generálása
        planet_name:str = map[0]
        # ellenőrízzük hogy ne forduljon elő már a "map"-ban, erre kicsi az esély, de elengedhetetlen a játék korrekt működéséhez
        while(planet_name in map):
            planet_name:str = ""
            # nevének hossza random, min 3 és max 6
            for i in range(random.randrange(3, 7)):
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
        # generáljuk az új bolygó technikaifejlettségét az átlagos technikaifejlettséghez relatívan random
        # így ahogy generálunk több és több bolygót, egyre magasabb lesz a technikaifejlettségük
        min:int = tech_levels_avarage(tech_levels)-6
        max:int = tech_levels_avarage(tech_levels)+7
        temp:int = random.randrange(min, max + 1)
        # nem  while(temp < 1 or 15 < temp)
        # ez a módszer jobb, mivel a nagyobb szám generálásának esélye nagyobb lesz, akkor is ha a max 15 felé esik
        # tehát ha "tech_levels_avarage" = 13, akkor nagyobb eséllyel generál nagyobb számot, mint kisebb számot
        if(temp < 1): temp = 1
        if(15 < temp): temp = 15
        tech_levels.append(temp)
    map.append(planet_name)

def set_chance_of_explosion():
    global chance_of_explosion
    a:int = int(input("set chance of explosion to: "))
    chance_of_explosion = a

def set_fuel():
    global fuel
    a:int = int(input("set fuel to: "))
    fuel = a

# kiszámolja az utolsó 5 technikaifejlettség átlagát, a 0 vagyis űr mezőket nem beleértve, és felfele kerekíti
def tech_levels_avarage(list:int):
    filtered_list:int=[]
    for i in range(len(list)-5, len(list), 1):
        if(list[i] != 0): filtered_list.append(list[i])
    return int(sum(filtered_list) / len(filtered_list)) + 1

# operációs rendszerhez alkalmazkodó képernyő tisztító (teljesen a ChatGPT generálta)
def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')