import random
import math
import os

cheats:bool = False

# százalékban, a landoláskor való felrobbanás esélye
chance_of_explosion:int=30
fuel:int = 2
# az üzemanyagtartály mérete, a jelenlegi üzemanagy + venni kívánt üzemanyag ezt nem haladhatja meg
max_fuel:int = 2
credits:float = 10
# áru
goods:int = 0
max_goods:int = 5
goods_have_just_been_sold:bool = False
goods_sold:int
credits_gained:float
# a felszereléseink
equipment:str = []
# a bolt tárgyai
shop_fuel:int
shop_goods:int
shop_equipment:str = []
shop_equipment_prices:int = []
shop_has_been_generated:bool = False
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
    global goods_have_just_been_sold
    utilize_equipment()
    clear_screen()
    print(">>>>>------------------STATUS------------------<<<<<")
    if(chance_of_explosion != 0): print(f"change of explosion on landing:  {chance_of_explosion}%")
    print(f"fuel:  {fuel}/{max_fuel}")
    #print(f"location: {map[location]}")
    #print(f"map: {map}")
    print(f"map:  {gps()}")
    #print(f"tech map:  {tech_map}")
    print(f"available telescopes:  {available_telescopes()}")
    #print(f"avarage tech level:  {tech_map_avarage()}")
    print("----------------------------------------------------")
    if(goods_have_just_been_sold):
        print(f"\n{goods_sold} goods sold for {credits_gained} credits\n")
        goods_have_just_been_sold = False
    print(f"credits:  ${credits}")
    print(f"goods:  {goods}/{max_goods}")
    if(equipment): print(f"equipment:  {equipment}")
    print("----------------------------------------------------")
    print(f"days left: {100}")
    print(f"chances of winning: {0}%")
    print("----------------------------------------------------")
    print("possible inputs:  travel, buy, telescope")
    if(cheats): print("cheat:  /fuel, /credits, /planet, /explosion chance, /cheats")
    print("----------------------------------------------------")

def travel():
    global location
    global fuel
    global chance_of_explosion
    global shop_has_been_generated
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
                # utazunk, vagyis a helyt átállítjuk a cél helyére
                location=map.index(destination)
                fuel -= fuelconsumption
                if(chance_of_explosion != 0): chance_of_explosion -= 1
                # sikeres utazásnál automatikusan eladjuk az árut
                sell_goods()
                # utazás után a boltot újra lehet generálni, mert egy új bolygón vagyunk/eltelt idő és a már meglátogatott bolygók készletei frissültek
                shop_has_been_generated = False
    else:
        print("\n---destination does not exist---\n")
        print("Press Enter to continue.")
        input()

def buy():
    global credits
    global shop_fuel
    global shop_goods
    global fuel
    global goods
    if(shop_has_been_generated == False):
        generate_shop()
    print("shop items:\n")
    print(f"{shop_fuel} fuel   $1 per piece")
    print(f"{shop_goods} goods   $1 per piece\n")
    for i in range(len(shop_equipment)):
        print(f"{shop_equipment[i]}   ${shop_equipment_prices[i]}")
    to_buy:str=str(input("\nwhat do you want to buy?: "))
    if(to_buy == "fuel"):
        fuel_to_buy:int=int(input("how much fuel do you want to buy?: "))
        if((fuel_to_buy > credits) or (fuel_to_buy > shop_fuel) or (fuel + fuel_to_buy > max_fuel)):
            if(fuel_to_buy > credits):
                print("\n---you don't have enough credits---\n")
            if(fuel_to_buy > shop_fuel):
                print("\n---the shop doesn't have that much fuel---\n")
            if(fuel + fuel_to_buy > max_fuel):
                print("\n---your fuel tank is too small for that---\n")
            print("Press Enter to continue.")
            input()
        else:
            credits -= round(fuel_to_buy, 3)
            shop_fuel -= fuel_to_buy
            fuel += fuel_to_buy
    elif(to_buy == "goods"):
        goods_to_buy:int=int(input("how many goods do you want to buy?: "))
        if((goods_to_buy > credits) or (goods_to_buy > shop_goods) or (goods + goods_to_buy > max_goods)):
            if(goods_to_buy > credits):
                print("\n---you don't have enough credits---\n")
            if(goods_to_buy > shop_goods):
                print("\n---the shop doesn't have that many goods---\n")
            if(goods + goods_to_buy > max_goods):
                print("\n---you can't store that many goods---\n")
            print("Press Enter to continue.")
            input()
        else:
            credits -= round(goods_to_buy, 3)
            shop_goods -= goods_to_buy
            goods += goods_to_buy

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
    global shop_equipment_prices
    global shop_has_been_generated
    # üzemanyag random generálása 1 és 5 között a technikaifejlettségtől függően
    # ennek köszönhetően, óvatosan kell olyan alacsony technikaifejlettségű bolygóra utazni, ami más bolygóktól messze van, mert ottragadhatunk
    x:float = 15 / 5
    min:int = math.ceil(tech_map[location] / x) - 1
    max:int = math.ceil(tech_map[location] / x) + 4
    temp:int = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    if(5 < temp): temp = 5
    shop_fuel = temp

    # árú random generálása 0 és 20 között (1 és 21 között, utána kivonunk egyet), a technikaifejlettségtől függően
    x = 15 / 21
    min = math.ceil(tech_map[location] / x) - 4
    max = math.ceil(tech_map[location] / x) + 4
    temp:int = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    # a felső limit opcionális, ettől még 1 és 21 között lesz a randomgenerálás közepe (tech_map[location] / x), de ha 21 fölé esik akkor nem vágódik le
    #if(21 < temp): temp = 21
    temp -= 1
    shop_goods = temp

    # a felszerelések random generálása a technikaifejlettségtől függően
    shop_equipment = []
    shop_equipment_prices = []
    # ha a technikaifejlettség 6, akkor 108% eséllyel lesz dokkoló egység, ha 5 akkor 90%, ha 4 akkor 72%, ha 3 akkor 54% stb...
    if(random.randrange(1, 101) <= (tech_map[location] * 18)):
        shop_equipment.append("docking unit")
        shop_equipment_prices.append(10)
    # ha a technikaifejlettség 15, akkor 30% eséllyel lesz tolmácsgép, ha 14 akkor 28%, ha 13 akkor 26% stb...
    if(random.randrange(1, 101) <= (tech_map[location] * 2)):
        shop_equipment.append("translation device")
        shop_equipment_prices.append(5)
    # ha a technikaifejlettség 15, akkor 30% eséllyel lesz konténer, ha 14 akkor 28%, ha 13 akkor 26% stb...
    if(random.randrange(1, 101) <= (tech_map[location] * 2)):
        shop_equipment.append("container")
        shop_equipment_prices.append(3)

    # 4 féle harc felszerelés van ami majd segít minket a harcban
    # 10%-al növeli az esélyét hogy megnyerjük a harcot
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("armor")
        shop_equipment_prices.append(random.randrange(15, 26))
    # 20%-al növeli az esélyét hogy megnyerjük a harcot
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("plasma cannon")
        shop_equipment_prices.append(random.randrange(30, 51))
    # 30%-al növeli az esélyét hogy megnyerjük a harcot
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("advanced missile launcher")
        shop_equipment_prices.append(random.randrange(45, 76))
    # 40%-al növeli az esélyét hogy megnyerjük a harcot
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("rechargable alien energy shield")
        shop_equipment_prices.append(random.randrange(60, 101))

    # 3 féle üzemanyagtartály van, ezeknek az az előnye, hogy nagyobb távolságot tudunk utazni, és jobban elkerülhetjük hogy egy bolygón ragadjunk
    # a "max_fuel"-t 3-ra állítja
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("small tank")
        shop_equipment_prices.append(10)
    # a "max_fuel"-t 4-re állítja
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("medium tank")
        shop_equipment_prices.append(15)
    # a "max_fuel"-t 5-re állítja
    if(random.randrange(1, 101) <= tech_map[location]):
        shop_equipment.append("large tank")
        shop_equipment_prices.append(25)   

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
        max:int = tech_map_avarage() + 9
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

