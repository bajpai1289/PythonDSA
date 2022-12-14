MAX_HASH_TABLE_SIZE=4096
data_list=[None]*4096

#this function just ad the unicode of all characters in a string take the remainder of it by length of data list and return it
def get_index(data_list, a_string):
    #variable to store the result (updated after each iteration)
    result=0
    for a_charachter in a_string:
        #convert the character to a number (using ord)
        a_number=ord(a_charachter)
        #update the result by adding the number
        result+=a_number
        
    #take the remainder of the result with the size of the data list
    list_index=result%len(data_list)
    return list_index
         
#print(get_index(data_list,'Abhishek')) 
#Thus now we can store the item at the get index position of the data List

# key,value='Aakash','9797979997'
# idx=get_index(data_list,key)
# data_list[idx]=(key, value)

#this whole thing can be written in the single line of code as follows

# data_list[get_index(data_list,'Hemanth')]=('Hemanth','95959595454')

#to find the value associated with the key in this we can simply get th ehasgh value
# f=get_index(data_list,'Aakash')
# key,value=data_list[f]
# print(key,value)

# To print all the valus of the this hash map we can simply do this

# keys=[kv[0]for kv in data_list if kv is not None]
# print(keys)



class hashTable:
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE) -> None:
        self.data_list=[None]*max_size
    
    def insert(self, key,value):
        idx = get_index(self.data_list,key)
        self.data_list[idx]=(key,value)
    
    def find(self, key):
        idx=get_index(self.data_list, key)
        kv=self.data_list[idx]
        if kv is None:
            raise IndexError('Not found')
        else:
            key,value=kv
            return value
    
    def update(self, key, value):
        idx=get_index(self.data_list, key)
        self.data_list[idx]=key,value
    
    def list_all(self):
        return [kv[0] for kv in data_list if kv is not None]
    
basic_table=hashTable(max_size=1024)

basic_table.insert('listen',99)
basic_table.insert('silent',200)
# print(basic_table.find('listen'))


def get_valid_index(datalist,key):
    idx=get_index(datalist,key)
    
    while True:
        k=datalist[idx]
    
        if k is None:
            return idx
        i,v=k
        if i==key:
            return idx
        idx+=1
        if idx==len(datalist):
            idx=0
    
data_list2=[None]*MAX_HASH_TABLE_SIZE
# print(get_valid_index(data_list2,'listen')==655)

# data_list2[get_index(data_list2,'listen')]=('listen',99)
# print(get_valid_index(data_list2,'silent')==656)
            
            


class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list=[None]*max_size
    
    def insert(self, key, value):
        idx= get_valid_index(self.data_list,key)
        self.data_list[idx]=(key,value)
        
    def find(self, key):
        idx=get_valid_index(self.data_list, key)
        # print(idx)
        kv=self.data_list[idx]
        if kv is None:
            return ('Not found')
        else:
            key,value=kv
            return value
        # return None if kv is None else kv[1]
    
    def update(self,key, value):
        idx=get_valid_index(self.data_list,key)
        self.data_list[idx]= (key,value)
        
    def list_all(self):
        return ( [kv for kv in self.data_list if kv is not None])
        # print(self.data_list)
    
probingTable=ProbingHashTable()
probingTable.insert('silent',99)
probingTable.insert('listen',200)

probingTable.list_all()
test=probingTable.list_all()
probingTable.update('silent', 101)
print(probingTable.find('silent'))
        
print(hash('hello')) #does same thing as get_valid_INDEX

#Hash Table Imporvements:
'''

1. Track the size of the hash table i.e. number of key-value pairs so that len(table) has complexity O(1).
2. Implement deletion with tombstones as described here: https://research.cs.vt.edu/AVresearch/hashing/deletion.php
3. Implement dynamic resizing to automatically grow/shrink the data list: https://charlesreid1.com/wiki/Hash_Maps/Dynamic_Resizing
4. Implement separate chaining, an alternative to linear probing for collision resolution: https://www.youtube.com/watch/T9gct6Dx-jo

'''