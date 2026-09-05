# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
marks = float(input("Enter your marks: "))

# Output Formatting
print("\n---------- STUDENT DETAILS ----------")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Course : {course}")
print(f"Marks  : {marks:.2f}")
print("-------------------------------------")


git init
git status
git add .
git commit -m "Added student details program"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main