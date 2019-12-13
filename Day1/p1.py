import math
# get input data and convert it to integers
data = open('input.txt', 'r').read().split('\n')
data = list(filter(None, data))
Mass = list(map(int, data))
# call data list Mass
Fuel  = lambda x : math.floor(x/3) - 2
# Iterate over Mass List
FuelList = list(map(Fuel, Mass))
TotalFuel = sum(FuelList)
print(TotalFuel)