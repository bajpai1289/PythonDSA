class ArrayImplementation:
    def __init__(self, val) -> None:
        self.arr=[None]*val
    
    def push(self, val):
        n=len(self.arr)
        if self.arr[-1] is not None:
            newArr=[None]*(n*2)
            for i in range(n):
                newArr[i]=self.arr[i]
            self.arr=newArr
            start=0
            while self.arr[start] is not None:
                start+=1
            self.arr[start]=val

        else:
            start=0
            while self.arr[start] is not None:
                start+=1
            self.arr[start]=val
    
    def display(self):
        start=0
        while self.arr[start] is not None:
            print(self.arr[start], end=", ")
            start+=1
        print()



vector = ArrayImplementation(5)
vector.push(1)
vector.push(2)
vector.push(3)
vector.display()
vector.push(4)
vector.push(5)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)
vector.push(6)

vector.display()
        
