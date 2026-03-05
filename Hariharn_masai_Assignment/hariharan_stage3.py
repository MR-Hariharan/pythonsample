Student_name = input("enter the student name:")
a = int(input())
b = int(input())
c = int(input())
print(Student_name)
total_marks = a + b + c
print(f"Total: {int(total_marks)}/300")
percent = (total_marks/300) * 100
print(f"Percentage: {percent}%")
if percent >= 75:
        grade = "A"
elif percent >= 60:
        grade = "B"   
elif percent >= 40:
        grade = "C"
elif percent < 40:
        grade = "F" 
print(f"Grade: {grade}")        