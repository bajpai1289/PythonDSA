from random import randint
from collections import defaultdict
class RandomizedCollection:
    def __init__(self):
        self.d=defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            self.d[val].append(len(self.array))
            self.array.append(val)
            print('added element false')
            return False

        else:
            self.d[val]=[len(self.array)]
            self.array.append(val)
            print('added element True')
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d:
            print('removed element False')
            return False
        else:
            temp=self.d[val].pop()
            self.array.pop(temp)
            if  len(self.d[val])==0:
                del self.d[val]
            print(f'removel element {temp} True')
            return True

    def getRandom(self) -> int:
        start=0
        end = len(self.array)-1
        randomNum=randint(start, end)
        return self.array[randomNum]
    
    def __repr__(self) -> str:
        return f"Dictionary: {self.d},\nArray: {self.array}"

    def __str__(self) -> str:
        return self.__repr__()


obj1=RandomizedCollection()
print(obj1)
obj1.insert(0)
obj1.insert(1)
print(obj1)
obj1.remove(0)
print(obj1)
obj1.insert(2)
print(obj1)
obj1.remove(1)
print(obj1)
print(obj1.getRandom())
