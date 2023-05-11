from collections import deque
class Node:
    def __init__(self, val) -> None:
        self.val=val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    
    def append(self, value)->None:
        if self.head is None:
            self.head = Node(value)
            self.length+=1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next=Node(value)
            self.length+=1
            
    def show(self)->None:
        """Displays the linked list, without trailing EOL charachter"""
        curr = self.head
        while curr is not None:
            print(curr.val, end="=>")
            curr = curr.next
        print() 
        

    def rotate(self, k: int)-> None:
        curr  = self.head
        if self.head is None:
            return
        arr = deque()
        while curr is not None:
            arr.append(curr.val)
            curr=curr.next
        k%=len(arr)
        for i in range(k):
            temp=arr.pop()
            arr.appendleft(temp)
        t=0
        # everything is correct
        curr=self.head
        while curr is not None:
            curr.val=arr[t]
            curr=curr.next
            t+=1
    def reverse(self)->None:
        curr= self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev =curr
            curr = next
        self.head = prev
    
    def __len__(self):
        return self.length
    

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.show()
list1.reverse()
list1.show()
print(len(list1))