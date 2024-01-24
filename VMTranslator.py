import sys
from vmparser import VMParser
from vmcodewriter import VMCoderWriter


def convertVMtoAssembly(outputFile, inputPath):
    outputFile.setFileName(inputPath[:-3])
    parser = VMParser(inputPath)

    while(parser.hasMoreLines()):
        parser.advance()
        commandType = parser.commandType()
        if commandType=="C_ARITHMETIC":
            outputFile.writeArithmetic(parser.args1())
        elif commandType=="C_PUSH" or commandType=="C_POP" or commandType=="C_FUNCTION" or commandType=="C_CALL":
            outputFile.writePushPop(str(commandType),parser.args1(),parser.args2())
        else:
            pass #Next Week - HW8

def main():
    
    input = sys.argv[1]
    file = input[:-2] + 'asm'

    asmFile = VMCoderWriter(file)
    convertVMtoAssembly(asmFile,input)
    
    #Finish the code
    asmFile.writeTheEnd()
    asmFile.close()
    


if __name__ == '__main__':
    main()

