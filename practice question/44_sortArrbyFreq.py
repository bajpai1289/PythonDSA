
# def frequencySort( nums: 'list[int]'):
    # d={}
    # for i in nums:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # d=dict(sorted(d.items(), key=lambda x:x[1]))
    # res = {}
    # for i, v in d.items():
    #     res[v] = [i] if v not in res.keys() else sorted(res[v] + [i],reverse=True)
    # print(res)
    # result=[]
    # for k, value in res.items():
    #     result+=sorted([*value*k], reverse=True)
    # # print(result)
    # return result
#     num_freq = {}
#     for num in nums:
#         if num not in num_freq:
#             num_freq[num] = 1
#         else:
#             num_freq[num] += 1
#     nums.sort(key=lambda x: (num_freq[x], -x))
#     return nums


# print(frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1])==[5,-1,4,4,-6,-6,1,1,1])

def my_filter(predicate, items):
    new_list = []
    for item in items:
         # Call the passed function (lambda)
        if predicate(item):
            new_list.append(item)
    return new_list

print(my_filter(lambda n: n > 5, range(10)))  # Prints [6, 7, 8, 9]