# leaders are the elements who have no element greater than them at their right side

def get_leaders(arr):
    n = len(arr)

    if (n == 0 or n == 1):
        return arr

    maxi = arr[-1]
    leaders = [maxi]

    for i in range(n-2, -1, -1):
        if arr[i] > maxi:
            maxi = arr[i]
            leaders.append(arr[i])

    return leaders


arr = [int(i) for i in input().split()]
a = get_leaders(arr)

print(*a[::-1])
