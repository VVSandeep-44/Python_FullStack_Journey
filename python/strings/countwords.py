
'''
 take a string, count how many words are there. assume that there are no extra spaces in the string and there are no spaces at the beginning and and the end. 
 '''
s ="Python is a programming language"
# word_count = len(s.split())
# print("Number of words:", word_count)
count = 0
for ch in s:
    if ch == " ":
        count += 1
print("Number of words:", count + 1)