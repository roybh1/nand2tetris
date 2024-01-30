import os
import sys

from vm_translator.vmcodewriter import VMCodeWriter
from vm_translator.vmparser import VMParser


def convert_vm_to_assembly(output_file: VMCodeWriter, inputPath: str):
    baseName = os.path.basename(inputPath)
    output_file.set_file_name(baseName[:-3])
    parser = VMParser(inputPath)

    while parser.has_more_lines:
        parser.advance()
        command_type = parser.command_type
        if command_type == "C_ARITHMETIC":
            output_file.write_arithmetic(parser.args1)
        elif command_type in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            output_file.write_push_pop(command_type, parser.args1, parser.args2)
        elif (command_type == "C_LABEL"):
            output_file.write_label(parser.args1)
        elif (command_type == "C_GOTO"):
            output_file.write_goto(parser.args1)
        elif (command_type == "C_IF"):
            output_file.write_if(parser.args1)
        else:
            pass



def main():

    input = sys.argv[1]

    # File name
    if os.path.isfile(input) and input.endswith(".vm"):
        file = input[:-2] + "asm"
        asmFile = VMCodeWriter(file)
        convert_vm_to_assembly(asmFile, input)
        asmFile.close()

    # Dir
    elif os.path.isdir(input):
        dir = os.path.normpath(input)
        outputName = os.path.join(dir, os.path.basename(dir) + ".asm")
        asmFile = VMCodeWriter(outputName)

        for filename in os.listdir(dir):
            if filename.endswith(".vm"):
                vmPath = os.path.join(dir, filename)
                convert_vm_to_assembly(asmFile, vmPath)

        asmFile.close()


if __name__ == "__main__":
    main()
