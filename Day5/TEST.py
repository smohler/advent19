#The Thermal Environment Supervision Terminal

# get input data and convert it to integers
data = open('input.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))


def Intcode(PRGM):

    k = 0
    prgmSize = len(PRGM)
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT', 99:'HALT'}
    modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE'}
    message = 'READ:{0:8}OPTCODE:{1:8}PARAMETER MODES:({2:10}, {3:10})\tSTEP:{4:3}'
    while k < prgmSize:
        STEP = k
        READ = str(PRGM[STEP])
        optint = int(READ[-2:])
        OPTCODE = optcodes[optint]
        #determine the PARAMETER MODES
        if len(READ) <=2:
            MODE2 = 'POSITIONAL'
            MODE1 = 'POSITIONAL'
        if len(READ) == 3: #mean 101 or 100 which imply modes
            MODE2 = 'POSITIONAL'
            MODE1 = 'IMMEDIATE'
        if len(READ) == 4:
            MODE2 = modedefs[int(READ[0])]
            MODE1 = modedefs[int(READ[1])]

        print(message.format(READ, OPTCODE, MODE1, MODE2, STEP))

        if OPTCODE == 'ADD': 
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]  
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]
            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1+VAL2
            inc = 4
            

        if OPTCODE == 'MULT':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1*VAL2
            inc = 4


        if OPTCODE == 'INPUT':
            VAL = int(input("Input: "))
            STOR = PRGM[STEP+1]
            PRGM[STOR] = VAL
            inc = 2

        if OPTCODE == 'OUTPUT':
            if MODE1 == 'POSITIONAL':
                VAL = PRGM[PRGM[STEP+1]]
            else:
                VAL = PRGM[STEP+1]
            outputmessage = 'PROGRAM OUTPUT: {}'
            print(outputmessage.format(VAL))
            inc = 2

        if OPTCODE == 'HALT':
            print('HALT')
            return PRGM     
        k = k+inc
Intcode(prgm)