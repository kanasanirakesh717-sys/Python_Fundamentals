day = input("Enter the number of the day (1-7):     ")
match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

Grade = input("Give u r grade")
match Grade:
    case "A":
            print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))

op = input("`Enter the operation (+, -, *, /): ")

match op:
    case "+":
        print(f"{n1} + {n2} = {n1 + n2}")   
    case "-":
        print(f"{n1} - {n2} = {n1 - n2}")
    case "*":
        print(f"{n1} * {n2} = {n1 * n2}")
    case "/":
        if n2 != 0:
            print(f"{n1} / {n2} = {n1 / n2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation! Please enter one of +, -, *, /.")
