import random
import math
import os

cheats:bool = False

# százalékban, a landoláskor való felrobbanás esélye
chance_of_explosion:int=30
fuel:int = 2
# az üzemanyagtartály mérete, a jelenlegi üzemanagy + venni kívánt üzemanyag ezt nem haladhatja meg
max_fuel:int = 2
credits:int = 10
# áru
goods:int = 0
max_goods:int = 5
goods_have_been_sold:bool = False
# a bolt tárgyai
shop_fuel:int
shop_goods:int
shop_equipment:str = []
shop_has_been_generated:bool = False
# a felszereléseink
equipment:str = []
# hol vagyunk a térképen, vagyis a térkép lista indexe
location:int = 0
# térkép, vagyis bolygók listája, az űrt 3*_-al jelöljük
map:str = ["Thorodin", "Ydalir", "Vidar", "___", "Folkvang"]
# Technikaifejlettség, min 1 és max 15, az űrt 0-val jelöljük
# a map-al "együtt műkődik" szóval a map[0] bolygó technikaifejlettsége ennek a listának a [0] eleme
tech_map:int = [2, 4, 10, 0, 6]
# az adott indexű bolygónak van-e teleszkópja
# a map-al "együtt működik"
telescope_map:bool = [False, False, False, False, True]

def status():
    global goods_have_been_sold
    clear_screen()
    print(">>>>>------------------STATUS------------------<<<<<")
    print(f"change of explosion on landing:  {chance_of_explosion}%")
    print(f"fuel:  {fuel}/{max_fuel}")
    #print(f"location: {map[location]}")
    #print(f"map: {map}")
    print(f"map:  {gps()}")
    print(f"tech map:  {tech_map}")
    print(f"available telescopes:  {available_telescopes()}")
    #print(f"avarage tech level:  {tech_map_avarage()}")
    print("----------------------------------------------------")
    if(goods_have_been_sold):
        print(f"\n{5} goods sold for {5} credits\n")
        goods_have_been_sold = False
    print(f"credits:  ${credits}")
    print(f"goods:  {goods}/{max_goods}")
    print(f"equipment:  {equipment}")
    print("----------------------------------------------------")
    print("possible inputs:  travel, buy, telescope")
    if(cheats): print("cheats:  /fuel, /credits, /planet, /explosion chance")
    print("----------------------------------------------------")

def travel():
    global location
    global fuel
    global chance_of_explosion
    global goods_have_been_sold
    global shop_has_been_generated
    goods_have_been_sold = False
    destination:str = str(input("where do you want to travel?: "))
    if(destination == "___"):
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
            print(f"\n---you dont have enough fuel---\nfuel needed: {fuelconsumption}   you have: {fuel}\n")
            print("Press Enter to continue.")
            input()
        else:
            if(random.randrange(1, 101) <= chance_of_explosion):
                clear_screen()
                print("\nGAME OVER: you exploded\n")
                print("Press Enter to exit...")
                input()
                exit()
            else:
                # utazunk, vagyis a helyt átállítjuk a célra
                location=map.index(destination)
                fuel -= fuelconsumption
                if(chance_of_explosion != 0): chance_of_explosion -= 1
                # sikeres utazásnál automatikusan eladjuk az árut
                ...
                #goods_have_been_sold = True
                # utazás után a boltot újra lehet generálni
                shop_has_been_generated = False
    else:
        print("\n---destination does not exist---\n")
        print("Press Enter to continue.")
        input()

def buy():
    if(shop_has_been_generated == False):
        generate_shop()
    print("shop items:")
    print(f"{shop_fuel} fuel")
    print(f"{shop_goods} goods")
    print(f"equipment: {shop_equipment}")
    to_buy:str=str(input("what do you want to buy?: "))

def telescope():
    if(telescope_map[location] == True):
        print("do you want to use the telescope for $10? (yes/no): ")
        print("Press Enter to continue.")
        input()
    else:
        print("\n---this planet doesn't have a telescope---\n")
        print("Press Enter to continue.")
        input()





# a jelenlegi bolygó boltjának tárgyait legenerálja, a technikaifejlettségétől függően
def generate_shop():
    global shop_fuel
    global shop_goods
    global shop_equipment
    global shop_has_been_generated
    # üzemanyag generálása 1 és 5 között a technikaifejlettségtől függően
    # ennek köszönhetően, óvatosan kell olyan alacsony technikaifejlettségő bolygóra utazni, ami más bolygóktól messze van, mert ottragadhatunk
    min:int = math.ceil(tech_map[location]/3) - 1
    max:int = math.ceil(tech_map[location]/3) + 4
    temp:int = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    if(5 < temp): temp = 5
    shop_fuel = temp

    shop_goods = 0

    shop_equipment = ["fart"]

    shop_has_been_generated = True

