import sys
def generate_diagonal_matrix(n):
    for i in range(n):
        sys.stdout.write(" ".join(str(abs(i - j)) for j in range(n)) + "\n")
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    generate_diagonal_matrix(n)