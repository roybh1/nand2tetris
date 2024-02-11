from JackTokenizer import JackTokenizer


class CompilationEngine:
    def __init__(self, input_file, output_file):
        self._tokenizer = JackTokenizer(input_file)
        self._output = open(output_file, "w+")
        self._indentation = 0

    def compile_class(self):
        if self._tokenizer.has_more_tokens():
            self._tokenizer.advance()  # new class
            self._output.write("<class>\n")
            self._indentation += 1

            self.write_keyword()  # class
            self._tokenizer.advance()

            self.write_identifier()  # className
            self._tokenizer.advance()

            self.write_symbol()  # {
            self._tokenizer.advance()

            while self._tokenizer.key_word() == "static" or self._tokenizer.key_word() == "field":  # classVarDec*
                self.compile_class_var_dec()

            while self._tokenizer.key_word() == "constructor" or self._tokenizer.key_word() == "function" or \
                    self._tokenizer.key_word() == "method":  # subroutine Dec
                self.compile_subroutine()

            self.write_symbol()  # }

            self._indentation -= 1
            self._output.write("</class>\n")
            self._output.close()

    def compile_class_var_dec(self):
        self._output.write("  " * self._indentation + "<classVarDec>\n")
        self._indentation += 1

        self.write_keyword()  # ('static'|'field')
        self._tokenizer.advance()

        self.compile_type_and_var_name()  # type

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</classVarDec>\n")

    def compile_type_and_var_name(self):
        # 'int' | 'char'| 'boolean'| className
        if self._tokenizer.token_type() == "KEYWORD":  # void / int / char / boolean
            self.write_keyword()
        elif self._tokenizer.token_type() == "IDENTIFIER":  # className
            self.write_identifier()
        self._tokenizer.advance()

        # varName (',' varName)*';'
        self.write_identifier()  # varName
        self._tokenizer.advance()

        while self._tokenizer.symbol() == ",":
            self.write_symbol()  # ,
            self._tokenizer.advance()
            self.write_identifier()  # identifier
            self._tokenizer.advance()

        self.write_symbol()  # ;
        self._tokenizer.advance()

    def compile_subroutine(self):  # include compile_subroutine_body -  the only place we are using subroutine_body
        self._output.write("  " * self._indentation + "<subroutineDec>\n")
        self._indentation += 1

        self.write_keyword()  # ('constructor'|'function' |method')
        self._tokenizer.advance()

        # (void | type)
        if self._tokenizer.token_type() == "KEYWORD":  # void / int / char / boolean
            self.write_keyword()
        elif self._tokenizer.token_type() == "IDENTIFIER":  # className
            self.write_identifier()
        self._tokenizer.advance()

        self.write_identifier()  # subroutineName: identifier
        self._tokenizer.advance()

        self.write_symbol()  # (
        self._tokenizer.advance()

        self.compile_parameter_list()  # parameterList

        self.write_symbol()  # )
        self._tokenizer.advance()

        self._output.write("  " * self._indentation + "<subroutineBody>\n")
        self._indentation += 1

        self.write_symbol()  # {
        self._tokenizer.advance()

        while self._tokenizer.key_word() == "var":  # varDec*
            self.compile_var_dec()

        self.compile_statements()  # statements

        self.write_symbol()  # }
        self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</subroutineBody>\n")
        self._indentation -= 1
        self._output.write("  " * self._indentation + "</subroutineDec>\n")

    def compile_parameter_list(self):
        self._output.write("  " * self._indentation + "<parameterList>\n")
        self._indentation += 1
        # (type varName)
        while self._tokenizer.token_type() != "SYMBOL":
            if self._tokenizer.token_type() == "KEYWORD":  # 'int' | 'char'| 'boolean'
                self.write_keyword()
            elif self._tokenizer.token_type() == "IDENTIFIER":  # className
                self.write_identifier()
            self._tokenizer.advance()

            self.write_identifier()  # varName
            self._tokenizer.advance()

            if self._tokenizer.symbol() == ",":  # ,
                self.write_symbol()
                self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</parameterList>\n")

    def compile_var_dec(self):
        self._output.write("  " * self._indentation + "<varDec>\n")
        self._indentation += 1

        self.write_keyword()  # var
        self._tokenizer.advance()

        self.compile_type_and_var_name()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</varDec>\n")

    def compile_statements(self):
        self._output.write("  " * self._indentation + "<statements>\n")
        self._indentation += 1

        while self._tokenizer.token_type() == "KEYWORD":
            if self._tokenizer.key_word() == "let":
                self.compile_let()
            elif self._tokenizer.key_word() == "if":
                self.compile_if()
            elif self._tokenizer.key_word() == "while":
                self.compile_while()
            elif self._tokenizer.key_word() == "do":
                self.compile_do()
            elif self._tokenizer.key_word() == "return":
                self.compile_return()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</statements>\n")

    def compile_let(self):
        self._output.write("  " * self._indentation + "<letStatement>\n")
        self._indentation += 1

        self.write_keyword()  # let
        self._tokenizer.advance()

        self.write_identifier()  # varName
        self._tokenizer.advance()

        # ([expression])?
        if self._tokenizer.symbol() == "[":
            self.write_symbol()  # [
            self._tokenizer.advance()
            self.compile_expression()  # expression
            self.write_symbol()  # ]
            self._tokenizer.advance()

        self.write_symbol()  # =
        self._tokenizer.advance()

        self.compile_expression()  # expression

        self.write_symbol()  # ;
        self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</letStatement>\n")

    def compile_if(self):
        self._output.write("  " * self._indentation + "<ifStatement>\n")
        self._indentation += 1

        self.write_keyword()  # if
        self._tokenizer.advance()

        self.write_symbol()  # (
        self._tokenizer.advance()

        self.compile_expression()  # expression

        self.write_symbol()  # )
        self._tokenizer.advance()

        self.write_symbol()  # {
        self._tokenizer.advance()

        self.compile_statements()  # statement

        self.write_symbol()  # }
        self._tokenizer.advance()

        if self._tokenizer.key_word() == "else" and self._tokenizer.token_type() == "KEYWORD":
            self.write_keyword()  # else
            self._tokenizer.advance()

            self.write_symbol()  # {
            self._tokenizer.advance()

            self.compile_statements()  # statement

            self.write_symbol()  # }
            self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</ifStatement>\n")

    def compile_while(self):
        self._output.write("  " * self._indentation + "<whileStatement>\n")
        self._indentation += 1

        self.write_keyword()  # while
        self._tokenizer.advance()

        self.write_symbol()  # (
        self._tokenizer.advance()

        self.compile_expression()  # expression

        self.write_symbol()  # )
        self._tokenizer.advance()

        self.write_symbol()  # {
        self._tokenizer.advance()

        self.compile_statements()  # statement

        self.write_symbol()  # }
        self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</whileStatement>\n")

    def compile_do(self):
        self._output.write("  " * self._indentation + "<doStatement>\n")
        self._indentation += 1

        self.write_keyword()  # do
        self._tokenizer.advance()

        self.write_identifier()  # identifier
        self._tokenizer.advance()

        if self._tokenizer.symbol() == ".":
            self.write_symbol()  # .
            self._tokenizer.advance()
            self.write_identifier()  # identifier
            self._tokenizer.advance()

        self.write_symbol()  # (
        self._tokenizer.advance()

        self.compile_expression_list()

        self.write_symbol()  # )
        self._tokenizer.advance()

        self.write_symbol()  # ;
        self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</doStatement>\n")

    def compile_return(self):
        self._output.write("  " * self._indentation + "<returnStatement>\n")
        self._indentation += 1

        self.write_keyword()  # return
        self._tokenizer.advance()

        if self._tokenizer.token_type() != "SYMBOL" and self._tokenizer.symbol() != ";":
            self.compile_expression()  # expression

        self.write_symbol()  # ;
        self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</returnStatement>\n")

    def compile_expression(self):
        self._output.write("  " * self._indentation + "<expression>\n")
        self._indentation += 1

        self.compile_term()  # term

        while self._tokenizer.token_type() == "SYMBOL" and self._tokenizer.symbol() in ["+", "-", "*", "/", "&", "|",
                                                                                        "<", ">", "="]:
            self.write_symbol()
            self._tokenizer.advance()

            self.compile_term()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</expression>\n")

    def compile_term(self):
        check = True
        self._output.write("  " * self._indentation + "<term>\n")
        self._indentation += 1

        if self._tokenizer.token_type() == "INT_CONST":  # integerConstant
            self.write_integer_constant()
        elif self._tokenizer.token_type() == "STRING_CONST":  # stringConstant
            self.write_string_constant()
        elif self._tokenizer.token_type() == "KEYWORD":  # keywordConstant
            self.write_keyword()
        elif self._tokenizer.token_type() == "IDENTIFIER":  # varName
            self.write_identifier()
            self._tokenizer.advance()
            check = False

            # subroutineCall
            if self._tokenizer.symbol() == "[":
                check = True
                self.write_symbol()
                self._tokenizer.advance()
                self.compile_expression()
                self.write_symbol()

            elif self._tokenizer.symbol() == ".":
                check = True
                self.write_symbol()
                self._tokenizer.advance()
                self.write_identifier()
                self._tokenizer.advance()
                self.write_symbol()
                self._tokenizer.advance()
                self.compile_expression_list()
                self.write_symbol()

            elif self._tokenizer.symbol() == "(":
                check = True
                self.write_symbol()
                self._tokenizer.advance()
                self.compile_expression_list()
                self.write_symbol()

        elif self._tokenizer.symbol() == "(":
            self.write_symbol()
            self._tokenizer.advance()
            self.compile_expression()
            self.write_symbol()

        elif self._tokenizer.symbol() == "~" or self._tokenizer.symbol() == "-":  # unaryOp term
            self.write_symbol()
            self._tokenizer.advance()
            self.compile_term()
            check = False

        if check:
            self._tokenizer.advance()

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</term>\n")

    def compile_expression_list(self):
        self._output.write("  " * self._indentation + "<expressionList>\n")
        self._indentation += 1

        if self._tokenizer.token_type() != "SYMBOL" and self._tokenizer.symbol() != ")":
            self.compile_expression()  # expression

            while self._tokenizer.token_type() == "SYMBOL" and self._tokenizer.symbol() == ",":
                self.write_symbol()  # ,
                self._tokenizer.advance()
                self.compile_expression()  # expression

        if self._tokenizer.symbol() == "(":
            self.compile_expression()  # expression
            while self._tokenizer.token_type() == "SYMBOL" and self._tokenizer.symbol() == ",":
                self.write_symbol()  # ,
                self._tokenizer.advance()
                self.compile_expression()  # expression

        self._indentation -= 1
        self._output.write("  " * self._indentation + "</expressionList>\n")

    def write_keyword(self):
        self._output.write("  " * self._indentation + "<keyword> " + self._tokenizer.key_word() + " </keyword>\n")

    def write_symbol(self):
        token = self._tokenizer.symbol()
        if token == "<":
            token = "&lt;"
        elif token == ">":
            token = "&gt;"
        elif token == "&":
            token = "&amp;"
        elif token == '"':
            token = "&quot;"
        self._output.write("  " * self._indentation + "<symbol> " + token + " </symbol>\n")

    def write_integer_constant(self):
        self._output.write(
            "  " * self._indentation + "<integerConstant> " + self._tokenizer.identifier() + " </integerConstant>\n")

    def write_string_constant(self):
        new_string = self._tokenizer.identifier().replace('"', '')
        self._output.write("  " * self._indentation + "<stringConstant> " +new_string +" </stringConstant>\n")

    def write_identifier(self):
        self._output.write(
            "  " * self._indentation + "<identifier> "  +self._tokenizer.identifier() + " </identifier>\n")
