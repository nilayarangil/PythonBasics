'''print("type in a list of numbers")
numlst = input().split(",")
min = 10000000
max = 0
for n in numlst:
    if int(n) > int(max):
        max = int(n)
    if int(n) < int(min):
        min = int(n)
print("the range is",int(max)-int(min))'''

print("enter numbers")
#read the numbers into a list
nlist = input().split(",")
#create another empty list to hold integers
nlist2 = []
#read the strings in the first list, cast them as integers
#and add them to the second list
for n in nlist:
    nlist2.append(int(n))

print(nlist) #this will print list as strings eg ['1','3','5']
print(nlist2) #this will be [1,3,5]

max = max(nlist2) # use max to get max value from list
min = min(nlist2)

print("the range is",int(max)-int(min))
    
