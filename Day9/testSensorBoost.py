from INTCODE import computer
intcode = computer('Example', Print = False, clock_Mode = 'RUN')
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
intcode.LoadProgram(example1)
output = intcode.RunProgram()
print('Example 1 is ' + str(output == example1))

# Example 2 Test
intcode.LoadProgram(example2)
output = intcode.RunProgram()
print('Example 2 is ' + str(16 == len(str(output[0]))))


# Example 3 Test
intcode.LoadProgram(example3)
output = intcode.RunProgram()
print('Example 3 is ' + str(output == [1125899906842624]))

# Example 4 Test
intcode.LoadProgram(example4)
output = intcode.RunProgram()
print('Example4 is ' + str(output == [-1]))

# Example 5 Test
intcode.LoadProgram(example5)
output = intcode.RunProgram()
print('Example 5 is ' + str(output == [1]))

# Example 6 Test
intcode.LoadProgram(example6)
output = intcode.RunProgram()
print('Example 6 is ' + str(output == [204]))

# Example 7 Test
intcode.LoadProgram(example7)
output = intcode.RunProgram()
print('Example 7 is ' + str(output == [204]))

# Example 8 Test
intcode.LoadProgram(example8)
output = intcode.RunProgram()
print('Example 8 is ' + str(output == [204]))

# Example 9 Test
intcode.LoadProgram(example9, INPUT = [1201])
output = intcode.RunProgram()
print('Example 9 is ' +str(output == [1201]))

# Example 10 Test
intcode.LoadProgram(example10, INPUT = [100001])
output = intcode.RunProgram()
print('Example 10 is ' + str(output == [100001]))
