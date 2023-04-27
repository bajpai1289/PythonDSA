# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# a2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(arr.dot(a2))
# print(arr@a2)
# for i in range(4):
#     pass

tpl = (1,2,[4,3,2],'strs')
def test(t: tuple):
    t[-1]+='this'
test(tpl)
print(tpl)