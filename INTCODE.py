# The INTCODE Program that Create the Virtual Computer
# Condsider revising it into an object with methods that can be easily added
class INTCODE:
    """
    Advent of Code 2019 INTCODE Computer Object
    """
    #Computer Variables
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 99:'HALT'}
    modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE'}

    @staticmethod
    def add_optcode(key, value):
        value = value.upper()
        key = int(key)
        INTCODE.optcodes.update({key:value})

    @staticmethod    
    def add_mode(key, value):
        value = value.upper()
        key = int(key)
        INTCODE.modedefs.update({key:value})

    @staticmethod
    def reset_defs():
        INTCODE.optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 99:'HALT'}
        INTCODE.modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE'}

    def __init__(self, computer_name = 'IntcodeA'):
        self.Name = computer_name


    # def object_method(self, **keywordargs):


#current working intcode computer...
def intcode(PRGM, PRGMINPUT, STEP = 0, inputSTEP = 0, log = False):
    inputSTEP = 0
    prgmSize = len(PRGM)
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 99:'HALT'}
    modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE'}
    if log: message = 'READ:{0:8}OPTCODE:{1:8}PARAMETER MODES:({2:10}, {3:10})\tSTEP:{4:3}'
   
    while STEP < prgmSize:
        READ = str(PRGM[STEP])
        optint = int(READ[-2:])
        OPTCODE = optcodes[optint]

        #determine the PARAMETER MODES
        if len(READ) <= 2:
            MODE2 = 'POSITIONAL'
            MODE1 = 'POSITIONAL'
        if len(READ) == 3:
            MODE2 = 'POSITIONAL'
            MODE1 = 'IMMEDIATE'
        if len(READ) == 4:
            MODE2 = modedefs[int(READ[0])]
            MODE1 = modedefs[int(READ[1])]

        if log: print(message.format(READ, OPTCODE, MODE1, MODE2, STEP))  

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
            STEP = STEP + 4
            
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
            STEP = STEP + 4

        if OPTCODE == 'INPUT':
            if log:
                #VAL = int(input('User Input: '))
                VAL = PRGMINPUT[inputSTEP] 
                print('INPUT TO COMPUTER: {}'.format(PRGMINPUT))
                print('INPUT TO PROGRAM :{}'.format(VAL))
            else:
                VAL = PRGMINPUT[inputSTEP]  
            STOR = PRGM[STEP+1]
            PRGM[STOR] = VAL
            inputSTEP = inputSTEP + 1
            STEP = STEP + 2

        if OPTCODE == 'OUTPUT':
            if MODE1 == 'POSITIONAL':
                VAL = PRGM[PRGM[STEP+1]]
            else:
                VAL = PRGM[STEP+1]
            outputmessage = 'PROGRAM OUTPUT: {}'
            if log: print(outputmessage.format(VAL))
            STEP = STEP + 2
            return PRGM, VAL, STEP

        if OPTCODE == 'JMPTRU':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 != 0:
                STEP = VAL2
            else:
                STEP = STEP + 3 
 
        if OPTCODE == 'JMPFLSE':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 == 0:
                STEP = VAL2
            else:
                STEP = STEP + 3 

        if OPTCODE == 'LESSTHN':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            STEP = STEP + 4

            if VAL1 < VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0     

        if OPTCODE == 'EQUALS':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            STEP = STEP + 4

            if VAL1 == VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0
               
        if OPTCODE == 'HALT':
            if log: print('HALT')
            return PRGM  
