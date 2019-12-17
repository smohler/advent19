from INTCODE import computer
Intcode = computer('Examples')
example1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
example2 = [1102,34915192,34915192,7,4,7,99,0]
example3 = [104,1125899906842624,99]

# Example 1 Test
Intcode.assignMemory(example1)
output = Intcode.RunProgram(example1)
if output == example1:
    print('Example 1 Matches')
else:
    print('Example 1 Test Failed')

# Example 2 Test


# Example 3 Test