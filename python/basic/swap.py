a=10
b=20

print(f"a={a} & b={b}")

print("---without temp---")
a,b = b,a
print(f"a={a} & b={b}")

print("---with temp---")
temp=a
a=b
b=temp
print(f"a={a} & b={b}")
