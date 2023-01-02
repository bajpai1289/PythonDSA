dividend=-2147483648
divisor=-1
count=1
minus: bool = False
if abs(dividend)<abs(divisor):
    print(0)
    exit(0)
if divisor==1:
    return dividend

if divisor<0 or dividend<0:
    if dividend<0 and divisor>0:
        dividend=-dividend
        minus=True
    if divisor<0 and dividend>0:
        divisor=-divisor
        minus=True 
if divisor<0 and dividend<0:
    minus=False
    dividend=-dividend
    divisor=-divisor

rem=dividend-divisor
while rem>=divisor:
    print(count)
    rem-=divisor
    count+=1
    
if minus:
    print(-count)
else:
    print(count)