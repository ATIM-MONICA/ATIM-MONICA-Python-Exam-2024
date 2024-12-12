# 3.(i)

# Ask the user for their age
age = int(input("Please enter your age: "))

 # Check if the user is eligible
if age >= 18:
    print("You are eligible")
else:
  print("You are not eligible")

# 3.(ii)
grade_students = int(input("Please enter Student's mark 0-100: "))


if grade_students >= 91 and grade_students <= 100:
	print("Your Grade is A")
elif grade_students >= 80 and grade_students < 90:
	print("Your Grade is B")
elif grade_students>= 70 and grade_students < 80:
	print("Your Grade is C")
elif grade_students>= 60 and grade_students < 70:
	print("Your Grade is D")
else:
	print("Your Grade is F")
	
# 3.(iv) Modifying to handle invalid inputs
grade_students = int(input("Please enter Student's mark 0-100: "))


if grade_students >= 91 and grade_students <= 100:
	print("Your Grade is A")
elif grade_students >= 80 and grade_students < 90:
	print("Your Grade is B")
elif grade_students>= 70 and grade_students < 80:
	print("Your Grade is C")
elif grade_students>= 60 and grade_students < 70:
	print("Your Grade is D")
elif grade_students < 60:
	print("Your Grade is F")
else: 
	print("Invalid Input!")
    
    

# 3.(v) Adding comments
grade_students = int(input("Please enter Student's mark 0-100: "))


if grade_students >= 91 and grade_students <= 100:
	print("Your Grade is A, Excellent")
elif grade_students >= 80 and grade_students < 90:
	print("Your Grade is B, Excelllent")
elif grade_students>= 70 and grade_students < 80:
	print("Your Grade is C, Good")
elif grade_students>= 60 and grade_students < 70:
	print("Your Grade is D, Satisfactory")
elif grade_students < 60:
	print("Your Grade is F, Need Improvement")

else:
	print("Invalid Input!")
