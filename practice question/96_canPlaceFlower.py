def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count: int =0
    for i in range(len(flowerbed)):
        if flowerbed[i]==0:
            isEmptyLeft=i==0 or flowerbed[i-1]==0
            isEmptyRight = i==len(flowerbed)-1 or flowerbed[i+1]==0

            if isEmptyLeft and isEmptyRight:
                flowerbed[i]=1
                count+=1
    print(flowerbed)
    return count>=n












print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))