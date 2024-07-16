#Automorphic number is a number whose square ends with the same digits as number itself
num=int(input("Enter the number:"))
square=pow(num,2)
mod=pow(10,len(str(num)))
if square%mod == num:
    print("Automorphic number")
else:
    print("Not automorphic number")
