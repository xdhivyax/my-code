#Anagram program in python is when strings share the same no of characters and also the same characters then strings are called anagrams. 
#The rearrangement of similar characters or letters in a string even if they don’t have the same meanings are anagrams

string1=input("Enter the string1: ")
string2=input("Enter the string2: ")
if len(string1) != len(string2):
    print("Strings are not anagram")
else:
    sorted_str1=sorted(string1)
    sorted_str2=sorted(string2)
    if sorted_str1 == sorted_str2 :
        print("Strings are anagram")
    else:
        print("Strings are not anagram")
