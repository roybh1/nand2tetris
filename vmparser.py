class Parser:
    #Constructor
    def __init__(self,inputVMfile):
        self.fileLines =[]
        with open(inputVMfile, 'r') as file:
            for line in file:
                # Split the line at '//', take the first part, clean the row
                cleanLine = line.split('//')[0].strip()
                # Add to the list
                if cleanLine:
                    self.fileLines.append(cleanLine)
        
        self.lineNumber = -1
        self.currentLine = None
        self.numOfLines = len(self.fileLines)-1


    def hasMoreLines(self) -> bool:
        return self.lineNumber<self.numOfLines

    def advance(self):
        if self.hasMoreLines():
            self.lineNumber+=1
            self.currentLine=self.fileLines[self.lineNumber]

    def commandType(self):
        if "push" in self.currentLine:
            return "C_PUSH"
        elif "pop" in self.currentLine:
            return "C_POP"
        elif "label" in self.currentLine:
            return "C_LABEL"
        elif "goto" in self.currentLine:
            return "C_GOTO"
        elif "if-goto" in self.currentLine:
            return "C_IF"
        elif "function" in self.currentLine:
            return "C_FUNCTION"
        elif "return" in self.currentLine:
            return "C_RETURN"
        elif "call" in self.currentLine:
            return "C_CALL"
        else:
            return "C_ARITHMETIC"

    def args1(self) -> str:
        if self.commandType() == "C_ARITHMETIC":
            return self.currentLine
        if self.commandType() == "C_RETURN":
            return
        else:
            return self.currentLine.split()[1]
    def args2(self) ->int:
        return self.currentLine.split()[2]