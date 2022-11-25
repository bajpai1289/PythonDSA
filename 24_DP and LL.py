class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head=head
    
    def append(self, value):
        if self.head==None:
            self.head=ListNode(value)
        else:
            currentNode=self.head
            while currentNode.next is not None:
                currentNode=currentNode.next
            currentNode.next=ListNode(value)

    def showElement(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.val)
            currentNode=currentNode.next

    def reverseLinkedList(self):
        if self.head==None:
            return

        prev = None
        current= self.head
        while current is not None:
            next_node= current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

list1=LinkedList()
list1.append(2)
list1.append(4)
list1.append(3)
list1.showElement()

print()
list1.reverseLinkedList()
list1.showElement()
 