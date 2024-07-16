#to find the factors of the number except the number itself and sum them all up. 
# We’ll check Whether the number is lower or greater than the sum. 
# For a Number to be classified as Abundant, the sum of it’s factors must be greater than the number itself.
num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum>num:
    print("Abundant Number")
else:
    print("Not Abundant Number")
