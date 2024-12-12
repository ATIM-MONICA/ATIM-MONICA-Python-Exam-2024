# 1.(i)
# Prompting the user to input the radius of the circle
radius = int(input("Input the radius of the circle : "))
pi = 3.14
# Calculate the area of the circle using the formula: area = π * r^2
circle_area = pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")


# 1.(ii)
list = [4,7,2,9,12,15]
print(f"The original list is : {list}")

# Initialize sum
odd_sum = 0
for num in list:
    if num % 2 != 0:  # Check if the number is odd
        odd_sum += num

print("The sum of all odd numbers is:", odd_sum)


# 1.(iii)
# sum
number1 = int(input("First number: "))
number2 = int(input("\nSecond number: "))
sum = int(number1) + int(number2)
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))

# Difference
difference = int(number1) - int(number2)
print("The difference of {0} and {1} is {2}" .format(number1, number2, difference))

# Product
product = int(number1) * int(number2)
print("The product of {0} and {1} is {2}" .format(number1, number2, product))

# Quotient

quotient = int(number1) // int(number2)
print("The quotient of {0} and {1} is {2}" .format(number1, number2, quotient))


# 1.(iv)
#Updating a dict
student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Update the age to 26
student_info["age"] = 26

print(student_info)

# Adding a new key-value pair
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['city'] = 'Kampala'
print(student_info)

