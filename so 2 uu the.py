from collections import deque
def sinh():
    queue = deque(["1","2"])
    valid_numbers = []
    while len(valid_numbers) < 1000:
        num = queue.popleft()
        if num.count('2') > len(num) // 2:
            valid_numbers.append(int(num))
        if len(num) < 10:
            queue.append(num + "0")
            queue.append(num + "1")
            queue.append(num + "2")
    return sorted(valid_numbers)
if __name__=='__main__':
    a=sinh()
    for t in range(int(input())):
        for i in range(int(input())):
            print(a[i],end=' ')
        print()