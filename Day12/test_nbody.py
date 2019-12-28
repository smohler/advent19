import nbody as nb
from importlib import reload

#test 1
a = 179
Io = nb.planet(-1, 0, 2)
Europa = nb.planet(2, -10, -7)
Gaynmede = nb.planet(4, -8, 8)
Callisto = nb.planet(3, 5, -1)
E = nb.simulate(10,Io,Europa,Gaynmede,Callisto)
print('The test is {}: Asserted: {}  Output: {}'.format(E==a, a, E))


#test 2
A= 1940
Io = nb.planet(-8, -10, 0)
Europa = nb.planet(5, 5, 10)
Gaynmede = nb.planet(2, -7, 3)
Callisto = nb.planet(9, -8, -3)
E = nb.simulate(100,Io,Europa,Gaynmede,Callisto)
print('The test is {}: Asserted: {}  Output: {}'.format(E==A, A, E))


#part1
Io = nb.planet(-16,15,-9)
Europa = nb.planet(-14,5,4)
Gaynmede = nb.planet(2, 0, 6)
Callisto = nb.planet(-3, 18, 9)
E = nb.simulate(1000,Io,Europa,Gaynmede,Callisto)
print('The answer is {}:'.format(E))


#test3
reload(nb)
a = 2772
Io = nb.planet(-1, 0, 2)
Europa = nb.planet(2, -10, -7)
Gaynmede = nb.planet(4, -8, 8)
Callisto = nb.planet(3, 5, -1)
Q = nb.efficient(Io,Europa,Gaynmede,Callisto)
Q = nb.LCM(Q[0],Q[1],Q[2])
print('The test is {}: Asserted: {}  Output: {}'.format(Q==a, a, Q))

#test 2
a = 4686774924
Io = nb.planet(-8, -10, 0)
Europa = nb.planet(5, 5, 10)
Gaynmede = nb.planet(2, -7, 3)
Callisto = nb.planet(9, -8, -3)
Q = nb.efficient(Io,Europa,Gaynmede,Callisto)
Q = nb.LCM(Q[0],Q[1],Q[2])
print('The test is {}: Asserted: {}  Output: {}'.format(Q==a, a, Q))

#part2
Io = nb.planet(-16,15,-9)
Europa = nb.planet(-14,5,4)
Gaynmede = nb.planet(2, 0, 6)
Callisto = nb.planet(-3, 18, 9)
E = nb.efficient(Io,Europa,Gaynmede,Callisto)
E = nb.LCM(E[0],E[1],E[2])
print('The answer is {}:'.format(E))
