# A játékot ajánlott cmd-ben futtatni!

# ötletek
# a gps-en a bolygók a tech_level-hez megfelelő színűek, minnél magassabb annál zöldebb például
# felfedezni kreditért lehet, csak bizonyos bolygókon
# days left
# the end
# 4 types of weapons
# S tartály: át tudunk utazni 2 űrt, M tartály: át tudunk utazni 3 űrt, L tartály: a bolygókon ragadás esélyét csökkenti és kényelem

import met

met.status()
while(True):   
    inputtext:str=str(input("input: "))
    if(inputtext == "travel"):
        met.travel()
    elif(inputtext == "buy"):
        met.buy()
    elif(inputtext == "telescope"):
        met.telescope()

    elif(inputtext =="/cheats"):
        met.cheats = not met.cheats
    elif(met.cheats and inputtext == "/fuel"):
        met.set_fuel()
    elif(met.cheats and inputtext == "/credits"):
        met.set_credits()
    elif(met.cheats and inputtext == "/planet"):
        met.add_new_planet()
    elif(met.cheats and inputtext == "/explosion chance"):
        met.set_chance_of_explosion()

    else:
        print("\n---invalid input---\n")
        print("Press Enter to continue.")
        input()
    
    met.status()

    
