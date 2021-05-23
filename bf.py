import sys
from typing import List, NamedTuple


class CharPos(NamedTuple):
    char: str
    pos: int


class BFException(Exception):
    # 基底クラス
    pass

class BFInvalidPointer(BFException):
    # ポインタがメモリからはみだした
    def __init__(self, pos):
        self._pos: int = pos

    def __str__(self):
        return f"Invalid pointer: {self._pos}"

class BFSyntaxError(BFException):
    # 対応する[や]が見つからなかった
    def __init__(self, pos):
        self._pos: int = pos

    def __str__(self):
        return f"Syntax error: {self._pos}"

class BFValueError(BFException):
    # メモリの値が0より小さいまたは255より大きくなった
    def __init__(self, pos):
        self._pos: int = pos

    def __str__(self):
        return f"Value error: {self._pos}"


class BF:
    def __init__(self):
        self._MEM_MAX_SIZE = 10000
        self._mem = [0] * 100
        self._pointer = 0  # メモリのポインタ
        self._pc = 0  # プログラムカウンタ

    def run(self, src_code):
        _src_code: List[CharPos] = self._compress_code(src_code)
        while 0 <= self._pc < len(_src_code):
            now_command, now_pos = _src_code[self._pc]
            if now_command == "+":
                if self._mem[self._pointer] >= 255:
                    raise BFValueError(pos=now_pos)
                self._mem[self._pointer] += 1
            elif now_command == "-":
                if self._mem[self._pointer] <= 0:
                    raise BFValueError(pos=now_pos)
                self._mem[self._pointer] -= 1
            elif now_command == ">":
                self._pointer += 1
                if self._pointer >= len(self._mem):
                    raise BFInvalidPointer(pos=now_pos)
            elif now_command == "<":
                self._pointer -= 1
                if self._pointer < 0:
                    raise BFInvalidPointer(pos=now_pos)
            elif now_command == "[":
                if self._mem[self._pointer] == 0:
                    depth = 1
                    while depth:
                        self._pc += 1
                        if not(0 <= self._pc <= len(_src_code)):
                            raise BFSyntaxError(pos=now_pos)
                        next_command, _ = _src_code[self._pc]
                        if next_command == "[":
                            depth += 1
                        elif next_command == "]":
                            depth -= 1
                        if depth == 0: break
            elif now_command == "]":
                if self._mem[self._pointer] != 0:
                    depth = 1
                    while depth:
                        self._pc -= 1
                        if not(0 <= self._pc <= len(_src_code)):
                            raise BFSyntaxError(pos=now_pos)
                        next_command, _ = _src_code[self._pc]
                        if next_command == "[":
                            depth -= 1
                        elif next_command == "]":
                            depth += 1
                        if depth == 0: break
            elif now_command == ".":
                print(chr(self._mem[self._pointer]), end="")
            elif now_command == ",":
                self._mem[self._pointer] = ord(sys.stdin.read(1))
            self._pc += 1

    @staticmethod
    def _compress_code(raw_code: str) -> List[CharPos]:
        return [CharPos(c, i) for i, c in enumerate(raw_code) if c in "+-><[].,"]


if __name__ == "__main__":
    bf = BF()
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as f:
            bf.run(f.read())
    else:
        bf.run(sys.stdin.read())
