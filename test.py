import met
import random
import math


# üzemanyag generálása 1 és 5 között a technikaifejlettségtől függően
for i in range(15):
    min:int = math.ceil((i+1)/3) - 1
    max:int = math.ceil((i+1)/3) + 4
    temp = random.randrange(min, max + 1)
    if(temp < 1): temp = 1
    if(5 < temp): temp = 5
    print(f"{i+1}:   {math.ceil((i+1)/3)}   {temp}")



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


