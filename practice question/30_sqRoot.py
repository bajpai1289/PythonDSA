def calculate(n: int):
    low =0
    high=n
    while low<=high:
        mid = (low+high)//2
        mid_sq=mid*mid
        if mid_sq==n:
            return mid
        elif mid_sq<n:
            low=mid+1
        elif mid_sq>n:
            high=mid-1
    return low-1, high
        
print(5, calculate(5))
print(16, calculate(16))
print(20, calculate(20))
print(64, calculate(64))
print(70, calculate(70))
print(256, calculate(256))
print("2**70", calculate(2**70))
print(125, calculate(125))
        


        