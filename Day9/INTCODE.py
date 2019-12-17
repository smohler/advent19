class computer:
    """
    Advent of Code 2019 INTCODE Computer Object
    """
    #Computer (Class) Variables
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 9:'RELBASE', 99:'HALT'}
    modedefs = {0: 'P', 1: 'I', 2:'R'}
    clockMode = {'RUN':False, 'STEP':True}

    def __init__(self, computer_name = 'IntcodeA', relative_base = 0, clock_Mode = 'RUN', print_Mode = True):
        self.Name = computer_name
        self.relbase = relative_base
        self.clock = computer.clockMode[clock_Mode.upper()]
        self.Print = print_Mode

        # state of computer
        self.INSTRUCTION = '0000'
        self.OPTCODE = 0
        self.MODE1 = 'N/A'
        self.MODE2 = 'N/A'
        self.VAL1 = 0
        self.VAL2 = 0
        self.STOR = 0
        self.STEP = 0
    # Sub Routines for Computer Methods
    def assignModes(self, program, step):
        #read the first instruction to set the optcode and parameter mode
        #put zero padding in instructions as not provied means 0
        READ = str(program[step]).rjust(4,'0')
        OPTCODE = computer.optcodes[int(READ[-2:])]
        MODE1 = computer.modedefs[int(READ[1])]
        MODE2 = computer.modedefs[int(READ[0])]
        self.OPTCODE = OPTCODE
        self.INSTRUCTION = str(program[step:step+4])
        self.MODE1 = MODE1
        self.MODE2 = MODE2

    def assignValues(self, program, step, MODE1, MODE2):
        if MODE1 == 'P': 
            VAL1 = program[program[step+1]]  
        elif MODE1 == 'I': 
            VAL1 = program[step+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.relbase
            VAL1 = program[RELBASE + program[step+1]]

        if MODE2 == 'P': 
            VAL2 = program[program[step+2]]  
        elif MODE2 == 'I': 
            VAL2 = program[step+2]
        else: #MODE2 == 'RELBASE'
            RELBASE = self.relbase
            VAL2 = program[RELBASE + program[step+2]]
        self.VAL1 = VAL1
        self.VAL2 = VAL2
        return VAL1, VAL2

    def assignMemory(self, program):
        programSize = len(program)
        self.inputIndex = programSize
        self.outputIndex = -1
        memory = [0 for i in range(10*programSize)]
        program = program + memory
        self.program = program 

    def assignInput(self,program, INPUT):
        program[self.inputIndex:self.inputIndex + len(INPUT)] = INPUT
        self.program = program 

    def getInput(self, program):
        INPUT = program[self.inputIndex]
        self.inputIndex = self.inputIndex + 1
        return INPUT

    def assignOutput(self, program, OUTPUT):
        program[self.outputIndex] = OUTPUT
        self.outputIndex = self.outputIndex - 1
        self.program = program 

    def assignValue(self, program, step, MODE1):
        if MODE1 == 'POSITIONAL': 
            VAL = program[program[step+1]]  
        elif MODE1 == 'IMMEDIATE': 
            VAL = program[step+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.relbase
            VAL = program[RELBASE + program[step+1]]
        self.VAL1 = VAL
        return VAL
   
    def printMessage(self):
        inst = self.INSTRUCTION
        opt = self.OPTCODE
        mode1 = self.MODE1
        mode2 = self.MODE2
        val1 = self.VAL1
        val2 = self.VAL2
        store = self.STOR
        rel = self.relbase
        step = self.STEP
        mesg = "INST:{0:8}   OPT:{1:10}   PARAMS:({2:1},{3:1})   VALUES:({4:3},{5:3})   STORE:{6:3}   RELBASE:{7:3}   STEP:{8:3}"
        print(mesg.format(inst, opt, mode1, mode2, val1, val2, store, rel, step))
    
    def getState(self):
        program = self.program
        step = self.STEP
        mode1 = self.MODE1
        mode2 = self.MODE2
        optcode = self.OPTCODE
        return program, step, mode1, mode2, optcode

    # Main Computer Functions
    def add(self, program, step, mode1, mode2):
        VAL1, VAL2 = self.assignValues(program, step, mode1, mode2)
        STOR = program[step+3]
        program[STOR] = VAL1+VAL2
        step = step + 4
        self.STOR = STOR
        self.STEP = step
        self.program = program 
    
    def mult(self, program, step, mode1, mode2):
        VAL1, VAL2 = self.assignValues(program, step, mode1, mode2)
        STOR = program[step+3]
        program[STOR] = VAL1*VAL2
        step = step + 4
        self.STOR = STOR
        self.STEP = step
        return program, step

    def Input(self, program, step, INPUT):
        STOR = program[step + 1]
        program[STOR] = INPUT
        step = step + 2
        self.STOR = STOR
        self.STEP = step
        self.program = program 

    def Output(self, program, STEP, MODE1):
        VAL = self.assignValue(program, STEP, MODE1)
        self.assignOutput(program, VAL)
        self.STEP = STEP + 2
        self.program = program
        self.output = VAL

    def JumpTrue(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)

        if VAL1 != 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3
        self.program = program  

    def JumpFalse(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        if VAL1 == 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3
        
        self.program = program 

    def LessThan(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        STOR = program[STEP+3]
        if VAL1 < VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0 
        STEP = STEP + 4
        self.STOR = STOR
        self.STEP = STEP
        self.program = program  

    def Equals(self, program, STEP, MODE1, MODE2):
        VAL1, VAL2 = self.assignValues(program, STEP, MODE1, MODE2)
        STOR = program[STEP+3]
        if VAL1 == VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0   
        STEP = STEP + 4
        self.STOR = STOR
        self.STEP = STEP
        self.program = program

    def AdjustBase(self, program, STEP, MODE1):
        self.relbase = self.relbase + program[self.STEP + 1]
        self.STEP = STEP + 2
        self.program = program

    def Halt(self, program, STEP):
        return program
        
    def RunProgram(self, program):
        programSize = len(program)
        clockMode = self.clock
        step = self.STEP
        while step < programSize:
            if clockMode: input('Press any key to step forward...')

            program, step, mode1, mode2, OPTCODE = self.getState()
            

            # Check OPTCODES and Run Functions accordingly 
            if OPTCODE == 'ADD':#1
                self.add(program, step, mode1, mode2)
            if OPTCODE == 'MULT':#2
                self.mult(program, step, mode1, mode2)
            if OPTCODE == 'INPUT':#3
                INPUT = self.getInput(program)
                self.Input(program, step, INPUT)
            if OPTCODE == 'OUTPUT':#4
                self.Output(program, step, mode1)
                self.assignOutput(program, self.output)
            if OPTCODE == 'JMPTRU':#5
                self.JumpTrue(program, step, mode1, mode2)
            if OPTCODE == 'JMPFLSE':#6
                self.JumpFalse(program, step, mode1, mode2)
            if OPTCODE == 'LESSTHN':#7
                self.LessThan(program, step, mode1, mode2)
            if OPTCODE == 'EQUALS':#8
                self.Equals(program, step, mode1, mode2)
            if OPTCODE == 'RELBASE':#9
                self.AdjustBase(program, step, mode1)
            if OPTCODE == 'HALT':#99
                program = self.Halt(program, step)
                self.STEP = programSize
                break

            if self.Print: self.printMessage()
            self.assignModes(program, self.STEP)     
        #return the output of the program
        return program[-1:self.outputIndex]