s = "Palle Technologies"

for c in range(len(s)):
    if s[c] in "aeiouAEIOU":
        s = s[:c] + 'z' + s[c+1:]
print(s)