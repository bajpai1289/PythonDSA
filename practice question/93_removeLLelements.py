class Node:
    def __init__(self, val) -> None:
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self, defualtList=[]) -> None:
        self.head=None

    def append(self, val):
        if self.head is None:
            self.head=Node(val)
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=Node(val)
    
    def show(self):
        curr= self.head
        while curr:
            print(curr.val, end="=>")
            curr=curr.next

    def removeElements(self, val: int):
        
            prev=None
            curr=self.head
            while curr:
                if curr.val==val:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head=curr.next
                    curr=curr.next
                else:
                    prev=curr
                    curr=curr.next

        #removal at the last:
    
    def swap(self):
        curr= self.head
        next = curr.next
        while curr and next:
            curr.val , next.val = next.val, curr.val
            next=next.next
            curr=curr.next
        

        


list1=LinkedList()
# list1.show()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.show()
print()
list1.swap()
list1.show()