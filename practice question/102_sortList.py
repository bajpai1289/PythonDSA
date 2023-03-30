class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr= self.head
            while curr.next is not None:
                curr= curr.next
            curr.next = Node(val)

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end="=>")
            curr=curr.next
    
    def sort(self):
        curr= self.head
        tmp = []
        while curr is not None:
            tmp.append(curr.val)
            curr=curr.next
        # print(tmp)
        tmp.sort()
        curr= self.head
        i=0
        while curr is not None:
            curr.val=tmp[i]
            curr=curr.next
            i+=1
        

list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)
list1.append(3)
list1.append(2)
list1.append(1)
list1.sort()
list1.show()