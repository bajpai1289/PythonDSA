nums = [1,0,1,0,1]
goal = 2
count=0
n=len(nums)
for i in range(n):
    for j in range(i+1,n+1):
        if sum(nums[i:j])==goal:
            print(nums[i:j])
            count+=1

print(count)
