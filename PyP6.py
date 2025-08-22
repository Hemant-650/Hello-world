# Practical 6: Student Marksheet
name = input("Enter student name: ")
marks = []
for i in range(5):
 marks.append(int(input(f"Enter marks of subject {i+1}: ")))
total = sum(marks)
percentage = total / 5
print("Total Marks:", total)
print("Percentage:", percentage)