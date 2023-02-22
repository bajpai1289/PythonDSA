def shipWithinDays(weights: list[int], days: int) -> int:
    #checking weather the packages can be shipped in less than "days" days with "c" capacity
    def bSearch(weights, c, days):
        daysNeeded, currentLoad=1,0
        for w in weights:
            currentLoad+=w
            if currentLoad>c:
                daysNeeded+=1
                currentLoad=w
        return daysNeeded<=days
    totalLoad, maxLoad=0,0
    for w in weights:
        totalLoad+=w
        maxLoad=max(maxLoad, w)
    l=maxLoad
    r=totalLoad
    while l<r:
        mid=(l+r)//2
        if bSearch(weights, mid, days):
            r=mid
        else:
            l=mid+1
    return l






print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(shipWithinDays([3,2,2,4,1,4], 3))
print(shipWithinDays([1,2,3,1,1],4 ))