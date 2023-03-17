class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
class TreeNode:
    def __init__(self, val) -> None:
        self.val=val
        self.left = None
        self.right =None
        
class linkedList:
    def __init__(self) -> None:
        self.head=None
    
    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr=curr.next
            curr.next = ListNode(value)
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end="=>")
            curr=curr.next
    def sortedListToBST(self):
        pass
    
    
    
    
    
    
list1=linkedList()
list1.append(-10)
list1.append(-3)
list1.append(0)
list1.append(5)
list1.append(9)
list1.display()