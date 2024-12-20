# A játékot ajánlott cmd-ben futtatni!

# ötletek
# a gps-en a bolygók a tech_level-hez megfelelő színűek, minnél magassabb annál zöldebb például
# felfedezni kreditért lehet, csak bizonyos bolygókon

import met

infinite_fuel_mode:bool=False
if(infinite_fuel_mode == True): met.fuel = 1000

met.status()
for i in range(100):   
    inputtext:str=str(input("input: "))
    if(inputtext == "travel"):
        met.travel()
        met.status()
    elif(inputtext == "buy"):
        met.buy()
        met.status()
    elif(inputtext == "explore"):
        met.explore()
        met.status()
    # ez egy csalókód
    elif(inputtext == "add"):
        met.add_new_planet()
        met.status()
    else:
        print("\nInvalid input, possible options are:\ntravel, buy, explore\n")
        print("Press Enter to continue.")
        input()
        met.status()

    
