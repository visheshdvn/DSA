# can hve repeated elements

def nextGreaterElement(arr, n):
    stack = []
    ret_list = [-1]*n

    for i in range(n):
        curr = arr[i]
        while stack and stack[-1]["val"] < curr:
            ret_list[stack[-1]["ind"]] = curr
            stack.pop()

        stack.append({"val": curr, "ind": i})

    return ret_list


arr = [int(i) for i in input().split()]

lst = nextGreaterElement(arr, len(arr))
print(lst)
