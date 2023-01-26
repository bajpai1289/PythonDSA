# def twoSort(arr: 'list[int]'):
#     start=0
#     end = len(arr)-1
#     while start<end:
#         if arr[start]==1:
#             if arr[end]==0:
#                 arr[start], arr[end]=arr[end], arr[start]
#                 start+=1
#                 end-=1
#             else:
#                 end-=1   
#         else:
#             start+=1
#     return arr
    





# print(twoSort([0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1]))
from collections import defaultdict

def remove_last_triplet(input_list):
    to_remove = [False] * len(input_list)
    counts = defaultdict(int)
    
    for value in input_list:
        counts[value] += 1
    
    for value, count in counts.items():

        triplet_count = count // 3
 
        current_index = len(input_list) - 1
        

        for triplet_index in range(triplet_count):

            this_triplet_count = 0
            
            for input_index in range(current_index, -1, -1):
                if input_list[input_index] == value:
        
                    to_remove[input_index] = True
                    this_triplet_count += 1
  
                current_index -= 1
                
                if this_triplet_count == 3:
                    break
    
    output = []
    
    for index in range(len(input_list)):
        if not to_remove[index]:
            output.append(input_list[index])
    
    return output

input_list = [2,2,3,2,3,2]
output_list = remove_last_triplet(input_list)
print(output_list) 
