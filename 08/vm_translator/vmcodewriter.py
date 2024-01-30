class VMCodeWriter:
    def __init__(self, filePath: str):
        self.file = open(filePath, "w")
        self.current_command = 0
        self.file_name = None

    def close(self) -> None:
        self.file.close()

    def set_file_name(self, file_name) -> None:
        self.file_name = file_name

    def write_the_end(self) -> None:
        self.file.write("(END_LOOP)\n")
        self.file.write("@END_LOOP\n")
        self.file.write("0;JMP")

    def write_label(self, label: str) -> None:
        self.current_command += 1

        self.file.write(f"({label})\n")

    def write_goto(self, label: str) -> None:
        self.current_command += 1

        self.file.write(f"@{label}\n")
        self.file.write("0;JMP\n")

    def write_if(self, label: str) -> None:
        self.current_command += 1

        # go to last in stack and hold the cond value
        self.file.write("@SP\n")
        self.file.write("A=M-1\n")
        self.file.write("D=M\n")

        # change address of last in stack
        self.file.write("@SP\n")
        self.file.write("M=M-1\n")

        # go to if cond holds
        self.file.write(f"@{label}\n")
        self.file.write("D;JNE\n")

    def write_function(self, function_name: str, nvars: int) -> None:
        pass

    def write_call(self, function_name: str, nargs: int) -> None:
        pass

    def write_return(self) -> None:
        pass

    def write_arithmetic(self, command: str) -> None:
        self.current_command += 1

        # Go to last place in the stack
        self.file.write("@SP\n")
        self.file.write("A=M-1\n")

        if command == "neg":
            self.file.write("M=-M\n")

        elif command == "not":
            self.file.write("M=!M\n")

        else:
            self.file.write("D=M\n")
            self.file.write("A=A-1\n")

            if command == "eq" or command == "lt" or command == "gt":
                self.file.write("D=M-D\n")  # x-y
                self.file.write(
                    f"@ISTRUE{self.current_command}\n"
                )  # If true it will jump and change the value
                match command:
                    case "eq":
                        self.file.write("D;JEQ\n")
                    case "gt":
                        self.file.write("D;JGT\n")
                    case "lt":
                        self.file.write("D;JLT\n")

                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("A=A-1\n")
                self.file.write("M=0\n")
                self.file.write(f"@END{self.current_command}\n")
                self.file.write("0;JMP\n")
                # (ISTRUE)
                self.file.write(f"(ISTRUE{self.current_command})\n")
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("A=A-1\n")
                self.file.write("M=0\n")
                self.file.write("M=!M\n")
                # (END)
                self.file.write(f"(END{self.current_command})\n")
                self.file.write("0\n")

            else:
                match command:
                    case "add":
                        self.file.write("M=M+D\n")  # x+y
                    case "sub":
                        self.file.write("M=M-D\n")  # x-y
                    case "and":
                        self.file.write("M=M&D\n")  # x&y
                    case "or":
                        self.file.write("M=M|D\n")  # x|y
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        self.current_command += 1

        if command == "C_PUSH":  # to change!!!!!!
            if segment == "constant":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
            elif segment == "static":
                self.file.write(f"@{self.file_name}.{index}\n")
                self.file.write("D=M\n")

            elif segment == "pointer":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                self.file.write("@3\n")
                self.file.write("A=D+A\n")
                self.file.write("D=M\n")
            elif segment == "temp":
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                self.file.write("@5\n")
                self.file.write("A=D+A\n")
                self.file.write("D=M\n")
            else:  # that / local / local / argument
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                match segment:
                    case "that":
                        self.file.write("@THAT\n")
                    case "this":
                        self.file.write("@THIS\n")
                    case "local":
                        self.file.write("@LCL\n")
                    case "argument":
                        self.file.write("@ARG\n")
                self.file.write("A=D+M\n")
                self.file.write("D=M\n")

            self.file.write("@SP\n")
            self.file.write("A=M\n")
            self.file.write("M=D\n")
            self.file.write("@SP\n")
            self.file.write("M=M+1\n")

        else:  # For 'pop' command
            if segment == "static":
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("D=M\n")
                self.file.write(f"@{self.file_name}.{index}\n")
                self.file.write("M=D\n")
            else:  # pointer / temp / that / local / local / argument
                self.file.write(f"@{index}\n")
                self.file.write("D=A\n")
                if segment == "pointer":
                    self.file.write("@3\n")
                    self.file.write("D=D+A\n")
                elif segment == "temp":
                    self.file.write("@5\n")
                    self.file.write("D=D+A\n")
                else:  # that / local / local / argument
                    match segment:
                        case "that":
                            self.file.write("@THAT\n")
                        case "this":
                            self.file.write("@THIS\n")
                        case "local":
                            self.file.write("@LCL\n")
                        case "argument":
                            self.file.write("@ARG\n")
                    self.file.write("D=D+M\n")

                self.file.write("@13\n")  # Free place in the stack
                self.file.write("M=D\n")
                self.file.write("@SP\n")
                self.file.write("A=M-1\n")
                self.file.write("D=M\n")
                self.file.write("@13\n")
                self.file.write("A=M\n")
                self.file.write("M=D\n")
            # SP--
            self.file.write("@SP\n")
            self.file.write("M=M-1\n")
