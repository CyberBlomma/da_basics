import math

for item in "Din Mor ":
    if item != " ":
        print(item)

print("")


for item in range(5, 10):
    print(item)
 
print("")
    
    
prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

print("")


for x in range(3):
    for y in range(3):
        print(f"{x}, {y}")
        
print("")


numbers = [5, 8, 3, 3, 3, 3, 1, 7, 3, 99, 1538, -382541, 38, 69, 11]

wide_boi = 0
for item in numbers:
    if item > wide_boi:
        wide_boi = item
        
print(wide_boi)
print("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]