#Given n elements, each of which has a wieghts and a profit, determine the maximum profit that can 
#be obtained by selecting a subset of the element wieghing no more than the capacity

from unittest import TestCase


test0={
    'input':{
        'capacity': 165,
        'weights': [23,31,29,44,53,38,63,85,89,82],
        'profits': [92,57,49,68,60,43,67,84,87,72]
    },
    'output':309
}
test1={
    'input':{
        'capacity':3,
        'weights' : [4,5,6],
        'profits' : [1,2,3]
    },
    'output':0
}
test2={
    'input':{
        'capacity':4,
        'weights' : [4,5,1],
        'profits' : [1,2,3]
    },
    'output':3
}
test3={
    'input':{
        'capacity':170,
        'weights' : [41,50,49,59,55,57,60],
        'profits' : [442,525,511,593,546,564,617]
    },
    'output':1735
}
test4={
    'input':{
        'capacity':15,
        'weights' : [4,5,6],
        'profits' : [1,2,3]
    },
    'output':6
}
test5={
    'input':{
        'capacity':15,
        'weights' : [4,5,1,3,2,5],
        'profits' : [2,3,1,5,4,7]
    },
    'output':19
}

tests=[test1,test2,test3,test4,test5,test0]


def max_profit_rec(weights,profits, capacity, idx=0):
    if idx==len(weights):
        return 0
    elif weights[idx]>capacity:
        return max_profit_rec(weights,profits, capacity,idx+1)
    else:
        option1= max_profit_rec(weights,profits, capacity,idx+1)  #elemnt doesnt get selected
        option2=profits[idx]+max_profit_rec(weights,profits,capacity-weights[idx],idx+1)
        return max(option1,option2)
        
#Memoized solution
#hint: look for what is changing
# within the recursive calls here 
#wieghts and the profits remain the same and its the capacity and the index is 
#what changes so we can take the capacity, idx as the key in the memoization dictionary 
# and when each time we compute store the result in the dictionary before returnin g it and at 
# the beginning of the recursive funstion check within the dictionary of the same capacity and the 
# index is already present there and return it
def max_profit_memo(weights,profits, capacity):
    memo={}
    def recurse(capacity=capacity,idx=0):
        key=(capacity,idx)
        if key in memo:
            return memo[key]
        elif idx==len(weights):
            memo[key]=0
        elif weights[idx]>capacity:
            memo[key]=recurse(capacity,idx+1)
        else:
            option1=recurse(capacity,idx+1)
            option2=profits[idx]+recurse(capacity-weights[idx], idx+1)
            memo[key]=max(option1,option2)
        return memo[key]
    return recurse(capacity=capacity,idx=0)

print(max_profit_memo(**test2['input']))