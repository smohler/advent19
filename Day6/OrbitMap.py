""" --- Day 6: Universal Orbit Map ---
 You've landed at the Universal Orbit Map facility on Mercury.
 Because navigation in space often involves transferring between orbits,
 the orbit maps here are useful for finding efficient routes between, 
 for example, you and Santa. You download a map of the local orbits (your puzzle input).
 
 Except for the universal Center of Mass (COM), every object in space is in
 orbit around exactly one other object. An orbit looks roughly like this:
                   \
                    \
                    |
                    |
 AAA--> o            o <--BBB
                    |
                    |
                   /
                  /

"""
# Total Direct & Indirect Orbits = 42
example = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

# Puzzle Data
data = list(open('input.txt', 'r').read().strip().split('\n'))

# Determine Orbits
Orbits = data
DirectOrbits = len(Orbits)

#Make sure the COM is in the data
leftOrbits = [x.split(')')[0] for x in Orbits]
I = leftOrbits.index('COM')
print('The COM exists in the orbit map: {} \t Orbits[{}] = {}'.format('COM' in leftOrbits, I, Orbits[I]))


#Count Indirect Orbits
def IndirectOrbits(directOrbit, Orbits):
    rightOrbits = [x.split(')')[1] for x in Orbits]
    left = directOrbit.split(')')[0]
    if left == 'COM':
        return 0
    #now find this left orbit somewhere in the right orbit
    if left in rightOrbits:
        I = rightOrbits.index(left)
        left = Orbits[I]
        return 1 + IndirectOrbits(left, Orbits)

TotalIndirects = sum([IndirectOrbits(i, Orbits) for i in Orbits])
message = "Total Orbits = {}\tIndirect Orbits = {}\tDirect Orbits = {}"
print(message.format(TotalIndirects + DirectOrbits, TotalIndirects, DirectOrbits))