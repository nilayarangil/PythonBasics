def add(a,b):
    r=int(a)+ int(b)
    return r

print("enter two numbers")
z = input().split(",")

print(add(z[0],z[1]))