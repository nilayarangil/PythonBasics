print("type your wish ex add 1,2 or multipy 1,2 or divide 1,2 or subtract 1,2")

i = input() # read the input
s = i.split(" ")[0] # this will get ['add']
s2 = i.split(" ")[1].split(",") #this will get ['1,2']
a = s2[0] #this will get 1
b = s2[1] #this will get 2
if s == "add":
  print("the sum is ",float(a)+float(b)) #this will print the words followed by a and b added by casting to float
elif s == "multiply":
  print("the product is ",float(a)*float(b))
elif s == "divide":
  print("the quotient is ",float(a)/float(b))

