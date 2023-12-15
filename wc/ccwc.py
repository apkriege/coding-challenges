import sys


class Wc:
    def __init__(self, filename):
        self.filename = filename
        self.chars = 0
        self.words = 0
        self.lines = 0
        self.bytes = 0

        self.read_file()

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                self.lines += 1
                self.words += len(line.split())
                self.chars += len(line)
                self.bytes += len(line.encode("utf-8"))


def is_options_valid(options):
    valid_options = ["-c", "-l", "-w", "-m"]

    for option in options:
        if option not in valid_options:
            return False

    return True


def main():
    if not is_options_valid(sys.argv[2:]):
        print("argument does not exist")
        return

    x = Wc(sys.argv[1])

    ret = ""
    for arg in sys.argv[2:]:
        if arg == "-c":
            ret += str(x.chars)
        if arg == "-w":
            ret += str(x.words)
        if arg == "-l":
            ret += str(x.lines)
        if arg == "-m":
            ret += str(x.bytes)

        ret += " "

    print(ret)


if __name__ == "__main__":
    main()
