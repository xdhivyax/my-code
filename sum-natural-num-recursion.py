def recur_sum(num):
    if num==1:
        return 1
    return num + recur_sum(num-1)
num=int(input("Enter the number: "))
print(recur_sum(num))