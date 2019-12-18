from INTCODE import computer
intcode = computer('Example', print_Mode = True, clock_Mode = 'RUN')
example1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
example2 = [1102,34915192,34915192,7,4,7,99,0]
example3 = [104,1125899906842624,99]

# Example 1 Test
intcode.LoadProgram(example1)
output = intcode.RunProgram()