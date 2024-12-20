# A játékot ajánlott cmd-ben futtatni!

# ötletek
# a gps-en a bolygók a tech_level-hez megfelelő színűek, minnél magassabb annál zöldebb például
# felfedezni kreditért lehet, csak bizonyos bolygókon

import met

met.cheats=True

met.status()
for i in range(100):   
    inputtext:str=str(input("input: "))
    if(inputtext == "travel"):
        met.travel()
        met.status()
    elif(inputtext == "buy"):
        met.buy()
        met.status()
    elif(inputtext == "telescope"):
        met.telescope()
        met.status()

    elif(met.cheats and inputtext == "/planet"):
        met.add_new_planet()
        met.status()
    elif(met.cheats and inputtext == "/explosion chance"):
        met.set_chance_of_explosion()
        met.status()
    elif(met.cheats and inputtext == "/fuel"):
        met.set_fuel()
        met.status()
    else:
        print("\n---invalid input---\n")
        print("Press Enter to continue.")
        input()
        met.status()

    
