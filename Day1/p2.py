import math
# get input data and convert it to integers
data = open('input2.txt', 'r').read().split('\n')
data = list(filter(None, data))
Mass = list(map(int, data))
# call data list Mass
Fuel  = lambda x : math.floor(x/3) - 2
SumFuel = lambda f: 0 if Fuel(f)<0 else Fuel(f) + SumFuel(Fuel(f))
# Test Example Case
print(SumFuel(14))
print(SumFuel(1969))
print(SumFuel(100756))
# Map Iterative Sum Over List
FuelList = list(map(SumFuel, Mass))
TotalFuel = sum(FuelList)
print(TotalFuel)