import met

infinitefuelmode:bool=False

met.status()
for i in range(100):

    if(infinitefuelmode == True):
        met.fuel = 1000
    
    inputtext:str=str(input("input: "))
    if(inputtext == "travel"): 
        destination:str = str(input("where do you want to travel: "))
        print("")
        location=met.travel(destination)
    else: print("bad input")

    # print(f"i: {i}")
