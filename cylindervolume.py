print("Type radius,height,color to find volume of a cylinder")
dmn = input().split(",")

rd = dmn[0]
hgt = dmn[1]
clr = dmn[2]
#create an empty cylinder dictionary
cldr = {
    "radius": 0,
    "height": 0
}
#assign the values read to the dictionary keys
cldr["radius"] = rd
cldr["height"] = hgt
#add a NEW key to the cylinder dictioary
cldr["color"] = clr

#calculate volume, volume = 3.14* radius *radius * height
volume = 3.1415 * int(cldr["radius"]) * int(cldr["radius"]) * int(cldr["height"])

print("the volume of the", cldr["color"], " cylinder is",volume,"cubic units")