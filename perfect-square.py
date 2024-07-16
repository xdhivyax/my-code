from math import sqrt
def perfect_square(num):
    if num>=0:
        sr=int(sqrt(num))
        if num==sr*sr:
            print("Perfect Square")
        else:
            print("Not Perfect Square")
num=81
perfect_square(num)