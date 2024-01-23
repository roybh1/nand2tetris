
class VMCoderWriter:

    #Constructor
    def __init__(self, path) -> None:
        self.currentline = -1
        self.lastLine = 0
        self.file = open(path, 'w')
        self.fileName = None

    def close(self):
        self.file.close()

    def setFileName(self, fileName):
        self.fileName=fileName

    def writeArtihmetic(self, command):
        pass

    def writePushPop(self, command, segment, index):
        self.currentline+=1

        if command=="C_PUSH":
            if segment=="constant":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                
            elif segment==("local" or "argument" or "this" or "that"):
                self.file.write("@{index}\n")
                self.file.write("D=A\n")
                self.file.write("@{segment}\n")
                self.file.write("A=D+M\n")

            elif segment=="static":
                self.file.write(f"@{self.fileName}.{index}\n")
                
            else:
                if segment=="temp":
                    self.file.write("@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@5\n")
                    self.file.write("A=D+A\n")

                elif segment=="pointer": 
                    self.file.write("@{index}\n")
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
                    self.file.write("@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@{segment}\n")
                    self.file.write("D=D+M\n")

                elif segment=="temp":
                    self.file.write("@{index}\n")
                    self.file.write("D=A\n")
                    self.file.write("@5\n")
                    self.file.write("D=D+A\n")

                elif segment=="pointer": 
                    self.file.write("@{index}\n")
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




    