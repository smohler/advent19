import INTCODE
from importlib import reload
print('Testing INPUT/OUTPUT')
C = INTCODE.computer()
p = [3,0,4,0,99] #outputs what ever it get as input
i = 12345
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==i, i, o))

print('Testing Equal/LessThan(POSITIONAL)')
p = [3,9,8,9,10,9,4,9,99,-1,8] #tests is input is EQUAL to 8.
i = 1; true = 0
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))
i = 8; true = 1
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

p = [3,9,7,9,10,9,4,9,99,-1,8] #test is if it is LESS than 8
i = 1; true = 1
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

i = 9; true = 0
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

print('Testing Equal/LessThan(IMMEDIATE)')
p = [3,3,1108,-1,8,3,4,3,99]
i = 1; true = 0
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))
i = 8; true = 1
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

p = [3,3,1107,-1,8,3,4,3,99] 
i = 1; true = 1
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

i = 9; true = 0
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))


print('Testing Jump (POSITIONAL)')
p = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
i = 1
true = 1 #input is nonzero
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

print('Testing Jumps (IMMEDIATE)')
p = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
i = 0
true = 0 #input zero
C.LoadProgram(p,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o==true, true, o))

print('Testing Comparison Suite')
p = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
i1 = 7; true1 = 999; C.LoadProgram(p,i1); o1 = C.RunProgram()
i2 = 8; true2 = 1000;C.LoadProgram(p,i2); o2 = C.RunProgram()
i3 = 9; true3 = 1001;C.LoadProgram(p,i3); o3 = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(o1==true1, true1, o1))
print('Test is {}. Asserted {}: Output {}'.format(o2==true2, true2, o2))
print('Test is {}. Asserted {}: Output {}'.format(o3==true3, true3, o3))

print('Testing Relative Base Functions')
example1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
example2 = [1102,34915192,34915192,7,4,7,99,0]
example3 = [104,1125899906842624,99]
example4 = [109, -1, 4, 1, 99] #output -1
example5 = [109, -1, 104, 1, 99] #outputs 1
example6 = [109, 1, 9, 2, 204, -6, 99] #outputs 204
example7 = [109, 1, 109, 9, 204, -6, 99] #outputs 204
example8 = [109, 1, 209, -1, 204, -106, 99] #outputs 204
example9 = [109, 1, 3, 3, 204, 2, 99] #outputs the input
example10= [109, 1, 203, 2, 204, 2, 99] #outputs the input

# Example 1 Test
C.LoadProgram(example1)
C.Print = False
O = []
halt = False
while halt == False:
    o = C.RunProgram()
    O.append(o)
    halt = C.HALT
O.pop()
print('Test is {}. Asserted {}: Output {}'.format(str(O == example1), example1, O))


# Example 3 Test
i = 1125899906842624
C.LoadProgram(example3,i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))


# Example 4 Test
i = -1
C.LoadProgram(example4)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 5 Test
i = 1
C.LoadProgram(example5)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 6 Test
i = 204
C.LoadProgram(example6)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 7 Test
i = 204
C.LoadProgram(example7)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 8 Test
i = 204
C.LoadProgram(example8)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 9 Test
i = 1201
C.LoadProgram(example9, i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Example 10 Test
i = 8
C.LoadProgram(example10, i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == i), i, o))

# Day 9 Verify
i = 1
a = 4080871669
data = open('day9.txt').read().split(',')
program = list(map(int, data))
C.LoadProgram(program, i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == a), a, o))

# Day 5 Verify
i = 1
a = 6745903
data = open('day5.txt').read().split(',')
program = list(map(int, data))
C.LoadProgram(program, i)
halt = False
O = []
while halt == False:
    o = C.RunProgram()
    O.append(o)
    halt = C.HALT
o = O[-2]
print('Test is {}. Asserted {}: Output {}'.format(str(o == a), a, o))

# Day 5 Verify
i = 5
a = 9168267
data = open('day5.txt').read().split(',')
program = list(map(int, data))
C.LoadProgram(program, i)
o = C.RunProgram()
print('Test is {}. Asserted {}: Output {}'.format(str(o == a), a, o))




