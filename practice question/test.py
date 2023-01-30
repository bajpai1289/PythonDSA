def isEven(n):
      if n%2==0:
            return False
      else:
             return True
arr=[str(i) for i in range(100,1000) if i%5==0]

arr=[i for i in arr if not any(isEven( int(c)) for c in i)]
print(arr)