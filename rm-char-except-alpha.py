string=(input("Enter the string:"))
new_string=""
for i in string:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        new_string+=i
print("Alphabets in string are",new_string)
