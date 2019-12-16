class computer:
    """
    Advent of Code 2019 INTCODE Computer Object
    """
    #Computer (Class) Variables
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 9:'RELBASE', 99:'HALT'}
    modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE', 2:'RELMODE'}

    def __init__(self, computer_name = 'IntcodeA', relative_base = 0):
        self.Name = computer_name
        self.relbase = relative_base

    def assignModes(self, program, step):
        #read the first instruction to set the optcode and parameter mode
        #put zero padding in instructions as not provied means 0
        READ = str(program[step]).rjust(4,'0')
        OPTCODE = computer.optcodes[int(READ[-2:])]
        MODE1 = computer.modedefs[int(READ[1])]
        MODE2 = computer.modedefs[int(READ[0])]
        return OPTCODE, MODE1, MODE2

    def assignValues(self, program, step, MODE1, MODE2):
        if MODE1 == 'POSITIONAL': 
            VAL1 = program[program[step+1]]  
        elif MODE1 == 'IMMEDIATE': 
            VAL1 = program[step+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.relbase
            VAL1 = program[RELBASE + 1]

        if MODE2 == 'POSITIONAL': 
            VAL2 = program[program[step+1]]  
        elif MODE2 == 'IMMEDIATE': 
            VAL2 = program[step+1]
        else: #MODE2 == 'RELBASE'
            RELBASE = self.relbase
            VAL2 = program[RELBASE + 1]

        return VAL1, VAL2

    def assignMemory(self, program):
        programSize = len(program)
        self.inputIndex = programSize
        self.outputIndex = -1
        memory = [0 for i in range(2*programSize)]
        program = program + memory
        return program

    def assignInput(self,program, INPUT):
        program[self.inputIndex:self.inputIndex + len(INPUT)] = INPUT
        return program

    def getInput(self, program):
        INPUT = program[self.inputIndex]
        self.inputIndex = self.inputIndex + 1
        return INPUT

    def assignOutput(self, program, OUTPUT):
        program[self.outputIndex] = OUTPUT
        self.outputIndex = self.outputIndex - 1
        return program

    def assignValue(self, program, step, MODE1):
        if MODE1 == 'POSITIONAL': 
            VAL = program[program[step+1]]  
        elif MODE1 == 'IMMEDIATE': 
            VAL = program[step+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.relbase
            VAL = program[RELBASE + 1]
        return VAL
  
    def add(self, program, step, mode1, mode2):
        VAL1, VAL2 = self.assignValues(program, step, mode1, mode2)
        STOR = program[step+3]
        program[STOR] = VAL1+VAL2
        step = step + 4
        return program, step
    
    def mult(self, program, step, mode1, mode2):
        VAL1, VAL2 = self.assignValues(program, step, mode1, mode2)
        STOR = program[step+3]
        program[STOR] = VAL1*VAL2
        step = step + 4
        return program, step

    def Input(self, program, step, INPUT):
        STOR = program[step + 1]
        program[STOR] = INPUT
        step = step + 2
        return program, step

    def Output(self, program, STEP, MODE1):
        VAL = self.assignValue(program, STEP, MODE1)
        STEP = STEP + 2
        return program, VAL, STEP

    def JumpTrue(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)

        if VAL1 != 0:
            STEP = VAL2
        else:
            STEP = STEP + 3 
        return program, STEP

    def JumpFalse(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        if VAL1 == 0:
            STEP = VAL2
        else:
            STEP = STEP + 3 
        return program, STEP

    def LessThan(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        STOR = program[STEP+3]
        if VAL1 < VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0 
        STEP = STEP + 4
        return program, STEP  

    def Equals(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        STOR = program[STEP+3]
        if VAL1 == VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0   
        STEP = STEP + 4
        return program, STEP

    def AdjustBase(self, program, STEP, MODE1):
        VAL = self.assignValue(program, STEP, MODE1)
        self.relbase = self.relbase + VAL
        STEP = STEP + 2
        return program, STEP

    def Halt(self, program, STEP):
        return program, STEP
        
    def RunProgram(self, program):
        step = 0
        programSize = len(program)
        while step < programSize:
            OPTCODE, mode1, mode2 = self.assignModes(program, step)
            # Check OPTCODES and Run Functions accordingly 
            if OPTCODE == 'ADD':#1
                program, step = self.add(program, step, mode1, mode2)
            if OPTCODE == 'MULT':#2
                program, step = self.mult(program, step, mode1, mode2)
            if OPTCODE == 'INPUT':#3
                INPUT = self.getInput(program)
                program, step = self.Input(program, step, INPUT)
            if OPTCODE == 'OUTPUT':#4
                program, step, output = self.Output(program, step, mode1)
                program = self.assignOutput(program, output)
            if OPTCODE == 'JMPTRU':#5
                program, step = self.JumpTrue(program, step, mode1, mode2)
            if OPTCODE == 'JMPFLSE':#6
                program, step = self.JumpFalse(program, step, mode1, mode2)
            if OPTCODE == 'LESSTHN':#7
                program, step = self.LessThan(program, step, mode1, mode2)
            if OPTCODE == 'EQUALS':#8
                program, step = self.Equals(program, step, mode1, mode2)
            if OPTCODE == 'RELBASE':#9
                program, step = self.AdjustBase(program, step, mode1)
            if OPTCODE == 'HALT':#99
                program, step = self.Halt(program, step)
        #return the output of the program