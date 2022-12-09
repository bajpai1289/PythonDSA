# def insertionSort(arr):
#     arr=list(arr)
#     n = len(arr)
#     for i in range(n):
#         current = arr.pop(i)
#         j=i-1
#         while j>=0 and arr[j]>current:
#             j-=1
#         arr.insert(j+1,current)
#     return arr

# nums=[2,5,4,1,3,6,8,7,14,56]
# print(insertionSort(nums))



def insestionSort(arr):
    arr=list(arr)
    for i in range(len(arr)):
        current = arr.pop(i)
        j=i-1
        while j<=0 and arr[j]>current:
            j-=1
        arr.insert(j+1, current)
    return arr

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self, value):
        if self.head == None:
            self.head=Node(value)
        
        else:
            currentNode= self.head
            while currentNode.next is not None:
                currentNode=currentNode.next
            currentNode.next = Node(value)

    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def deleteNode(self, value):
        current = self.head
        if current.value==value:
            self.head=self.head.next
        else:
            while current.next is not None and current.next.value !=value:
                current = current.next
                if current.next is None:
                    print('No such value in the linked list')
                    return
            
            if current.next.value==value:
                current.next=current.next.next
            else:
                print('No such value in the list')

    def insertSort(self):
        current = self.head
        while current.next is not None:
            curr=current.value
            self.deleteNode(current.value)
            prev=current
            while prev is not None and self.value>curr:
                pass

list1 = LinkedList()
list1.append(5)
list1.append(3)
list1.append(1)
list1.append(8)
list1.append(10)
list1.display()
print('\ndelete operation:\n')
list1.deleteNode(11)
list1.display()
