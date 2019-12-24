class computer:
    """
    Advent of Code 2019 INTCODE Computer Object
    """
    #Computer (Class) Variables
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 9:'RELBASE', 99:'HALT'}
    modedefs = {0: 'P', 1: 'I', 2:'R'}
    clockMode = {'RUN':False, 'STEP':True}

    def __init__(self, computer_name = 'IntcodeA', relative_base = 0, clock_Mode = 'RUN', Print = False):
        self.Name = computer_name

        # debug settings for computer
        self.clock = computer.clockMode[clock_Mode.upper()]
        self.Print = Print

        # state of computer
        self.PROGRAM = []
        self.INSTRUCTION = '0000'
        self.OPTCODE = 0
        self.MODE1 = 'N/A'
        self.MODE2 = 'N/A'
        self.MODE3 = 'N/A'
        self.VAL1 = 0
        self.VAL2 = 0
        self.VAL3 = 0
        self.STOR = 0
        self.STEP = 0
        self.REL = 0
        self.HALT = False
        #state of input and output pointers
        self.Out = 0
        self.In = -1

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
        READ = str(program[STEP]).rjust(5,'0')
        OPTCODE = computer.optcodes[int(READ[-2:])]
        MODE1 = computer.modedefs[int(READ[2])]
        MODE2 = computer.modedefs[int(READ[1])]
        MODE3 = computer.modedefs[int(READ[0])]
        self.OPTCODE = OPTCODE
        self.INSTRUCTION = program[STEP:STEP+4]
        self.MODE1 = MODE1
        self.MODE2 = MODE2
        self.MODE3 = MODE3

        program = self.PROGRAM
        MODE1 = self.MODE1
        MODE2 = self.MODE2
        MODE3 = self.MODE3
        STEP = self.STEP

    def assignMemory(self, SCALE = 50):
        program = self.PROGRAM
        self.programSize = len(program)
        memory = [0 for i in range(SCALE*self.programSize)]
        program = program + memory
        self.PROGRAM = program 

    def assignInput(self,INPUT):
        self.INPUT = INPUT
        program = self.PROGRAM
        #store the input in the front end of memory
        if self.Print: print('ASSIGNING INPUT {}'.format(INPUT))
        program[-1] = INPUT
        self.PROGRAM = program 

    def assignOutput(self, OUTPUT):
        program = self.PROGRAM
        Out = self.Out
        program[Out] = OUTPUT
        self.PROGRAM = program 
        self.Out = Out + 1

    def assignValue(self, mode, step, program):
        #step should be the parameter's pointer
        if mode == 'P': 
            return program[program[step]]  
        elif mode == 'I': 
            return program[step]
        else: #MODE1 == 'RELBASE'
            RELBASE = self.REL
            return program[RELBASE + program[step]]
            
    def assignStorage(self, mode, step, program):
        #step should be the parameter's pointer
        if mode == 'P': 
            return program[step] 
        elif mode == 'R': 
            RELBASE = self.REL
            return RELBASE + program[step]
        else:
            print('Immediate Storage Not Allowed')
            self.HALT = True
 
    def printMessage(self, intlength = 4):
        inst = str(self.INSTRUCTION[:intlength])
        opt = self.OPTCODE
        mode1 = self.MODE1
        mode2 = self.MODE2
        mode3 = self.MODE3
        val1 = self.VAL1
        val2 = self.VAL2
        val3 = self.VAL3
        store = self.STOR
        rel = self.REL
        step = self.STEP
        mesg = "INST:{0:20}   OPT:{1:10}   PARAMS:({2:1},{3:1},{4:1})   VALUES:({5:3},{6:3},{7:3})   \tSTORE:{8:3}   RELBASE:{9:3}   STEP:{10:3}"
        print(mesg.format(inst, opt, mode1, mode2, mode3, val1, val2, val3, store, rel, step))
    
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
        program = self.PROGRAM
        STEP = self.STEP

        VAL1 = self.assignValue(self.MODE1, STEP + 1, program)
        VAL2 = self.assignValue(self.MODE2, STEP + 2, program)
        VAL3 = self.assignStorage(self.MODE3, STEP + 3, program)

        program[VAL3] = VAL1+VAL2
        
        self.VAL1 = VAL1
        self.VAL2 = VAL2
        self.STOR = VAL3
        if self.Print: self.printMessage()
        self.STEP = STEP + 4
        self.PROGRAM = program 
    
    def mult(self):
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.assignValue(self.MODE1, STEP + 1, program)
        VAL2 = self.assignValue(self.MODE2, STEP + 2, program)
        VAL3 = self.assignStorage(self.MODE3, STEP + 3, program)


        program[VAL3] = VAL1*VAL2

        self.VAL1 = VAL1
        self.VAL2 = VAL2
        self.STOR = VAL3
        if self.Print: self.printMessage()
        self.STEP = STEP + 4
        self.PROGRAM = program

    def Input(self):
        program = self.PROGRAM  
        STEP = self.STEP
        MODE1 = self.MODE1
        if self.Print: print('INPUT TO PROGRAM: {}'.format(program[-1]))
        # Assign Input to Only Parameter <- Find Input in Memory using In
        if MODE1 == 'P':
            program[program[STEP + 1]] = program.pop()
        elif MODE1 == 'R':
            RELBASE = self.REL
            program[RELBASE + program[STEP + 1]] = program.pop()
        else: #MODE1 = 'I' Not Supposed to Happen
            program[STEP + 1] = program.pop()

        if self.Print: self.printMessage(2)
        self.STEP = STEP + 2
        self.PROGRAM = program 

    def Output(self):
        """Parameters that an instruction writes to will never be in immediate mode."""
        program = self.PROGRAM
        STEP = self.STEP
        MODE1 = self.MODE1
        VAL1 = self.assignValue(MODE1, STEP+1, program)


        #override the mode check for output
        if MODE1 == 'P':
            #write to the address of you parameter. This is why it can't be immediate
            output = VAL1
        elif MODE1 == 'R':
            output = VAL1
        else:#MODE1 == 'I'
            output = VAL1

        self.assignOutput(output)
        if self.Print: self.printMessage(2)
        self.STOR = VAL1
        self.PROGRAM = program
        self.STEP = STEP + 2
        return output

    def JumpTrue(self):
        STEP = self.STEP
        program = self.PROGRAM
        VAL1 = self.assignValue(self.MODE1, STEP+1, program)
        VAL2 = self.assignValue(self.MODE2, STEP+2, program)

        if self.Print: self.printMessage(3)

        if VAL1 != 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3

    def JumpFalse(self):
        STEP = self.STEP
        program = self.PROGRAM
        VAL1 = self.assignValue(self.MODE1, STEP+1, program)
        VAL2 = self.assignValue(self.MODE2, STEP+2, program)

        if self.Print: self.printMessage(3)

        if VAL1 == 0:
            self.STEP = VAL2
        else:
            self.STEP = STEP + 3

    def LessThan(self):
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.assignValue(self.MODE1, STEP + 1, program)
        VAL2 = self.assignValue(self.MODE2, STEP + 2, program)
        VAL3 = self.assignStorage(self.MODE3, STEP + 3, program)
        
        STOR = VAL3
        if VAL1 < VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0 
        self.STOR = STOR
        if self.Print: self.printMessage()
        self.STEP = STEP + 4
        self.PROGRAM = program  

    def Equals(self):
        program = self.PROGRAM
        STEP = self.STEP
        VAL1 = self.assignValue(self.MODE1, STEP + 1, program)
        VAL2 = self.assignValue(self.MODE2, STEP + 2, program)
        VAL3 = self.assignStorage(self.MODE3, STEP + 3, program)

        STOR = VAL3
        if VAL1 == VAL2: 
            program[STOR] = 1
        else:
            program[STOR] = 0   
        self.STOR = STOR
        if self.Print: self.printMessage()
        self.STOR = STOR
        self.VAL1 = VAL1
        self.VAL2 = VAL2
        self.VAL3 = VAL3
        self.STEP = STEP + 4
        self.PROGRAM = program

    def AdjustBase(self):
        program = self.PROGRAM
        STEP = self.STEP
        REL = self.REL
        MODE1 = self.MODE1

        if MODE1 == 'P':
            VAL = program[program[STEP+1]]
        elif MODE1 == 'I':
            VAL = program[STEP+1]
        else: #MODE1 == 'R'
            RELBASE = self.REL
            VAL = program[RELBASE + program[STEP+1]]
        if self.Print: self.printMessage(2)
        self.REL = REL + VAL
        self.STEP = STEP + 2
        self.PROGRAM = program

    def LoadProgram(self, program, INPUT = 0):
        self.reset()
        self.PROGRAM = program
        self.Out = len(program)
        self.assignMemory()
        self.assignInput(INPUT)  

    def reset(self):
        # state of computer
        self.PROGRAM = []
        self.INSTRUCTION = '0000'
        self.OPTCODE = 0
        self.MODE1 = 'N/A'
        self.MODE2 = 'N/A'
        self.MODE3 = 'N/A'
        self.VAL1 = 0
        self.VAL2 = 0
        self.VAL3 = 0
        self.STOR = 0
        self.STEP = 0
        self.REL = 0
        self.HALT = False
        #state of input and output pointers
        self.Out = -1
        self.In = 0

    def RunProgram(self):
        clockMode = self.clock
        Halting = self.HALT
        self.assignModes()
        while not Halting:
            #step thru each clock cycle to debug
            if clockMode: 
                user = input('Any key step forward...q to quit')
                if user == 'q':
                    return
        
            # Check OPTCODES and Run Functions accordingly 
            OPTCODE = self.OPTCODE

            if OPTCODE == 'ADD':#1
                self.add()
            if OPTCODE == 'MULT':#2
                self.mult()
            if OPTCODE == 'INPUT':#3
                self.Input()
            if OPTCODE == 'OUTPUT':#4
                return self.Output()
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
                self.HALT = True
                Halting = True
                return 99
            #end OPTCODE Checks
            self.assignModes()
        #end while loop 