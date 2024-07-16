low=100
high=200
for num in range(low,high+1):
    length=len(str(num))
    sum=0
    temp=num
    for i in range(length):
        digit=int(num%10)
        sum=sum+(digit**length)
        num=num//10
    if sum==temp:
        print(sum,end="")