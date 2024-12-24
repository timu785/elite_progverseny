# to do:
# the end
# rövidítések, a "" válasz lehetne egy alapvető igen, vagy alap funkció
# az int inputok kifagyasztják a programot szöveges inputtal
# kommentek tisztítása
# változók és metódukso tisztítása
# kód átnázáse és tiszítása

import met

met.status()
while(True):
    if(met.days_left < 0):
        met.clear_screen()
        print("\nGAME OVER: You ran out of time, a nearby star exploded.\n")
        print("Press Enter to exit...")
        input()
        exit()

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

    
