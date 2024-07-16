def longest_palindrome(array):
    longest_palindrome = -1
    n = len(array)
    for i in range(n):
        if is_palindrome(array[i]):
            if array[i] > longest_palindrome:
                longest_palindrome = array[i]
    return longest_palindrome

def is_palindrome(i):
    original = i
    reverse = 0
    while i > 0:
        remainder = i % 10
        reverse = (reverse * 10) + remainder
        i = i // 10
    if reverse == original:
        return True

array = [12521, 1045401, 12321, 12421]
print(longest_palindrome(array))
