
class VMCoderWriter:

    #Constructor
    def __init__(self, path) -> None:
        self.currentCommand = 0
        self.file = open(path, 'w')
        self.fileName = None

    def close(self):
        self.file.close()

    def setFileName(self, fileName) -> None:
        self.fileName=fileName

    def writeArtihmetic(self, command) -> None:
        self.currentCommand+=1

        #Go to last place
        self.file.write("@SP\n")
        self.file.write("A=M-1\n")

        if command=="neg":
            self.file.write("M=-M\n")

        elif command=="not":
            self.file.write("M=!M\n")
        else:
            self.file.write("D=M\n")
            self.file.write("A=M-1\n")
            if command==("eq" or "lt" or "gt"):
                self.file.write("D=M-D\n") #x-y
                self.file.write(f"@ISTRUE{self.commandNum}")
                match command:
                    case "eq":
                        self.file.write("D;JEQ\n") 
                    case "gt":
                        self.file.write("D;JGT\n")
                    case "lt":
                        self.file.write("D;JLT\n")
                self.file.write("@SP")
                self.file.write("A=M-1")
                self.file.write("A=A-1")
                self.file.write("M=0") #Current stack position

                self.file.write(f"@END{self.commandNum}")
                self.file.write("0;JMP")

                self.file.write(f"(ISTRUE{self.commandNum})")
                self.file.write("@SP")
                self.file.write("A=M-1")
                self.file.write("A=A-1")
                self.file.write("M=0")
                self.file.write("M!=M")

                self.file.write(f"END{self.commandNum}")
                self.file.write("0")

            else:
                match command:
                    case "add":
                        self.file.write("A=A+D\n") #x+y
                    case "sub":
                        self.file.write("A=A-D\n") #x-y
                    case "and":
                        self.file.write("A=A&D\n") #x&y
                    case "or":
                        self.file.write("A=A|D\n") #x|y
            self.file.write("@SP")
            self.file.write("M=M-1")       

    def writePushPop(self, command, segment, index) -> None:
        self.currentCommand+=1

        if command=="C_PUSH":
            if segment=="constant":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                
            elif segment==("local" or "argument" or "this" or "that"):
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                self.file.write(f"@{segment}\n")
                self.file.write("A=D+M\n")

            elif segment=="static":
                self.file.write(f"@{self.fileName}.{index}\n")
                
            else:
                if segment=="temp":
                    self.file.write(f"@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@5\n")
                    self.file.write("A=D+A\n")

                elif segment=="pointer": 
                    self.file.write("f@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@3\n") 
                    self.file.write("A=D+A\n")
                    
            #RAM[SP]=D                
            self.file.write("@SP\n")
            self.file.write("D=M\n")
            self.file.write("M=D\n")
            #SP++
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")    
        
        else:
            if segment=="static":
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("D=M")
                self.file.write(f"@{self.fileName}.{index}\n")
                self.file.write("M=D")

            else:
                if segment==("local" or "argument" or "this" or "that"):
                    self.file.write(f"@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write(f"@{segment}\n")
                    self.file.write("D=D+M\n")

                elif segment=="temp":
                    self.file.write(f"@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@5\n")
                    self.file.write("D=D+A\n")

                elif segment=="pointer": 
                    self.file.write(f"@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@3\n") 
                    self.file.write("D=D+A\n")

                #Store the data in cell 13
                self.file.write("@13\n")
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




    