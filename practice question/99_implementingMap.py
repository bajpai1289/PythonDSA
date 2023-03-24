class List:
    def __init__(self, arr) -> None:
        self.arr=arr


    def myMap(self, callback):
        newArr=[]
        for i in self.arr:
            newArr.append(callback(i))
        return newArr
    

l=List([2,4,6,8,10])
a=l.myMap(lambda x:x**2)
print(a)

a=[*map(lambda a: a**2,( [2,4,6,1,3,5]))]

b=list(2,3,4,5)
print(b)

print(a)
