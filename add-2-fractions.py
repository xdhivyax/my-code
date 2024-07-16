n1=int(input("Enter the numerator1:"))
d1=int(input("Enter the denominator1:"))
n2=int(input("Enter the numerator2:"))
d2=int(input("Enter the denominator2:"))
lcm=d1*d2
num=(n1*d2)+(n2*d1)
fraction=num/lcm
def gcd(num,lcm):
    gcd=0
    for i in range(1,min(num,lcm)+1):
        if num%i==0 and lcm%i==0:
            gcd=i
    return gcd
numerator=num/gcd(num,lcm)
denominator=lcm/gcd(num,lcm)
print("The sum of",n1,"/",d1,"and",n2,"/",d2,"is",int(numerator),"/",int(denominator))