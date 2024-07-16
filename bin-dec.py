def bin_to_dec(num):
    bin_val=num
    dec_val=0
    base=1          #2 power of 0 is 1
    while bin_val >0:
        last_digit=bin_val%10
        dec_val+=last_digit*base
        bin_val=bin_val//10
        base=base*2
    return dec_val
num=int(input("Enter the binary number: "))
print(bin_to_dec(num))