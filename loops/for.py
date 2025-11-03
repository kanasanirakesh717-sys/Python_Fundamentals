for i in range(1,11):
    if i%2==0:
        print(i)
        
n= int(input("Enter a number: "))
add = 0
count = 1
while count<=n:
    add+=count
    count+=1
print(add)

n= int(input("Enter a number: "))
count = 1
while count<=n:
    for i in range(count):
        print("*",end=" ")
    count+=1
    print()



# Q1.
# Create a variable a = 10 and b = 3.
# Print the result of:

# addition

# floor division

# exponent (a to the power b)

a = 10 
b = 3
print(f"add:{a+b}")
print(f'div:{a//b}')
print(f'exponent:{a ** b}')

# Q2.
# Write a program to check if a number entered by the user is even or odd.

num = int(input("Enter the number: "))

if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Q3.
# Given a list nums = [2, 4, 6, 8, 10],
# calculate the sum of all elements using a for loop (don’t use sum()),
# and then find the maximum using a built-in function.

nums = [2, 4, 6, 8, 10]
add=0
for i in nums:
    add+=i
print(f"The num sum of {nums} is {add}\nThe max of {nums} is {max(nums)}")

# Use a while loop to print numbers from 5 down to 1.
 
num = 5
while num>0:
    print(num)
    num-=1


# Q5.
# Given a string s = "Python", print:
# the first and last character,
# and the reverse of the string using slicing.

s = "Python"
print(f"{s[0]},{s[len(s)-1]}")


# Q6.
# Create a function greet(name) that prints "Hello <name>, welcome to Python!".
# Then call it for your name.

def greet(name):
    print(f"Hello {name}, welcome to Python!")

greet('Rakesh')

# Q7.
# Given a tuple t = (5, 10, 15, 20, 25),
# print the index of the value 15 and convert the tuple into a list.

t = (5, 10, 15, 20, 25)
print(t.index(15))
l = list(t)
print(l)

# Q9.
# Write a program that prints all even numbers between 1 and 20 using a for loop and the range() function.
for i in range(0,21):
    if i%2==0:
        print(i)

# Q10.
# Create a function calc(a, b, op) that takes two numbers and an operator (+, -, *, /).
# Return the result based on the operator entered.

a  = int(input("Enter the 1st num: "))
b  = int(input("Enter the 2nd num: "))
op = input("Select the operation: + , - , / , % , *")

match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
