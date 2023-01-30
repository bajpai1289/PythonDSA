def sortColors(arr: list[int]) -> None:
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

from sys import getsizeof

n=(0,)
arr=(1,2,3,4,5)
print(type(n))
# when you were here before
# couldnt look you in the eye
# you're just like an angel 
# your skin makes me cry 
# you float like a feather 
# in a beutiful world
# you're so fucking special
# i wish i was special
# but ima creep 
# ima wiedro 
# what the hell im doing here
# i dont belong here
# i dont care if it hurts
# i wanna have control
# i wanta a perfect body
# i want a perfect soul
# i want you to notice
# when i'm not around
# so fucking special 
# i wish i wa