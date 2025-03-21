def is_palindrome(s):
    return s == s[::-1]
def convert_base(x, base):
    if x == 0:
        return "0"
    res = ""
    while x > 0:
        remainder = x % base
        if remainder >= 10:
            res = chr(remainder - 10 + ord('A')) + res
        else:
            res = str(remainder) + res
        x //= base
    return res
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    for line in data:
        arr = line.split()
        x = int(arr[0])
        if x == -1:
            break
        a, b = map(int, arr[1:3])
        res_a = convert_base(x, a)
        res_b = convert_base(x, b)
        print('YES' if (is_palindrome(res_a) and is_palindrome(res_b)) else 'NO',end=' ')