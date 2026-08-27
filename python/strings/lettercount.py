
s= 'programming language'
letter_count = {}
for ch in s:
    if ch in letter_count:
        letter_count[ch] += 1
    else:
        letter_count[ch] = 1
print(letter_count)