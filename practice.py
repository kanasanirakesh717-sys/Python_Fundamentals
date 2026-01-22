l = [1,2,3,4,5]
add = 0
mul = 1
for i in l:
    add+=i
    mul*=i
print(f"Sum of {l} = {add} \n Mul of P{l} ={mul}")


l = [1,2,3,4,5]
for i in l:
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

t =(21,4,65,89,38,80,3)
print(f"Max:{max(t)} \nMin:{min(t)}")


l = [10, 20, 10, 30, 20, 10]

for i in l:
    print(f"{i} count is :{l.count(i)}")


l = [1,2,2,3,4,5,6]
l1 = set(l)
print(l1)

l = [122, 23, 33, 42, 5, 56]
L = len(l)-1
while L>=0:
    print(l[L])
    L-=1


init =0
limit =50
while init<=50:
    if init%3==0 and init%5==0:
        print(f"{init} is divisible by both 3 and 5 ")
    init+=1

t = (1,3,4)
t1 = (1,3,2,4)
if t==t1:
    print(f"{t}\n{t1}\nare identical")
else:
    print(f"{t}\n{t1}\nare not identical")


l =  [5, 10, 15, 20, 25]
l.append(30)
l.remove(10)
l.insert(1,12)
print(l)

init = 1
limit = 5
while init<=limit:
    for i in range(0,init):
        print('*',end=" ")
    print("")
    init+=1



def operation():
    a  = int(input("Enter the 1st num: "))
    b  = int(input("Enter the 2nd num: "))
    op = input("Select the operation: + , - , / , * , exit: ")

    while True:
        if op == "exit":
            print("Exiting Calculator...")
            break
        match op:
            case '+':
                print(a+b)
                operation()
            case '-':
                print(a-b)
                operation()
            case '*':
                print(a*b)
                operation()
            case '/':
                print(a/b)
                operation()
            case _:
                print("invalid operator")
                operation()


# operation()

def string_tool():
    s = input("Enter the String: ") 

    while True:
        
        print(f"1. Count vowels\n2.Reverse string\n3.Check palindrome\n4.Convert case (upper/lower/title)\n5.Exit")
        user_input = int(input("Choose from above: "))

        if user_input==1:
            l = ['a','e','i','o','u']
            count=0
            for i in s:
                if i.lower() in l:
                    count+=1
            print(f"Vowels present:{count}")

        elif user_input==2:
            print(f"{s[::-1]}")
    
        elif user_input == 3:
            if s== s[::-1]:
                print(f"{s} is a palindrome")

            else:
                print(f"{s} is not palindrome")

        elif user_input==4:
            print(f"lower:{s.lower()}\nupper:{s.upper()}\n title:{s.title()}")

        elif user_input ==5:
            print('Exiting from loop')
            break

        else:
            print("Invalid num")
 

string_tool()