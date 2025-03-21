def digit_sum(x):
    return sum(int(d) for d in str(x))
def count(n, h):
    return sum(1 for i in range(n) if digit_sum(i) == h)
def main():
    while True:
        try:
            line = input().strip()
            if line == "-1":
                break
            n, h = map(int, line.split())
            print(count(n, h))
        except EOFError:
            break
if __name__ == "__main__":
    main()