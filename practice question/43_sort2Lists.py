def sortPeople(names: 'list[str]', heights: 'list[int]'):
    return [n for h,n in sorted(zip(heights, names),reverse=True)]

print(sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))
print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))

