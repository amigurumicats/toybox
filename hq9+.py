import sys

class HQ9p:
    def __init__(self):
        self._src: str = ""
        self._count: int = 0

    def run(self, src_code):
        self._src = src_code
        for c in src_code:
            if c == "H":
                print("Hello, World!")
            elif c == "Q":
                print(src_code, end="")
            elif c == "9":
                self._bottles()
            elif c == "+":
                self._count += 1

    @staticmethod
    def _bottles():
        for i in range(99, -1, -1):
            if i == 2:
                print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
                print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
            elif i == 1:
                print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
                print(f"Take one down and pass it around, no more bottles of beer on the wall.")
            elif i == 0:
                print(f"No more bottles of beer on the wall, no more bottles of beer.")
                print(f"Go to the store and buy some more, 99 bottles of beer on the wall.")
            else:
                print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
                print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
            print()


if __name__ == "__main__":
    hq9p = HQ9p()
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as f:
            hq9p.run(f.read())
    else:
        hq9p.run(sys.stdin.read())

