import sys
from vmparser import VMParser
from vmcodewriter import VMCoderWriter



def main():
    if len(sys.argv) != 2:
        vmFile = sys.argv[1]
        name = vmFile.split('.')[0]
        file = name +".asm"
        readVM = VMParser(vmFile)
        asmFile = VMCoderWriter(file)
        asmFile.setFileName(name)

        while(readVM.hasMoreLines):
            readVM.advance()
            commandType = readVM.commandType()
            if commandType=="C_ARITHMETIC":
                asmFile.writeArtihmetic(readVM.args1())
            elif commandType==("C_PUSH" or "C_POP"):
                asmFile.writePushPop(commandType,readVM.args1(),readVM.args2())
            else:
                pass #Next Week - HW8

        #Finish the code
        asmFile.writeTheEnd()
        asmFile.close()

    else:
        print("No path provided.")

if __name__ == '__main__':
    main()
