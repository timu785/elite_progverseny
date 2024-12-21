import met
import random
import math

int1:int = 10
int2:int = 2
float1:float = 3.3

print(int1 > float1)
print(int1 - float1)
print(float1)
print(float1 - int2)



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


