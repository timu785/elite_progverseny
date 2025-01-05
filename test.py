import met
import random
import math
import time
import string

met.clear_screen()
sample_size:int = 10
for i in range(sample_size):
    print(f"{i+1:3}    ", end="")
    word:str = ""
    for j in range(random.randrange(1,11)):
        word += random.choice(string.ascii_letters)
    print(word)

    time.sleep(1)




#input()

'''
a:float = 5.5
b:int = 7
c:int = 9
list = [a, b, c]
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(list)
print(int(min(list)))
'''



'''
while True:
    user_input = input("Please enter an integer: ")
    try:
        user_number = int(user_input)
        print(f"Thank you! You entered the integer: {user_number}")
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("That is not a valid integer. Please try again.")
'''

'''
inputtext:str = str(input("adjon megy egy szamot: "))
a:int = int(inputtext)
a += 1
print(a)
'''



'''
list:str = ["alma", "korte", "barack", "barack"]
print(len(list))
print(15 * list.count("barack"))
print(15 * list.count("gyumolcs leves"))
'''


'''
shop_items:str = ["alma", "korte", "barack"]
shop_prices:int = [10, 20, 30]
print(shop_items)
print(shop_prices)

to_buy:str=str(input("mit akarsz venni?: "))

print(shop_items.index(to_buy))
# azért kell először az árat áltávolítani, hogy név szerint tudjunk hivatkozni a list indexre utoljára
del shop_prices[shop_items.index(to_buy)]
del shop_items[shop_items.index(to_buy)]

print(shop_items)
print(shop_prices)
'''

'''
#  0.9  és  1.5
print(round(random.randrange(9, 16) * 0.1, 3))
print()
print("(\033[31mThis is red text\033[0m" + " asd")
print()
temp:str = "alma"
print(f"\033[31m{temp}\033[0m")
'''

'''
int1:int = 10
int2:int = 2
float1:float = 3.3

print(int1 > float1)
print(int1 - float1)
print(float1)
print(float1 - int2)
'''

'''
# ha egy lista nem üres akkor igaz-ra értékelődik ki
list1:str = []
list2:str = ["alma", "korte"]

if(list1): print("ures lista")
if(list2): print("nem ures lista")
'''

'''
# árú generálása 1 és 20 között a technikaifejlettségtől függően
for i in range(15):
    x:float = 15 / 20
    tech_level = i + 1
    middle:int = math.ceil(tech_level / x)
    min:int = middle - 4
    max:int = middle + 4
    temp:int = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    #if(20 < temp): temp = 20
    print(f"tech level {tech_level}:   {middle}   {temp}")
'''

'''
# üzemanyag generálása 1 és 5 között a technikaifejlettségtől függően
for i in range(15):
    x:float = 15 / 5
    tech_level = i + 1
    middle:int = math.ceil(tech_level / x)
    min:int = middle - 1
    max:int = middle + 4
    temp = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    if(5 < temp): temp = 5
    print(f"tech level {tech_level}:   {middle}   {temp}")
'''

'''
random_number:int = random.randrange(1, 101)
print(random_number)
limit:int = 12 * 3.34
print(limit)
print(random_number <= limit)
'''

'''
print(met.tech_levels_avarage([2, 4, 10, 0, 6, 1, 0, 4, 0, 6, 0, 14]))

# 2 dimenziós string lista
# Example of a 2x2 string matrix
string_matrix:str = [["hello", "world"], ["python", "rocks"]]
print(string_matrix)
print(string_matrix[1][0])
string_matrix.append(["asd", "asd2"])
print(string_matrix)
string_matrix[0].append("hello2")
print(string_matrix)
'''


