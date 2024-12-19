import met

infinitefuelmode:bool=True
if(infinitefuelmode == True): met.fuel = 1000

met.status()
for i in range(100):   
    inputtext:str=str(input("input: "))
    if(inputtext == "travel"): met.travel()
    elif(inputtext == "buy"): met.buy()
    else: print("bad input")

    # print(f"i: {i}")
