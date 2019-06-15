print("type a sentence with happy in it")
hp = input().split(" ")
c = 0
for word in hp:
 if word == "happy":
     c = c + 1
print("happy ocurred",c,"times")