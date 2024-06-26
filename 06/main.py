import os
import sys
from typing import Optional

from hack_assembler.code import Code
from hack_assembler.enums import InstructionType
from hack_assembler.parser import Parser
from hack_assembler.symbol_table import SymbolTable


class AssemblerException(Exception):
    pass


def main(input_path: str):
    input_files = []
    if input_path.endswith(".asm"):
        input_files.append(input_path)
    else:
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".asm"):
                    input_files.append(os.path.join(root, file))

    for input_file in input_files:
        assemble(input_file)


def assemble(input_path: str, output_path: Optional[str] = None):
    if not output_path:
        output_path = input_path.split(".asm")[0] + ".hack"

    print(f"running assembler on file: {input_path}. exporting to {output_path}")

    parser = Parser(input_path)
    code = Code()
    symbol_table = SymbolTable()

    with open(output_path, "w") as output_file:
        # iter1
        while not parser.file_done:
            if parser.parse_instruction_type() == InstructionType.L:
                symbol = parser.parse_instruction_symbol()
                if symbol is not None:
                    if not symbol.isdigit():
                        symbol_table.add_entry(
                            symbol, parser.current_instruction_counter
                        )
            parser.advance()

        # iter2
        parser = Parser(input_path)
        while not parser.file_done:
            _type = parser.parse_instruction_type()
            if _type == InstructionType.A:
                symbol = parser.parse_instruction_symbol()
                if symbol is not None:
                    if symbol.isdigit():
                        value = int(symbol)
                    elif not symbol_table.contains(symbol):
                        symbol_table.add_entry(
                            symbol, parser.current_instruction_counter
                        )
                        value = symbol_table.get_address(symbol)
                    else:
                        value = symbol_table.get_address(symbol)
                    if value is None:
                        raise AssemblerException()
                    bin_instruction = str(bin(value))[2:].zfill(16)
                    output_file.write(bin_instruction + "\n")
            elif _type == InstructionType.C:
                dest = parser.parse_instruction_dest()
                comp = parser.parse_instruction_comp()
                jump = parser.parse_instruction_jump()
                bin_dest = code.get_binary_dest(dest)
                bin_comp = code.get_binary_comp(comp)
                bin_jump = code.get_binary_jump(jump)
                bin_instruction = f"111{bin_comp}{bin_dest}{bin_jump}"
                output_file.write(bin_instruction + "\n")
            parser.advance()


main(sys.argv[1])
