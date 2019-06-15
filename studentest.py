import studentclass as sc

Nilay = sc.Student()
Nilay.age = 10
Nilay.name = "Nilay"
Nilay.studentID = 142085
Nilay.awards.append("a honor roll")
Nilay.awards.append("bluebonnet award")
Nilay.personality.append("likes ping pong")
Nilay.personality.append("is active")

Varun = sc.Student()
Varun.age = 10
Varun.name = "Varun"
Varun.studentID = 142016
Varun.awards.append("classroom award")
Varun.awards.append("bluebonnet award")
Varun.personality.append("joyful")
Varun.personality.append("likes outdoors")
Varun.personality.append("is active")

Alex = sc.Student()
Alex.age = 10
Alex.name = "Alex"
Alex.studentID = 390621
Alex.awards.append("classroom award")
Alex.awards.append("bluebonnet award")
Alex.personality.append("joyful")
Alex.personality.append("likes outdoors")
Alex.personality.append("is inactive")

students = []
students.append(Nilay)
students.append(Varun)
students.append(Alex)
'''
#print names of students in the students list
for x in students:
    print(x.name)

#print Nilays awards
print(students[0].GetAwards())

#print students who are active
for s in students:
    for p in s.personality:
        if p == "is inactive":
            print(s.name)
'''
    
for s in students:
    if "is active" in s.personality:
        print(s.name)