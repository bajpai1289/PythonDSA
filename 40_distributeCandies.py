'''N kid stand in line, each having an integer rating. We distribute candies following:
1. Each kid gets atleat 1 candy
2. Kids with higher ratings than their neighbours get more candies. Find min candies requires
Leetcode 135
  
'''
test_case = {
    'input': [1,3,7,1],
    'output': 7
}
def candy(ratings: 'list[int]') -> int:
    n = len(ratings)
    data = sorted((x,i) for i, x in enumerate(ratings)) #for this particular kid rating this is its index, then sort all the kids by the ratings 
    candies = [1]*n    
    print(data)             #assign the default 1 candy
    for _, i in data:
        if i>0 and ratings[i]>ratings[i-1]:
            candies[i]=max(candies[i],candies[i-1]+1)
        if i<n-1 and ratings[i]>ratings[i+1]:
            candies[i]=max(candies[i], candies[i+1]+1)
    print(candies)
    # return sum(candies)

print(candy([1,3,7,1]))