num=int(input("Enter the number:"))
prime_factors=[]
for i in range(2,num+1):
    if num%i==0:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            prime_factors.append(i)
print(prime_factors)