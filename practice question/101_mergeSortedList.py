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
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr= next
        self.head=prev
    def sort(self):
        curr = self.head
        arr=[]
        while curr is not None:
            arr.append(curr.val)
            curr=curr.next
        print(arr)
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
# list1.reverse()
list1.show()
arr1=[1,2,4,5]
arr2=[1,3,4,8]
def mergeTwoArray(arr1, arr2):
    merged = []
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            merged.append(arr2[j])
            j+=1
    
    nums1T=arr1[i:]
    nums2T=arr2[j:]
    return merged+nums1T+nums2T

# print(mergeTwoArray(arr1, arr2))
        

def mergeTwoList(list1: Node, list2: Node):
    dummy=Node(0)
    hea=dummy
    curr1, curr2=list1, list2
    while curr1 is not None and curr2 is not None:
        if curr1.val<=curr2.val:
            dummy.next=curr1
            curr1=curr1.next
            dummy = dummy.next
        elif curr1.val>curr2.next:
            dummy.next = curr2
            curr2=curr2.next
            dummy = dummy.next
    
    while curr1 is not None:
        dummy.next=curr1
        curr1= curr1.next
        dummy=dummy.next
    
    while curr2 is not None:
        dummy.next=curr2
        curr2= curr2.next
        dummy=dummy.next
    return hea.next






