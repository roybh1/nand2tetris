import re
from typing import Optional

from hack_assembler.enums import InstructionType


class ParserError(Exception):
    pass


class Parser:
    """Reads and parses an instruction"""

    def __init__(self, path: str) -> None:
        """
        creates a parser and opens the source text file, at path :path:
        """
        self.file_done = False
        self._f = open(path, "r")
        self.current_instruction_counter = -1
        self.advance()

    @property
    def current_instruction(self) -> str:
        if self._current_instruction[-1] == ";":
            self._current_instruction = self._current_instruction[:-1]
        if "//" in self._current_instruction:
            self._current_instruction = self._current_instruction.split("//")[0]
        return self._current_instruction

    def advance(self) -> Optional[int]:
        """
        gets the next instruction and makes it the current instruction
        sets the self.current_instruction
        """
        if self.file_done:
            return

        _current_instruction = ""
        # handle comments
        while _current_instruction.startswith("//") or _current_instruction == "":
            _current_instruction = self._f.readline()
            if not _current_instruction:
                self.file_done = True
                self._current_instruction = ""
                self._f.close()
                return
            _current_instruction = re.sub(r"\s", "", _current_instruction)

        self._current_instruction = _current_instruction
        self.current_instruction_counter += 1

    def parse_instruction_type(self) -> InstructionType:
        """
        returns the type of the current instruction.
        A for @xxxx
        C for dest=comp;jump
        L for (xxx)
        """
        current_instruction = self.current_instruction
        if current_instruction.startswith("@"):
            return InstructionType.A
        elif current_instruction.startswith("(") and current_instruction.endswith(")"):
            return InstructionType.L
        elif "=" in current_instruction or ";" in current_instruction:
            return InstructionType.C
        raise ParserError(
            f"could not determine type for instruction: {current_instruction}"
        )

    def parse_instruction_symbol(self) -> Optional[str]:
        """
        if the current instruction is (xxx), return xxx.
        if the current instruction is @xxx, return xxx.
        otherwise, raise ParserError
        """
        current_instruction = self.current_instruction
        if current_instruction.startswith("@"):
            return current_instruction.split("@")[1]
        elif current_instruction.startswith("(") and current_instruction.endswith(")"):
            return current_instruction.split("(")[1].split(")")[0]
        elif "=" in current_instruction:
            return
        raise ParserError(
            f"could not parse symbol from instruction: {current_instruction}"
        )

    def parse_instruction_dest(self) -> Optional[str]:
        current_instruction = self.current_instruction
        if "=" in current_instruction:
            return current_instruction.split("=")[0]
        return None

    def parse_instruction_comp(self) -> str:
        instruction = self.current_instruction
        if "=" in instruction:
            instruction = instruction.split("=")[1]
            if ";" in instruction:
                return instruction.split(";")[0]
            return instruction
        elif ";" in instruction:
            return instruction.split(";")[0]
        raise ParserError(
            f"could not parse comp from instruction: {self.current_instruction}"
        )

    def parse_instruction_jump(self) -> Optional[str]:
        instruction = self.current_instruction
        if "=" in instruction:
            instruction = instruction.split("=")[1]
            if ";" in instruction:
                return instruction.split(";")[1]
            return
        elif ";" in instruction:
            return instruction.split(";")[1]
        return None