# generál egy új bolygót, hozzá technikaifejlettségi szintet, teleszkópot, és hozzáadja a térképhez
def add_new_planet():
    global map
    global tech_map
    VOWELS:str = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS:str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    if(random.randrange(1,101) <= 40 and (map[-1] != "___" or map[-2] != "___" or map[-3] != "___")):
        # 40% esélye van, hogy űrt generálunk, ha a "map" utolsó 3 eleme között van bolygó
        # ennek köszönhetően, ha generálódik 2 vagy 3 űr egymás után, akkor fejlesztenünk kell az üzemanyagtartályt, hogy át tudjuk utazni ezeket
        planet_name:str = "___"
        map.append(planet_name)
        tech_map.append(0)
        telescope_map.append(False)
    else:
        # a bolygó nevének random generálása
        planet_name:str = map[0]
        # ellenőrízzük hogy ne forduljon elő már a "map"-ban, erre kicsi az esély, de elengedhetetlen a játék korrekt működéséhez
        while(planet_name in map):
            planet_name:str = ""
            for i in range(random.randrange(3, 7)):
                if(len(planet_name) == 0):
                    if(random.randrange(1, 101) <= 80):
                        planet_name += random.choice(CONSONANTS).upper()
                    else:
                        planet_name += random.choice(VOWELS).upper()
                else:
                    if(planet_name[-1].lower() in VOWELS):
                        planet_name += random.choice(CONSONANTS)
                    else:
                        planet_name += random.choice(VOWELS)
        map.append(planet_name)
        # generáljuk az új bolygó technikaifejlettségét az átlagos technikaifejlettséghez relatívan random
        # így ahogy generálunk több és több bolygót, egyre magasabb lesz a technikaifejlettségük általában
        min:int = tech_map_avarage() - 6
        max:int = tech_map_avarage() + 8
        temp:int = random.randrange(min, max + 1)
        # nem  while(temp < 1 or 15 < temp)
        # ez a módszer jobb, mivel a nagyobb szám generálásának esélye nagyobb lesz, még akkor is ha a max 15 felé esik
        # tehát ha "tech_map_avarage()" = 14, akkor nagyobb eséllyel generál 15-öt,  mint 13-at, 12-őt, 11-et, 10-et stb... együtt
        if(temp < 1): temp = 1
        if(15 < temp): temp = 15
        tech_map.append(temp)
        # ha a technikaifejlettség 15, akkor 50% eséllyel lesz teleszkóp, ha 14 akkor 46%, ha 13 akkor 43%, ha 12 akkor 40%, stb...
        if(random.randrange(1, 101) <= (temp * 3.34)):
            telescope_map.append(True)
        else: telescope_map.append(False)

# visszatér egy olyan térképpel ami mutatja hol vagyunk jelenleg
def gps():
    string:str = ""
    for i in range(len(map)):
        if(location == i): string += f"({map[i]}), "
        else: string += f"{map[i]}, "
    return string[:-2]

    '''
    list:str=[]
    for i in range(len(map)):
        if(i == location): list.append(f"({map[i]})")
        else: list.append(map[i])
    return list
    '''

def available_telescopes():
    string:str = ""
    for i in range(len(telescope_map)):
        if(telescope_map[i] == True):
            string += f"{map[i]}, "
    return string[:-2]

# formázottan kilistázza a felszereléseinket
def list_equipment():
    ...

def set_chance_of_explosion():
    global chance_of_explosion
    a:int = int(input("set chance of explosion to: "))
    while(a < 0 or 100 < a):
        a = int(input("chance of explosion must be from 0 to 100: "))
    chance_of_explosion = a

def set_fuel():
    global fuel
    global max_fuel
    a:int = int(input("set fuel to: "))
    fuel = a
    max_fuel = a + 4

def set_credits():
    global credits
    a:int = int(input("set credits to: "))
    credits = a

# kiszámolja az utolsó 5 technikaifejlettség átlagát, a 0 vagyis űr mezőket nem beleértve, és felfelé kerekíti
def tech_map_avarage():
    filtered_list:int=[]
    for i in range(len(tech_map)-5, len(tech_map), 1):
        if(tech_map[i] != 0): filtered_list.append(tech_map[i])
    return math.ceil(sum(filtered_list) / len(filtered_list))

# operációs rendszerhez alkalmazkodó képernyő tisztító (teljesen a ChatGPT generálta)
def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')