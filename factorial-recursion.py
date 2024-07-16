def fact_recur(n):
    if n==0:
        return 1
    return n * fact_recur(n-1)

num=int(input("Enter the number:"))
print("The factorial of", num,"is",fact_recur(num))
