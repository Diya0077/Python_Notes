name = input("Enter the name:")

marks1 = int(input("Enter marks1:"))
marks2 = int(input("Enter marks2:"))
marks3 = int(input("Enter marks3:"))
marks4 = int(input("Enter marks4:"))
marks5 = int(input("Enter marks5:"))


totalMarks = marks1+marks2+marks3+marks4+marks5
percentage = (totalMarks/500)*100

print(f"your total marks:{totalMarks} and you percentage is:{percentage}")
if percentage >= 90:
    print("congratulations you are passed. you got O")
elif percentage >= 80:
    print("You got A+")

elif percentage >= 70:
    print("You got A")

elif percentage >= 60:
    print("You got B")
else:
    print("HAHA!sorry you are fail.")
    pass
