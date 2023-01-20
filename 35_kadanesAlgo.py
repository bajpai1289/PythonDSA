# def kadane(arr: list[int]):
#     max_current = max_global = arr[0]
#     for i in range(1, len(arr)):
#         max_current=max(max_current, max_current+arr[i])
#         if max_current>max_global:
#             max_global=max_current
#     return max_global

# print(kadane([-2,3,2,-1]))

arr = [0,1,1,0,0,0,1,1,0,1,0]
i = 0
j = len(arr) - 1
while i < j:
    if arr[i] == 1:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            j -= 1
    else:
        i += 1
print(arr)

