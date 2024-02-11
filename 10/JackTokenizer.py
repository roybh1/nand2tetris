import re

COMMENT = r"(//.*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)"


class JackTokenizer:
    KEYWORDS = ["class", "constructor", "function", "method", "field", "static",
                "var", "int", "char", "boolean", "void", "true", "false", "null",
                "this", "let", "do", "if", "else", "while", "return"]
    SYMBOLS = "{}()[].,;+-*/&|<>=~"

    def __init__(self, input_file):
        with open(input_file, "r") as file:
            self.input = file.read()
        self.remove_comments()
        self._tokens = self.tokenize()
        self._tokenIndex = 0
        self._currentToken = None
        self._tokenType = None

    def remove_comments(self):
        self.input = re.sub(COMMENT, "", self.input)

    def has_more_tokens(self) -> bool:
        return self._tokenIndex < len(self._tokens)

    def advance(self):
        if self.has_more_tokens():
            self._currentToken = self._tokens[self._tokenIndex]
            if self._currentToken in self.KEYWORDS:
                self._tokenType = "KEYWORD"
            elif self._currentToken in self.SYMBOLS:
                self._tokenType = "SYMBOL"
            elif self._currentToken.isdigit():
                self._tokenType = "INT_CONST"
            elif self._currentToken.startswith('"') and self._currentToken.endswith('"'):
                self._tokenType = "STRING_CONST"
            else:
                self._tokenType = "IDENTIFIER"
            self._tokenIndex += 1

    def token_type(self) -> str:
        return self._tokenType

    def current_token(self) -> str:  # for debugging
        return self._currentToken

    def key_word(self) -> str:
        return self._currentToken

    def symbol(self) -> str:
        return self._currentToken

    def identifier(self) -> str:
        return self._currentToken

    def int_val(self) -> int:
        return int(self._currentToken)

    def string_val(self) -> str:
        return self._currentToken

    def tokenize(self):
        tokens = []  # result tokens
        current_token = ""
        in_string = False  # flag
        in_comment = False  # flag

        for char in self.input:
            if in_comment:
                if char == "\n":  # finish comment
                    in_comment = False
                continue

            if char in self.SYMBOLS:
                if current_token:
                    tokens.append(current_token)
                tokens.append(char)
                current_token = ""

            elif char.isspace():
                if in_string:
                    current_token += char
                elif current_token:
                    tokens.append(current_token)
                    current_token = ""

            elif char == '"':
                if in_string:
                    in_string = False
                    tokens.append('"' + current_token + '"')
                    current_token = ""
                else:
                    in_string = True

            elif char == "/" and not in_string:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                current_token += char

                if current_token == "//":
                    in_comment = True
                    tokens.pop()  # remove the previous token
                    current_token = ""
            else:
                current_token += char  # build the token

        if current_token:
            tokens.append(current_token)

        return tokens
