def frequency(arr):
    f = {}
    for i in arr:
        f[i] = f.get(i, 0) + 1

    for k, v in f.items():
        print(k, v)


arr = [int(i) for i in input().split()]
frequency(arr)
