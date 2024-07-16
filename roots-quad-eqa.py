import math
def roots_of_quadratic_equation(a,b,c):
    dis=(b**b - 4*a*c)
    squr_val=math.sqrt(abs(dis))
    if dis >0:
        print("Roots are real and different")
        print((-b+squr_val)/(2*a))
        print((-b-squr_val)/(2*a))
    elif dis==0:
        print("Roots are real and same")
        print(-b/(2*a))
    else:
        print("Roots are real and complex")
        print(-b/(2*a),"+i",squr_val)
        print(-b/(2*a),"-i",squr_val)
a=int(input("Enter the value a:"))
b=int(input("Enter the value b:"))
c=int(input("Enter the value c:"))
if a==0:
    print("Invalid input")
else: 
    roots_of_quadratic_equation(a,b,c)