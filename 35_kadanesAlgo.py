def kadane(arr: list[int]):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current=max(max_current, max_current+arr[i])
        if max_current>max_global:
            max_global=max_current
    return max_global

print(kadane([-2,3,2,-1]))