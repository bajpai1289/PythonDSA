# class Node:
#     def __init__(self, value, next = None) -> None:
#         self.value = value
#         self.next = next

    
# class LinkedList:
#     def __init__(self, head =None) -> None:
#         self.head = head

#     def append(self, value):
#         if self.head == None:
#             self.head=Node(value)
        
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node=current_node.next
#             current_node.next=Node(value)

#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.value)
#             current=current.next

#     def rerverse(self):
#         prev = None
#         current = self.head
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev=current
#             current = next
#         self.head=prev



# list1 = LinkedList()
# list1.append(1)
# list1.append(2)
# list1.append(3)
# list1.append(5)
# list1.rerverse()
# list1.display()

class Node:
    def __init__(self, value) -> None:
        self.value= value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.size=0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size+=1
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next=Node(value)
            self.size+=1
    def __len__(self):
        return self.size
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.value,end="=>")
            curr=curr.next
    
    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            next= curr.next
            curr.next = prev
            prev= curr
            curr=next
        self.head=prev
    
    def insertAt(self, value, pos):
        if pos>self.size:
            raise IndexError('invalid position')

        #if user want to insert at first
        curr= self.head
        if pos==0:
            self.head=Node(value)
            self.head.next=curr
            self.size+=1
        #if user wants to insert at last
        elif pos==self.size:
            if self.head is None:
                self.head = Node(value)
                self.size+=1
            else:
                current=self.head
                while current.next is not None:
                    current = current.next
                current.next=Node(value)
                self.size+=1
        
        #if the insertion at anywhere in the middle
        else:
            curr=self.head
            currCount=0
            while currCount<pos-1:
                currCount+=1
                curr=curr.next
            temp=curr.next
            curr.next=Node(value)
            curr.next.next=temp
            self.size+=1


ll=LinkedList()
ll.append(0)
ll.append(1)
ll.append(2)
# ll.append(3)
ll.append(4)
ll.insertAt('inserted',0)
ll.display()
# print()
# ll.reverse()
# ll.display()
# print(len(ll))
# print(ll.size)