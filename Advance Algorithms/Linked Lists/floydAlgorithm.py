'find the middle of the linked list'
class Node:
    def __init__(self, val) -> None:
        self.val=val
        self.next=None
    def __repr__(self) -> str:
        return f"({self.val})"
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self, val):
        if self.head is None:
            self.head=Node(val)
        else:
            curr =self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=Node(val)
    
    def getMiddle(self):
        slow, fast=self.head, self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.val,  end="=>")
            curr=curr.next
    def hasCycle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

    def cycleStart(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next:
            return None
        slow2=self.head
        while slow!=slow2:
            slow=slow.next
            slow2=slow2.next
        return slow
     
    def __repr__(self) -> str:
        str1=""
        curr=self.head
        while curr is not None:
            str1+=str(curr.val)
            curr=curr.next
            str1+="=>"
        print(str1)
        return 
    def __str__(self) -> str:
        return self.__repr__()
    

ll=LinkedList()
ll.append(1) 
ll.head.next=Node(2)
ll.head.next.next=Node(3)
ll.head.next.next.next=Node(4)
ll.head.next.next.next.next=Node(5)
ll.head.next.next.next.next.next=ll.head.next
# ll.display()
print(ll.cycleStart())