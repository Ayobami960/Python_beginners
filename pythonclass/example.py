# #  def is use to define a function
# def show_data(first_name, last_name):
#     print("Welcome back!", first_name, last_name)


# show_data("Daniel", "Kehinde")


# print the length of a string  hello
# print(len("Hello"))


# # concatenate two string
# print("Hello" + "world")

# Apply upper method to "Hello"
# print("hello".capitalize())

# Extract a slice from a string
# print("Hello"[1:4])

# User the index string method
# print("Hello".index("e"))


# # Concatenate two lists which is easy to changes
# my_list = ["a", "b", "c", "d", "e"]
# number_list = ["1", "2", "3", "4"]
# print(my_list + number_list)

# Change a specific element in a list
# my_list = ["a", "b", "c", "d", "e"]
# my_list[1] = 7
# print(my_list)


# use the insert method
# my_list = ["a", "b", "c", "d", "e"]
# my_list.insert(1,7)
# print(my_list)


# use the remove method
# my_list = ["a", "b", "c", "d", "e"]
# my_list.remove("d")
# print(my_list)


# use the append method
# my_list = [1,2,3,4,5]
# my_list.append(6)
# print(my_list)

# address = "198.567.XX.XX"
# # Extract the first three charaters of an Ip address
# print(address[0:3])


# address = "198.567.XX.XX", "198.561.XX.XX", "180.164.XX.XX", "192.168.XX.XX", "184.890.XX.XX"
# # Extract the first three characters of an Ip address


# Extract email addresses
# import re
# email_log = """Email received june 2 from user1@email.com.
# Email received june 2 from user2@email.com.
# Email received june 2 from invalid_email@email.com."""
# print(re.findall("\w+@\w+\.\w+", email_log))

# Open a text file
# with open("login_attempts.txt", "r") as file:
#     file_text = file.read()
# print(file_text)


# Open, read, and split a text file
with open("login_attempts.txt", "r") as file:
    file_text = file.read()
# print(file_text.split())
usernames = file_text.split()
# print(usernames)


# Create a function that counts a user's failed login attempts
# usernames = "fwefwe32we"


# def login_check(login_list, current_user):
#     counter = 0
#     for i in login_list:
#         if i == current_user:
#             counter = counter + 1
#             if counter >= 3:
#                 return "You have tried to login three or more times. Your account has been locked."
#             else:
#                 return "You can log in!"
#     print(login_check(usernames, "fwefwe32we"))

# if = Do some code only if some condition is True
# # Else do somethng else

age = int(input("Enter your age:"))

print("You are now signed up!")