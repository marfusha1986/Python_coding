#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
# student_heights[n] = int(student_heights[n])

student_heights = input("Input a list of student heights ").split()
total_height = 0
for student in student_heights:
   total_height += int(student)
   #print(total_height)

n = 0
for student in student_heights:
   n += 1
#print(n)
average_height = round(total_height / n)
print(average_height)
