""" --- Day 6: Universal Orbit Map Transfers---

"""
from functools import lru_cache

# Total Direct & Indirect Orbits = 42
example = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

# Puzzle Data
data = list(open('input.txt', 'r').read().strip().split('\n'))

# Determine Orbits
Orbits = data


#Make sure the COM, YOU, and SAN are in the data
leftOrbits = [x.split(')')[0] for x in Orbits]
rightOrbits = [x.split(')')[1] for x in Orbits]
I = leftOrbits.index('COM')
you = rightOrbits.index('YOU')
santa = rightOrbits.index('SAN')
print('COM exists in the orbit map: {} \t Orbits[{}] = {}'.format('COM' in leftOrbits, I, Orbits[I]))
print('SAN exists in the orbit map: {} \t Orbits[{}] = {}'.format('SAN' in rightOrbits, santa, Orbits[santa]))
print('YOU exists in the orbit map: {} \t Orbits[{}] = {}'.format('YOU' in rightOrbits, you, Orbits[you]))


#Count Indirect Orbits Output Total Orbit Transfer Path

def IndirectOrbits(directOrbit, Orbits):
    
    rightOrbits = [x.split(')')[1] for x in Orbits]
    left = directOrbit.split(')')[0]

    if left == 'COM':
        return []

    #now find this left orbit somewhere in the right orbit
    if left in rightOrbits:
        I = rightOrbits.index(left)
        left = Orbits[I]
        return IndirectOrbits(left, Orbits) + [directOrbit]

SantaPath = set(IndirectOrbits(Orbits[santa], Orbits))
YouPath = set(IndirectOrbits(Orbits[you], Orbits))
 
#Orbital Transfers = (Unique Elements in YouPath - 1) +  (Unique Elements in SantaPath - 1)
OrbitalTransfers = (len(YouPath-SantaPath)- 1) + (len(SantaPath-YouPath) - 1)
print('YOU path length: {}'.format(len(YouPath)))
print('SANTA path length: {}'.format(len(SantaPath)))
print('Orbital Transfers to Intercept Santa: {}'.format(OrbitalTransfers))