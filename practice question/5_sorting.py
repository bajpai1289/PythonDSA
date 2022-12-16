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
            print(current.value,end="--->")
            current = current.next
    
    def deleteNode(self, value):
        current = self.head
        if current.value==value:
            self.head=self.head.next
        else:
            while current.next is not None and current.next.value != value:
                current = current.next
                if current.next is None:
                    print('No such value in the linked list')
                    return
            
            if current.next.value==value:
                current.next=current.next.next
            else:
                print('No such value in the list')



list1 = LinkedList()
list2 = LinkedList()
# list1.append(1)
# list1.append(5)
# list1.append(3)
# list1.append(9)
# list1.append(7)
# list1.display()
list2.append(10)
list2.append(8)
list2.append(6)
list2.append(4)
list2.append(2)
list2.append(0)
# list1.display()
list2.display()
# print('\ndelete operation:\n')
# list1.deleteNode(11)
# list1.display()
def merge_sorted_lists(list1: LinkedList, list2: LinkedList)->LinkedList:
    list3=LinkedList()
    current1=list1.head
    current2=list2.head
    while current1 is not None and current2 is not None:
        if current1.value>current2.value:
            list3.append(current2.value)
            current2=current2.next
        elif current2.value>current1.value:
            list3.append(current1.value)
            current1=current1.next
        elif current1.value == current2.value:
            list3.append(current2.value)
            list3.append(current1.value)
            current1=current1.next
            current2=current2.next
    if current1 is None:
        while current2 is not None:
            list3.append(current2.value)
            current2=current2.next
    elif current2 is None:
        while current1 is not None:
            list3.append(current1.value)
            current1=current1.next
    list3.display()

def sort(list2):
    current=list2.head
    if current == None:
        return 
    while current.next is not None:
        if current.value>current.next.value:
            # print(current.value, current.next.value)
            current.value,current.next.value=current.next.value,current.value
            sort(list2)
        current=current.next
    # list2.display()
    # print()
    return



merge_sorted_lists(list1, list2)

# merge_sorted_lists(list1, list2)
# sort(list2)
# print(sort(list2))
print()
sort(list2)
list2.display()

