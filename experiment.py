#cast a number
#y = int(2.8)
#print(y)

#print the value of pi
#a=float(22/7)
#print("pi is approximately",int(a))

#printing words and numbers
#x = 2.3
#print("the value of x is", x) #note the comma used
#print("the value of x in int is", int(x)) #note the comma used


#b = "  Hello, World!  "
#print(b.strip())  #.method()

#b=[1,2]
#print(b[0])


#a = "Hello World!"
#b = a.split(" ")
#print(b)
#print(b[1]) 

"""
print("Enter the base length:")
b = float(input())

print("Enter the height:")
h = float(input())
a = b*h*1/2
print("the area of the triangle is",a,"square units")

a = "Hello, World!"
print(a.split(",")[0]) # returns ['Hello', ' World!']

print("Enter your wish eg. sum 1,2")
w = input()
x = w.split(" ")[1] #this will get you ['1,2'] from  ['sum', '1,2']
y = x.split(",") # this will split 1,2 to 1 and 2
z = float(y[0])+float(y[1]) # y[0] will get 1
print(z)


print("Enter your wish eg. sum 1,2")
w = input().split(" ")[1].split(",")
print("sum of the numbers are", float(w[0]) + float(w[1]))



print("Enter your wish eg. sum 1 and 2")
w = input()
x = w.split(" ")
y = float(x[1]) + float(x[3])
print("sum is " , y )


print("Guess my password number range is 1-100")
h = input("Guess my password number range is 1-100")
if int(h) == 72:
  print("you guessed it")
elif int(h) >= 80:
  print("too large")
elif int(h) > 65 and int(h) < 70:
  print("you are pretty close to the answer")
elif int(h) > 75 and int(h) < 79:
  print("you are pretty close to the answer")
elif int(h) > 70 and int(h) < 75:
  print("you are extreeemeeely close!!!")
else:
  print("too small")




while True:
    h = input("Guess my password number range is 1-100 : ")
    if int(h) == 72:
     print("you guessed it")
     break
    elif int(h) >= 80:
     print("too large")
     continue
    elif int(h) > 65 and int(h) < 70:
     print("you are pretty close to the answer")
     continue
    elif int(h) > 75 and int(h) <= 79:
     print("you are pretty close to the answer")
     continue
    elif int(h) > 70 and int(h) < 75:
     print("you are extreeemeeely close!!!")
     continue
    else:
     print("too small")
     continue


print("Type your wish e.g add/muliply,divide/substract 1,2")

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
elif s == "subtract":
  print("the difference is ",float(a)-float(b))

# to convert first word to upper case. eg nilay to Nilay
print("enter your word")
a = input()
one = a[0]
upped = one.upper()

print(a.replace(one, upped))



print("input your word now..")
a= input()
print(a.capitalize())


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
"""
print("type words")
i = input()
i2 = i.split(" ")

thislist = []

for x in i2:
  thislist.append(x)

print(thislist)

