class VMCoderWriter:

    def __init__(self, filePath):
        self.file = open(filePath, 'w')
        self.currentCommand = 0
        self.fileName = None

    def close(self):
        self.file.close()

    def writeTheEnd(self):
        self.file.write("(END_LOOP)\n")
        self.file.write("@END_LOOP\n")
        self.file.write("0;JMP")

    def setFileName(self, fileName):
        self.fileName = fileName

    def writeArithmetic(self, command) -> None:
        self.currentCommand += 1

        # Go to last place in the stack
        self.file.write("@SP\n")
        self.file.write("A=M-1\n")

        if command == "neg":
            self.file.write("M=-M\n")

        elif command == "not":
            self.file.write("M=!M\n")
        else:
            self.file.write("D=M\n")
            self.file.write("A=A-1\n")
            if command == ("eq" or "lt" or "gt"):
                self.file.write("D=M-D\n")  # x-y
                self.file.write(f"@ISTRUE{self.currentCommand}\n")  # If true it will jump and change the value
                match command:
                    case "eq":
                        self.file.write("D;JEQ\n")
                    case "gt":
                        self.file.write("D;JGT\n")
                    case "lt":
                        self.file.write("D;JLT\n")

                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("A=A-1\n")
                self.file.write("M=0\n")
                self.file.write(f"@END{self.currentCommand}\n")
                self.file.write("0;JMP\n")
                #(ISTRUE)
                self.file.write(f"(ISTRUE{self.currentCommand})\n")
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("A=A-1\n")
                self.file.write("M=0\n")
                self.file.write("M=!M\n")
                #(END)
                self.file.write(f"(END{self.currentCommand})\n")
                self.file.write("0\n")

            else:
                match command:
                    case "add":
                        self.file.write("M=M+D\n")  # x+y
                    case "sub":
                        self.file.write("M=M-D\n")  # x-y
                    case "and":
                        self.file.write("M=M&D\n")  # x&y
                    case "or":
                        self.file.write("M=M|D\n")  # x|y
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
    
    def writePushPop(self, command, segment, index) -> None:
        self.currentCommand += 1

        if command == 'C_PUSH':  #to change!!!!!!         
            if segment == 'constant':
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
            elif segment=="static":
                self.file.write(f"@{self.fileName}.{index}\n")
                self.file.write("D=M\n")
            
            elif segment=="pointer":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                self.file.write("@3\n")
                self.file.write("A=D+A\n")
                self.file.write("D=M\n")
            elif segment=="temp":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                self.file.write("@5\n")
                self.file.write("A=D+A\n")
                self.file.write("D=M\n")
            else: # that / local / local / argument
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                match segment:
                    case "that":
                        self.file.write("@THAT\n")
                    case "this":
                        self.file.write("@THIS\n")
                    case "local":
                        self.file.write("@LCL\n")
                    case "argument":
                        self.file.write("@ARG\n")
                self.file.write("A=D+M\n")
                self.file.write("D=M\n")

            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")

        else:  # For 'pop' command
            if segment == 'static':
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("D=M\n")
                self.file.write(f"@{self.fileName}.{index}\n")
                self.file.write("M=D\n")
            else: # pointer / temp / that / local / local / argument
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                if segment=="pointer":
                    self.file.write("@3\n")
                    self.file.write("D=D+A\n")
                elif segment=="temp":
                    self.file.write("@5\n")
                    self.file.write("D=D+A\n")
                else: # that / local / local / argument
                    match segment:
                        case "that":
                            self.file.write("@THAT\n")
                        case "this":
                            self.file.write("@THIS\n")
                        case "local":
                            self.file.write("@LCL\n")
                        case "argument":
                            self.file.write("@ARG\n")
                    self.file.write("D=D+M\n")
 
                self.file.write("@13\n") #Free place in the stack
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("D=M\n")
                self.file.write("@13\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
            #SP--
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
     
      