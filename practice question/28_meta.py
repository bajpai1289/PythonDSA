from random import randint
class Meta:
    def __init__(self) -> None:
        self.data=set()
        
    def addValue(self, value):
        self.data.add(value)
        
    def removeValue(self, value):
        if value not in self.data:
            print("Value not present in the data")
            return
        else:
            self.data.remove(value)
    
    def generateRandom(self):
        n=len(self.data)
        ul=randint(0,n-1)
        print(list(self.data)[ul])
    
    def __repr__(self) -> str:
        return ", ".join([str(i) for i in self.data])
    def __str__(self) -> str:
        return self.__repr__()
    
val=Meta()
val.addValue(1)
val.addValue(1)
val.addValue(2)
val.addValue(3)
val.addValue(3)
val.addValue(4)
print(val)

val.removeValue(1)
print(val)
        
val.generateRandom()