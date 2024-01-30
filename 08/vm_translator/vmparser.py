class VMParser:
    def __init__(self, input_vm_file: str) -> None:
        self.file_lines = []
        with open(input_vm_file, "r") as file:
            for line in file:
                # Split the line at '//', take the first part, clean the row
                clean_line = line.split("//")[0].strip()
                # Add to the list
                if clean_line:
                    self.file_lines.append(clean_line)

        self.line_number = -1
        self.num_of_lines = len(self.file_lines) - 1

    def advance(self) -> None:
        if self.has_more_lines:
            self.line_number += 1
            self.current_line = self.file_lines[self.line_number]

    @property
    def has_more_lines(self) -> bool:
        return self.line_number < self.num_of_lines

    @property
    def command_type(self):
        if "push" in self.current_line:
            return "C_PUSH"
        elif "pop" in self.current_line:
            return "C_POP"
        elif "label" in self.current_line:
            return "C_LABEL"
        elif "goto" in self.current_line:
            return "C_GOTO"
        elif "if-goto" in self.current_line:
            return "C_IF"
        elif "function" in self.current_line:
            return "C_FUNCTION"
        elif "return" in self.current_line:
            return "C_RETURN"
        elif "call" in self.current_line:
            return "C_CALL"
        else:
            return "C_ARITHMETIC"

    @property
    def args1(self) -> str:
        if self.command_type == "C_ARITHMETIC":
            return self.current_line
        if self.command_type == "C_RETURN":
            return ""
        else:
            return self.current_line.split()[1]

    @property
    def args2(self) -> int:
        return self.current_line.split()[2]
