#Harshad Number is the sum of the digits of the number can perfectly divide the number or not.
num=int(input("Enter the number:"))
str_num=str(num)
sum=0
for i in str_num:
    sum=sum+int(i)
if num%sum==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")