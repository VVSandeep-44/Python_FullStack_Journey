
'''
take 2 strings. find those 2 strings are anagrams. if 2 strings are of same length, and made up of same letters with dif combinations then it is anagram. 
'''

str1="listen"
str2="silent"

if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")


# without using sorted function
str1="listen"
str2="silent"
if len(str1) == len(str2):
    for ch in str1:
        if ch not in str2:
            print("Not Anagram")
            break
    else:
        print("Anagram")