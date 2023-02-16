usernames = ["Skyler", "Kaitlyn", "Abby"]
passwords = ["password", "password1", "spiderman"]

# Use a while loop to perform user authentication.
# Assume each username is unique.

# Hint: .index()

username = input("Username: ")
password = input("Password: ")

username_index = None
password_index = None

for value in range(len(usernames)):
    if(username == usernames[value]):
        username_index = value

for value in range(len(passwords)):
    if(password == passwords[value]):
        password_index = value

if (username_index == password_index and username_index != None):
    print("Allow Access")

