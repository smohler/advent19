# get input data and convert it to integers
data = open('input1.txt', 'r').read().strip().split(',')
program = list(map(int, data))
goal = 19690720

def Intcode(program, noun, verb):
    PRGM = program
    k = 0
    prgmSize = len(PRGM)
    PRGM[1] = noun
    PRGM[2] = verb
    while k < prgmSize/4:
        OPTCODE = PRGM[4*k]
        STOR = PRGM[4*k+3]
        if OPTCODE == 1: 
            VAL1 = PRGM[PRGM[4*k+1]]
            VAL2 = PRGM[PRGM[4*k+2]]
            PRGM[STOR] = VAL1+VAL2
            #print(str(OPTCODE) + ' : ADD : ' + str(VAL1) + '+' + str(VAL2) + ' : STORE :' + str(STOR))
        if OPTCODE == 2:
            VAL1 = PRGM[PRGM[4*k+1]]
            VAL2 = PRGM[PRGM[4*k+2]]
            PRGM[STOR] = VAL1*VAL2
            #print(str(OPTCODE) + ' : MULT : ' + str(VAL1) + '*' + str(VAL2) + ' : STORE :' + str(STOR))
        if OPTCODE == 99:
            #print(str(OPTCODE) + ' : HALT')
            return PRGM[0]
        k = k+1


# Determine noun & verb that give desired goal by brute force
i = 0
while i < 100:
    for j in range(100):
        output = Intcode(program, i, j)
        if output == goal:
            print('Goal Reached')
            message = "noun = {} : verb = {} : output = {}"
            answer = "100*{} + {} = {}"
            print(message.format(i,j,output))
            print(answer.format(i, j, 100*i + j))
        program = list(map(int, data))
    i += 1
