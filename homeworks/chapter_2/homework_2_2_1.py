def summation(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = (-arr[i])*2
    return sum(arr)/max(arr)


N = int(input())
summation(list(map(int, input().split())))
