string=input("Enter the string: ")
for i in string:
    frequency=string.count(i)
    print(i ,":" ,frequency,end=" ,")
print()

#frequency of particular character
char=input("Enter the particular charater: ")
frequency_of_char =string.count(char)
print(char, ":", frequency_of_char)