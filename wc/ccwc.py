import sys


class Wc:
    def __init__(self, args):
        self.args = args
        self.chars = 0
        self.words = 0
        self.lines = 0
        self.bytes = 0

        self.read_file()

    def read_file(self):
        with open(self.args, "r", encoding="utf-8") as file:
            for line in file:
                self.lines += 1
                self.words += len(line.split())
                self.chars += len(line)
                self.bytes += len(line.encode("utf-8"))

            # f = file.read()

            # for i, l in enumerate(f):
            #     if l == "\n":
            #         self.lines += 1

            #     if l == " ":
            #         self.words += 1

            #     self.chars += 1
            #     self.bytes += len(l.encode("utf-8"))


def is_options_valid(options):
    valid_options = ["c", "l", "w", "m"]

    for option in options:
        if option not in valid_options:
            return False

    return True


def main():
    enum = {"c": "chars", "w": "words", "l": "lines", "m": "bytes"}
    if not is_options_valid(sys.argv[2:]):
        print("arg does not exist")
        return

    x = Wc(sys.argv[1])

    # ret = ""
    # for arg in sys.argv[2:]:
    #     ret += x.enum[arg] + " "

    # print(ret)
    # print(x.lines, x.words, x.chars, x.bytes)


if __name__ == "__main__":
    main()
