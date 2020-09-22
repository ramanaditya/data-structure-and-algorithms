class Naive:
    def __init__(self, T, P):
        self.T = T
        self.P = P

    def search(self):
        print("Pattern Matching Started")
        t_start = 0
        t_length, p_length = len(self.T), len(self.P)
        while t_start <= t_length - p_length:
            if self.T[t_start : t_start + p_length] == self.P:
                print(f"Pattern Matched at index {t_start}")
            t_start += 1
        return


class RabinKarp:
    def __init__(self, T, P):
        self.T = T
        self.P = P

    def search(self,):
        pass


if __name__ == "__main__":
    print("=======================")
    print("Pattern Matching")
    print("=======================")
    s = input("Enter the String: ")
    p = input("Enter the pattern: ")
    while True:
        print("----------------------------------")
        print("1. Find Using Naive Method")
        print("2. Edit your String")
        print("3. Edit your Pattern")
        print("4. Exit")
        choice = int(input("Enter your Choice: "))
        print("----------------------------------")

        if choice == 1:
            naive = Naive(s, p)
            naive.search()
        elif choice == 2:
            s = input("Enter the String: ")
        elif choice == 3:
            p = input("Enter the pattern: ")
        elif choice == 4:
            print("Exiting...")
            exit(0)
