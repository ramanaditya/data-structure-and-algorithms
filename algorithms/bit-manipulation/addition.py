import sys


class Addition:
    def addition(self, a, b):
        if not a:
            return b
        else:
            return self.addition((a & b) << 1, a ^ b)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a, b = data[:]
    print("a : {} - bin : {}".format(a, bin(a)[2:]))
    print("b : {} - bin : {}".format(b, bin(b)[2:]))
    bin_res = Addition().addition(a, b)
    print("Arithmetic Addition\t : {} and bin : {}".format(a + b, bin(a + b)[2:]))
    print("Binary Addition\t\t : {} and bin : {}".format(bin_res, bin(bin_res)[2:]))
