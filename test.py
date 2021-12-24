arr = [5, 6, 7, 8, 9, 10]
divisor = 5


def solution(arr, divisor):
    arr.sort()
    for i in arr[:]:
        if i % divisor == 0:
            continue
        else:
            arr.remove(i)
    if not arr:
        return [-1]
    return arr


# print(solution(arr, divisor))

print(id(arr))
print(id(arr[:]))
