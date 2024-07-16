# A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.
# 1,2,145,40585 are known strong number
def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)
num=40585 
temp=num
sum=0
while temp>0:
    r=temp%10
    temp=temp//10
    sum=sum+factorial(r)
if num==sum:
    print("Strong Number")
else:
    print("Not a strong number")
