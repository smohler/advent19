# get input data and convert it to integers
data = open('input1.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))
prgm[1] = 12
prgm[2] = 2 
example = [1,9,10,3,2,3,11,0,99,30,40,50]
def Alarm(PRGM):
    k = 0
    prgmSize = len(PRGM)
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
            return PRGM
        k = k+1
print(Alarm(prgm))