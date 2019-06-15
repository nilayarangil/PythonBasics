
numbers = [1,2,3,3,4,5,5,4,4,1,1,1,1]

count = 0
mode= 0

for n in numbers:
    if numbers.count(n) > count:
        count = numbers.count(n)
        mode = n

print("mode is", mode, "and it appears", str(count),"times")



    
