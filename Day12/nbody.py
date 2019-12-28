from collections import defaultdict
import timeit 
class planet:
    def __init__(self,x,y,z):
        self.x = x; self.vx = 0
        self.y = y; self.vy = 0
        self.z = z; self.vz = 0
        self.pot = abs(x) + abs(y) + abs(z)
        self.kin = 0
    
    def __add__(self, other):
        add = lambda p, q: (p.x + q.x, p.y + q.y, p.z + q.z)
        return add(self, other)

    def __len__(self):
        #consider the length of the vetor as it's energy
        return self.energy()

    def __str__(self):
        return "Position: {}   Velocity: {}".format(self.position(), self.velocity())

    def phase(self):
        #unique scalar identifer for planet state
        return self.position() + self.velocity()

    def position(self):
        return (self.x, self.y, self.z)

    def velocity(self):
        return (self.vx,self.vy,self.vz)

    def gravity(self, other):
        force = lambda x, y: 1 if x<y else -1 if x>y else 0 
        self.vx = self.vx + force(self.x,other.x)
        self.vy = self.vy + force(self.y,other.y)
        self.vz = self.vz + force(self.z,other.z)
    
    def orbit(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.z = self.z + self.vz

    def energy(self):
        self.pot = abs(self.x) + abs(self.y) + abs(self.z)
        self.kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return self.pot*self.kin

def step(P0, P1, P2, P3):
    #apply gravitational force
    P0.gravity(P1); P0.gravity(P2); P0.gravity(P3)
    P1.gravity(P0); P1.gravity(P2); P1.gravity(P3)
    P2.gravity(P0); P2.gravity(P1); P2.gravity(P3)
    P3.gravity(P0); P3.gravity(P1); P3.gravity(P2)
    #update positions
    P0.orbit()
    P1.orbit()
    P2.orbit()
    P3.orbit()

def TotalEnergy(P0, P1, P2, P3):
    return len(P0) + len(P1) + len(P2) + len(P3)

def TotalPhase(P0, P1, P2, P3):
    u = P0.phase()
    v = P1.phase()
    w = P2.phase()
    m = P3.phase()
    return u + v + w + m


def simulate(t,P0,P1,P2,P3):
    k = 0
    phase = defaultdict(list)
    while k<t:
        key = (P0.position(),P1.position(),P2.position(),P3.position(),\
            P0.velocity(),P1.velocity(),P2.velocity(),P3.velocity())
        if not phase[key]:
            phase[key] = k
            k +=1
        else:
            print('Orbit Found')
            return k-1
        step(P0,P1,P2,P3)   
    p = [P0, P1, P2, P3]
    E = sum(map(len, p))
    return E

def efficient(P0, P1, P2, P3):
    x0 = P0.position()[0],P1.position()[0],P2.position()[0],P3.position()[0],\
         P0.velocity()[0],P1.velocity()[0],P2.velocity()[0],P3.velocity()[0]

    y0 = P0.position()[1],P1.position()[1],P2.position()[1],P3.position()[1],\
         P0.velocity()[1],P1.velocity()[1],P2.velocity()[1],P3.velocity()[1]

    z0 = P0.position()[2],P1.position()[2],P2.position()[2],P3.position()[2],\
         P0.velocity()[2],P1.velocity()[2],P2.velocity()[2],P3.velocity()[2]

    c0 = c1= c2 = False
    k = 0
    while True:
        k+=1
        step(P0, P1, P2, P3)
        x = P0.position()[0],P1.position()[0],P2.position()[0],P3.position()[0],\
         P0.velocity()[0],P1.velocity()[0],P2.velocity()[0],P3.velocity()[0]

        y = P0.position()[1],P1.position()[1],P2.position()[1],P3.position()[1],\
         P0.velocity()[1],P1.velocity()[1],P2.velocity()[1],P3.velocity()[1]

        z = P0.position()[2],P1.position()[2],P2.position()[2],P3.position()[2],\
         P0.velocity()[2],P1.velocity()[2],P2.velocity()[2],P3.velocity()[2]

        if x0 == x and not c0:
            print('x Orbit Found')
            c0 = True
            i0 = k
        if y == y0 and not c1:
            print('y Orbit Found')
            c1 = True
            i1 = k
        if z == z0 and not c2:
            print('z Orbit Found')
            c2 = True
            i2 = k
        if k%1000000 == 0: print("Iterations: {}".format(k))
        if c0 and c1 and c2:print('All Cycles Found in {} steps'.format(k)); return [i0, i1, i2]


def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def LCM(a,b,c):
    x = lcm(a,b)
    return lcm(x,c)