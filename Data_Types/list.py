names = ["Alice", "Bob", "Charlie","Alice", "Bob", "Charlie"]
age = [25, 30, 35, 25, 30,455]
emp_details = [["Rakesh",2000],["LOkesh",3000],["Ramesh",4000]]

# for i in range(0,len(names)):
#     print(f"{names[i]} is {age[i]} years old.")

# print(names[2:5])

for i in range(0,len(emp_details)):
    print(f"{emp_details[i][0]} salary is {emp_details[i][1]}")