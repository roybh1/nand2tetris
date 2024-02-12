from hack_assembler.enums import COMP_TO_BINARY, DEST_TO_BINRAY, JUMP_TO_BINARY


class Code:
    @staticmethod
    def get_binary_dest(dest: str | None) -> str:
        return DEST_TO_BINRAY[dest]

    @staticmethod
    def get_binary_comp(comp: str) -> str:
        return COMP_TO_BINARY[comp]

    @staticmethod
    def get_binary_jump(jump: str | None) -> str:
        return JUMP_TO_BINARY[jump]