def utilize_equipment():
    ...

# visszatér egy olyan térképpel ami mutatja hol vagyunk jelenleg, és technikaifejlettség alapján színkódol
def gps():
    #   0    1-3  4-6    7-9  10-12 13-15
    # black  red yellow white green cyan
    string:str = ""
    temp:str
    for i in range(len(map)):
        temp = map[i]
        if(tech_map[i] == 0): temp = f"\033[30m{temp}\033[0m"
        if(1 <= tech_map[i] and tech_map[i] <= 3): temp = f"\033[31m{temp}\033[0m"
        if(4 <= tech_map[i] and tech_map[i] <= 6): temp = f"\033[33m{temp}\033[0m"
        if(7 <= tech_map[i] and tech_map[i] <= 9): temp = f"\033[37m{temp}\033[0m"
        if(10 <= tech_map[i] and tech_map[i] <= 12): temp = f"\033[32m{temp}\033[0m"
        if(13 <= tech_map[i] and tech_map[i] <= 15): temp = f"\033[36m{temp}\033[0m"
        if(location == i): temp = f"({temp})"
        string += temp + " "
    return string

def available_telescopes():
    string:str = ""
    temp:str
    for i in range(len(map)):
        temp = map[i]
        if(telescope_map[i] == True):
            if(1 <= tech_map[i] and tech_map[i] <= 3): temp = f"\033[31m{temp}\033[0m"
            if(4 <= tech_map[i] and tech_map[i] <= 6): temp = f"\033[33m{temp}\033[0m"
            if(7 <= tech_map[i] and tech_map[i] <= 9): temp = f"\033[37m{temp}\033[0m"
            if(10 <= tech_map[i] and tech_map[i] <= 12): temp = f"\033[32m{temp}\033[0m"
            if(13 <= tech_map[i] and tech_map[i] <= 15): temp = f"\033[36m{temp}\033[0m"
            string += temp + " "
    return string

    '''    
    string:str = ""
    for i in range(len(telescope_map)):
        if(telescope_map[i] == True):
            string += f"{map[i]}, "
    return string[:-2]
    '''
def sell_goods():
    global goods_have_just_been_sold
    global goods
    global credits
    global goods_sold
    global credits_gained
    if(0 < goods):
        goods_sold = goods
        credits_gained = goods_sold * round(random.randrange(9, 16) * 0.1, 3)
        goods -= goods_sold
        credits += round(credits_gained, 3)
        goods_have_just_been_sold = True

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
    max_fuel = a

def set_credits():
    global credits
    a:float = float(input("set credits to: "))
    credits = round(a, 3)

# kiszámolja a technikaifejlettség átlagát, a 0 vagyis űr mezőket nem beleértve, és felfelé kerekíti
def tech_map_avarage():
    filtered_list:int=[]
    for i in range(len(tech_map)):
        if(tech_map[i] != 0): filtered_list.append(tech_map[i])
    return math.ceil(sum(filtered_list) / len(filtered_list))

# operációs rendszerhez alkalmazkodó képernyő tisztító (teljesen a ChatGPT generálta)
def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')