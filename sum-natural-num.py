num=int(input("Enter the number"))
sum=0
#sum = int((number * (number + 1))/2)
for i in range(num+1):
    sum+=i
print("The sum of natural number is",sum)