num=int(input("Enter the number: "))
temp=num
sum=0
length=len(str(num))
for i in range(length):
    r=temp%10
    sum+=pow(r,length)
    temp=temp//10
if sum==num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

def is_armstrong(num1):
	num_str = str(num1)
	n = len(num_str)
	sum = 0
	for digit in num_str:
		sum += int(digit)**n
	if sum == num1:
		print("Armstrong number")
	else:
		print("Not a Armstrong number")
num1=153
is_armstrong(num1)
