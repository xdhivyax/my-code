num1=int(input("Enter the number1 : "))
num2=int(input("Enter the number2 : "))
if num1 > num2:
    small =num2
else :
    small =num1
for i in range (1,small+1):
    if (num1 % i == 0) and (num2 %i == 0):
        gcd =i
print("GCD is : ",gcd)
