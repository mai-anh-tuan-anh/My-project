def longest_max_subarray(arr):
    max_val = max(arr)
    max_length = 0
    current_length = 0
    for i in range(len(arr)):
        if arr[i] == max_val:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    if current_length > max_length:
        max_length = current_length
    return max_length
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(longest_max_subarray(a))