from random import randint
class Google:
    def __init__(self) -> None:
        self.data= set()
    
    def append(self, value):
        self.data.add(value)

    def removeItem(self, value):
        if value in self.data:
            print(value, 'removed')
            self.data.remove(value)
        else:
            print('no value found')
            return

    def getRandom(self):
        items= list(self.data)
        index= randint(0, len(items)-1)
        print(items[index])
        return
    
    def __repr__(self) -> str:
        return ", ".join([str(i) for i in self.data])

    def __str__(self) -> str:
        return self.__repr__()


items=Google()
items.append(10)
items.append(20)
items.append(20)
items.append(30)
items.append(40)
items.append(50)
items.append(50)
print(items)

items.removeItem(30)
items.removeItem(9)

print(items)

items.getRandom()


