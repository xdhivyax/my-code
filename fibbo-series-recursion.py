def fibbo_recursion(i):
    if i<0:
        print("Incorrect input")
    elif(i==0):
        return i
    elif(i==1):
        return i
    else:
        return fibbo_recursion(i-1)+fibbo_recursion(i-2)
num=int(input("Enter the value:"))
for i in range(0,num):
    print(fibbo_recursion(i))

