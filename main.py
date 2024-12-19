# A játékot ajánlott cmd-ben futtatni!

import met

infinite_fuel_mode:bool=True
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
    else: print("bad input, possible inputs are: travel, buy")

    # print(f"i: {i}")
