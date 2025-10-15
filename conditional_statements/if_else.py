temp = float(input("Give the temperature: "))

if temp<20:
    print("It's cold")
elif temp>20 and temp<30:
    print("It's warm")
elif temp>=30:
    print("It's hot")

num = float(input("Give a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")  

num = float(input("Give a number: "))
if num>0
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")


marks  = float(input("Give your marks: "))
if marks>=90 and marks<=100:
    print("A") 
elif marks>=75 and marks<90:
    print("B")
elif marks>=50 and marks<75:
    print("C")
else:
    print("Fail")

username = input("Username:   ")
password = input("Password:   ")

if username=='admin' and password=='admin123':
    print("Login successful")
else:
    print("Inalid credentials")


num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1>=num2 and num1>=num3:
    print(f"{num1} is the largest")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is the largest") 
else:
    print(f"{num3} is the largest")


Amount = float(input("Enter the amount: "))
if Amount>5000:
    print(f"Eligible for 20% discount:{Amount*0.80}")
elif Amount>=2000 and Amount<5000:
    print(f"Eligible for 10% discount:{Amount*0.90}")
else:
    print(f"not eligible for discount:{Amount}")

age = int(input("Enter your age: "))
had_ID = input("True or False: ")
if age>=18 and had_ID=='True':
    print("Eligible to vote")
else:
    print("Not eligible to vote")   