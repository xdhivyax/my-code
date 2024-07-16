#A Number that can be represented as the sum of all the factors of the number is known as a Perfect Number.
num=int(input("Enter the number: "))
sum_of_divisors =0
for i in range(1,num):
    if num % i == 0:
        sum_of_divisors =sum_of_divisors + i
if (num==sum_of_divisors):
    print("It is a perfect number")
else:
    print("It is not a perfect number")