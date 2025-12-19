
# Demonstrate a type error
# device_id = "h332rbi"
# number = 3
# print(device_id + number)

# # Reassign a variable
# device_id = "h332rb17"
# print(device_id)
# device_id = "n73ab07"
# print(device_id)

# Create a conditional using for loop
# operating_system = "OS 2"

# if operating_system == "OS 2":
#     print("Updates needed")
# else:
#     print("No Updates needed")


# Loop function for (for loop)
# for i in [1,2,3,4]:
#     print(i)

# Run for loop with range
# for i in range(10):
#     print("Cannot connect to the destination")


# Create  While loop. I check how many device user are connected to we can you white loop
# max_devices = 5
# i = 1

# while i < max_devices:
#     print("User can still connect to additional devices")
#     i = i + 1
#     print("User has reached maximum number of connected devices")

# create a function that give the employees
# Define a function 
# def greet_employee():
#     print("Welcome you`re logged in.")
# # THe next thing is to call a function
# greet_employee()

# Anothor function called range which user parameter
# Greet employess by name
# def greet_employee(first_name, last_name):
#     print("Welcome you`re logged in", first_name, last_name)
# greet_employee("Charley", "Patel")

# Creating a function by analysiing login attempts. because this function will continue failed attempts
# How to Return information form a function
# def calculate_fails(total_attempts, failed_attempts):
#  fail_percentage = failed_attempts / total_attempts
#  return fail_percentage

# percentage = calculate_fails(4,2)

# if (percentage >= .5):
#     print("Account locked.")


# Explore input and output of print function
# print("This is string, but" ,75, "is a number.")

# Explore input and output of type
# print(type("security"))
# print(type(73.2))


# Explore max function
# a = 3
# b = 9
# c = 6
# print(max(a,b,c))

# Use the sorted function
# username = ["elarson", "bmorena", "tshah", "sgilnore", "araab", "gesparza", "alevirsk", "ujaffrey"]
# print(sorted(username))

# Print account locked message when failed_attempts is greater than 5
failed_attempts = 10

if failed_attempts > 5:
    print("Account locked")