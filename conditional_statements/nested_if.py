# num = int(input("Enter a number: "))

# if num>=0:
#     if num%2==0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive and odd.")
# else:
#     print("The number is negative.")

# username = input("Enter username:  ")
# password = input("Enter password:  ")
# if username == "admin":
#     if username =="admin" and password=="admin123":
#         print("Login successful")
#     elif username =="admin" or password=="admin123":
#         print("Incorrect password")
# else:
#     print("Invalid username")

marks = int(input("Enter your marks: "))    
if marks>=35:
    print("You have passed the exam.")
    if marks>=75:
        print("You have passed with distinction.")
    elif marks>=60:
        print("You have passed with first division.")
    else:
        print("You have passed with second division.")
else:
    print("You have failed the exam.")