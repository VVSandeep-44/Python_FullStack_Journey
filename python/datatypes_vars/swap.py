a=23
b=44
print("before swap:", a, b)

#one way to swap
swap=a
a=b
b=swap

#2nd way to swap
a,b=b,a

#3rd way to swap
a=a+b
b=a-b
a=a-b

print("after swap:", a, b)