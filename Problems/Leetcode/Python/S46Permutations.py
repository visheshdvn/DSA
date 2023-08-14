from itertools import permutations


def permute(nums):
    if len(nums) == 1:
        return [[nums[0]]]

    permutations = [[nums[0]]]

    for i in range(1, len(nums)):
        new_lists = []
        for j in permutations:
            element = j[:]
            for k in range(0, len(j)+1):
                element.insert(k, nums[i])
                new_lists.append(element[:])
                element = j[:]

        permutations = new_lists[:]

    print(permutations)


nums = [int(i) for i in input().split()]
permute(nums)
