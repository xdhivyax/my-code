num=int(input("enter the number: "))
reverse=0
while num > 0:
    remainder = num %10
    reverse = (reverse*10) + remainder
    num = num // 10
print("the reverse of a number is: ",reverse)

n="1234"
new_string=""
while n!=0:
	rem=int(n)%10
	new_string+=str(rem)
	n=int(n)//10
print(new_string)