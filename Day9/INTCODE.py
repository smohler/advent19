class computer:
    """
    Advent of Code 2019 INTCODE Computer Object
    """
    #Computer (Class) Variables
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 9:'RELBASE', 99:'HALT'}
    modedefs = {0: 'P', 1: 'I', 2:'R'}
    clockMode = {'RUN':False, 'STEP':True}

    def __init__(self, computer_name = 'IntcodeA', relative_base = 0, clock_Mode = 'RUN', print_Mode = False):
        self.Name = computer_name

        # debug settings for computer
        self.clock = computer.clockMode[clock_Mode.upper()]
        self.Print = print_Mode

        # state of computer
        self.PROGRAM = []
        self.INSTRUCTION = '0000'
        self.OPTCODE = 0
        self.MODE1 = 'N/A'
        self.MODE2 = 'N/A'
        self.VAL1 = 0
        self.VAL2 = 0
        self.STOR = 0
        self.STEP = 0
        self.REL = relative_base
        self.HALT = False
        #state of input and output pointers
        self.Out = -1
        self.In = 0

    def __str__(self):
        CurrentState ='NAME:{}\nINST:{}\nOPT:{}\nMODE1:{}\nMODE2:{}\nVAL1:{}\nVAL2:{}\nSTOR:{}\nSTEP:{}\nREL:{}\nHALT:{}\nPROGRAM:{}'
        n = self.Name
        i = self.INSTRUCTION
        o = self.OPTCODE
        m1 = self.MODE1
        m2 = self.MODE2
        v1 = self.VAL1
        v2 = self.VAL2
        sr = self.STOR
        sp = self.STEP
        r = self.REL
        h = self.HALT
        p = self.PROGRAM
        return CurrentState.format(n,i,o,m1,m2,v1,v2,sr,sp,r,h, p)


    # Sub Routines for Computer Methods
    def assignModes(self):
        #read the first instruction to set the optcode and parameter mode
        #put zero padding in instructions as not provied means 0
        program = self.PROGRAM
        STEP = self.STEP
        READ = str(program[STEP]).rjust(4,'0')
        OPTCODE = computer.optcodes[int(READ[-2:])]
        MODE1 = computer.modedefs[int(READ[1])]
        MODE2 = computer.modedefs[int(READ[0])]
        self.OPTCODE = OPTCODE
        self.INSTRUCTION = str(program[STEP:STEP+4])
        self.MODE1 = MODE1
        self.MODE2 = MODE2

    def assignValues(self):
        program = self.PROGRAM
        MODE1 = self.MODE1
        MODE2 = self.MODE2
        STEP = self.STEP
        if MODE1 == 'P': 
            VAL1 = program[program[STEP+1]]  
        elif MODE1 == 'I': 
            VAL1 = program[STEP+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.REL
            VAL1 = program[RELBASE + program[STEP+1]]

        if MODE2 == 'P': 
            VAL2 = program[program[STEP+2]]  
        elif MODE2 == 'I': 
            VAL2 = program[STEP+2]
        else: #MODE2 == 'RELBASE'
            RELBASE = self.REL
            VAL2 = program[RELBASE + program[STEP+2]]
        self.VAL1 = VAL1
        self.VAL2 = VAL2

    def assignMemory(self, SCALE = 10):
        program = self.PROGRAM
        programSize = len(program)
        memory = [0 for i in range(SCALE*programSize)]
        program = program + memory
        self.PROGRAM = program 
        self.In = programSize

    def assignInput(self,INPUT):
        self.INPUT = INPUT
        program = self.PROGRAM
        #store the input in the front end of memory
        program[self.In:self.In + len(INPUT)] = INPUT
        self.PROGRAM = program 

    def assignOutput(self, OUTPUT):
        program = self.PROGRAM
        Out = self.Out
        program[Out] = OUTPUT
        self.PROGRAM = program 
        self.Out = Out - 1

    def assignValue(self):
        MODE1 = self.MODE1
        program = self.PROGRAM
        STEP = self.STEP
        if MODE1 == 'P': 
            VAL = program[program[STEP+1]]  
        elif MODE1 == 'I': 
            VAL = program[STEP+1]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.REL
            VAL = program[RELBASE + program[STEP+1]]
        self.VAL1 = VAL
   
    def printMessage(self):
        inst = self.INSTRUCTION
        opt = self.OPTCODE
        mode1 = self.MODE1
        mode2 = self.MODE2
        val1 = self.VAL1
        val2 = self.VAL2
        store = self.STOR
        rel = self.REL
        step = self.STEP
        mesg = "INST:{0}   \tOPT:{1:10}   PARAMS:({2:1},{3:1})   VALUES:({4:3},{5:3})   STORE:{6:3}   RELBASE:{7:3}   STEP:{8:3}"
        print(mesg.format(inst, opt, mode1, mode2, val1, val2, store, rel, step))
    
    def getState(self):
        """Debug function to pause and get the current state of the computer
        return (program, step, stor, mode1, mode2, val1, val2, optcode, In, Out, instruction)
        """
        p = self.PROGRAM
        sp = self.STEP
        st = self.STOR
        m1 = self.MODE1
        m2 = self.MODE2
        v1 = self.VAL1
        v2 = self.VAL2
        opt = self.OPTCODE
        i = self.In
        o = self.Out
        inst = self.INSTRUCTION

        return p,sp,st,m1,m2,v1,v2,opt,i,o,inst

    # Main Computer Functions
    def add(self):
        self.assignValues()
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.VAL1
        VAL2 = self.VAL2
        STOR = program[STEP+3]
        program[STOR] = VAL1+VAL2
        self.STOR = STOR
        self.STEP = STEP + 4
        self.PROGRAM = program 
    
    def mult(self):
        self.assignValues()
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.VAL1
        VAL2 = self.VAL2
        STOR = program[STEP+3]
        program[STOR] = VAL1*VAL2
        self.STOR = STOR
        self.STEP = STEP + 4
        self.PROGRAM = program

    def Input(self):
        program = self.PROGRAM  
        In = self.In #input address pointer
        STEP = self.STEP
        # Assign Input to Only Parameter <- Find Input in Memory using In
        program[STEP + 1] = program[In]
        self.STEP = STEP + 2
        self.In = In + 1 #step forward to next input in stack
        self.PROGRAM = program 

    def Output(self):
        self.assignValue() 
        STEP = self.STEP
        VAL = self.VAL1
        self.assignOutput(VAL) # PROGRAM and OUT changed in assignOutput
        self.STEP = STEP + 2

    def JumpTrue(self):
        self.assignValues()
        STEP = self.STEP
        VAL1 = self.VAL1
        VAL2 = self.VAL2

        if VAL1 != 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3

    def JumpFalse(self):
        self.assignValues()
        STEP = self.STEP
        VAL1 = self.VAL1
        VAL2 = self.VAL2
        if VAL1 == 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3

    def LessThan(self):
        self.assignValues()
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.VAL1
        VAL2 = self.VAL2
        STOR = program[STEP+3]
        if VAL1 < VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0 
        STEP = STEP + 4
        self.STOR = STOR
        self.STEP = STEP
        self.PROGRAM = program  

    def Equals(self):
        self.assignValues()
        VAL1 = self.VAL1
        VAL2 = self.VAL2
        program  = self.PROGRAM
        STEP = self.STEP
        STOR = program[STEP+3]
        if VAL1 == VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0   
        STEP = STEP + 4
        self.STOR = STOR
        self.STEP = STEP
        self.PROGRAM = program

    def AdjustBase(self):
        STEP = self.STEP
        REL = self.REL
        program = self.PROGRAM
        self.REL = REL + program[STEP + 1]
        self.STEP = STEP + 2
        self.PROGRAM = program

    def LoadProgram(self, program, INPUT = [0]):
        self.resetState()
        self.PROGRAM = program
        self.assignMemory()
        self.assignInput(INPUT)  

    def resetState(self):
        # state of computer
        self.PROGRAM = []
        self.INSTRUCTION = '0000'
        self.OPTCODE = 0
        self.MODE1 = 'N/A'
        self.MODE2 = 'N/A'
        self.VAL1 = 0
        self.VAL2 = 0
        self.STOR = 0
        self.STEP = 0
        self.REL = 0
        self.HALT = False
        #state of input and output pointers
        self.Out = -1
        self.In = 0

    def RunProgram(self):
        clockMode = self.clock
        printMode = self.Print
        Halting = self.HALT
        self.assignModes()
        while not Halting:
            #step thru each clock cycle to debug
            if clockMode: input('Press any key to step forward...')
            if printMode: self.printMessage()

            # Check OPTCODES and Run Functions accordingly 
            
            OPTCODE = self.OPTCODE
            if OPTCODE == 'ADD':#1
                self.add()
            if OPTCODE == 'MULT':#2
                self.mult()
            if OPTCODE == 'INPUT':#3
                self.Input()
            if OPTCODE == 'OUTPUT':#4
                self.Output()
            if OPTCODE == 'JMPTRU':#5
                self.JumpTrue()
            if OPTCODE == 'JMPFLSE':#6
                self.JumpFalse()
            if OPTCODE == 'LESSTHN':#7
                self.LessThan()
            if OPTCODE == 'EQUALS':#8
                self.Equals()
            if OPTCODE == 'RELBASE':#9
                self.AdjustBase()
            if OPTCODE == 'HALT':#99
                Halting = True
                program = self.PROGRAM
                output = program[self.Out + 1:]
                print(output)
                output.reverse() 
            #end OPTCODE Checks
            self.assignModes()
        return output
        #end while loop 
