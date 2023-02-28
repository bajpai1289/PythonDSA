from locale import currency


class heap:
    def __init__(self) -> None:
        self.heap=[0]
    
    def push(self, val):
        self.heap.append(val)
        i=len(self.heap)-1
        #percolate up
        while self.heap[i]<self.heap[i//2]:
            self.heap[i], self.heap[i//2]=self.heap[i//2], self.heap[i]
            i//=2
        
    def pop(self):
        if len(self.heap)==1:
            return None
        if len(self.heap)==2:
            return self.heap.pop()

        res=self.heap[1]
        #move last value to the root
        self.heap[1]=self.heap.pop()
        i=1
        #percolate down
        while 2*i<len(self.heap):
            if(2*i+1<len(self.heap) and self.heap[2*i+1]<self.heap[2*i] and self.heap[i]>self.heap[2*i+1]):
                #swap the right child
                self.heap[i], self.heap[2*i+1]=self.heap[2*i+1], self.heap[i]
                i=2*i+1
            elif self.heap[i]>self.heap[2*i]:
                self.heap[i], self.heap[2*i]=self.heap[2*i], self.heap[i]
                i=2*i
            else:
                break
        return res
    
    def heapify(self, arr:'list[int]'):
        #oth position is first move towards the end
        arr.append(arr[0])
        self.heap=arr
        cur=(len(self.heap)-1)//2
        while cur>0:
            #percolate down
            i=cur
            while 2*i<len(self.heap):
                if(2*i+1<len(self.heap) and self.heap[2*i+1]<self.heap[2*i] and self.heap[i]>self.heap[2*i+1]):
                    self.heap[i], self.heap[2*i+1]=self.heap[2*i+1], self.heap[i]
                    i=2*i+1
                elif self.heap[i]>self.heap[2*i]:
                    self.heap[i], self.heap[2*i]=self.heap[2*i],self.heap[i]
                    i=2*i
                else:
                    break
            cur-=1
        
            
        
    

        