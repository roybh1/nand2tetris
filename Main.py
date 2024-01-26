import sys
from vmparser import VMParser
from vmcodewriter import VMCodeWriter
import os



def convertVMtoAssembly(outputFile, inputPath):
    baseName = os.path.basename(inputPath)
    outputFile.setFileName(baseName[:-3])
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


    #File name
    if os.path.isfile(input) and input.endswith('.vm'):
        file = input[:-2] + 'asm'
        asmFile = VMCodeWriter(file)
        convertVMtoAssembly(asmFile,input)
        asmFile.close()

    #Dir
    elif os.path.isdir(input):
        dir = os.path.normpath(input)
        outputName = os.path.join(dir, os.path.basename(dir) + '.asm')
        asmFile = VMCodeWriter(outputName)

        for filename in os.listdir(dir):
            if filename.endswith('.vm'):
                vmPath = os.path.join(dir, filename)
                convertVMtoAssembly(asmFile, vmPath)

        asmFile.close()


if __name__ == '__main__':
    main()

