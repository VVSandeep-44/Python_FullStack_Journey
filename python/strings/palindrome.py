string = input("Enter a string:")
reverse=""
for ch in string:
    reverse = ch + reverse
print(reverse)
if string==reverse:
    print("Palindrome")
else:
    print("not palindrome")