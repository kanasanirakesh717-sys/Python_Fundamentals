# Create a function to find maximum of 3 numbers
def numMax(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater")
    elif b>a and b>c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
numMax(12.4,23.4,8)


# Create a function that returns sum of digits of a number

def sum(a,b):
    result = a+b
    return result
print(sum(1,2))

# Create a function to count vowels in a string
vowels = ['a','e','i','o','u','A','E','I','O','U']
def countVowels(word):
    count = 0
    for i in word:
        if i in vowels:
            count+=1

    return count
result = countVowels("Rakesh")
print(f"No of vowels:{result}")

# Create a function is_palindrome(word)
def checkPalindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

checkPalindrome("mom")

# Create a function grade_marks(marks)
def checkgrade(num):
    if num>=90:
        print(f"Got A grade")
    elif num>=80:
        print(f"Got B grade")
    elif num>=70:
        print(f"Got C grade")
    else:
        print(f"Fail")
checkgrade(78)

# Create a function reverse_list(lst):

def reverselist(a):
    return a[::-1]
print(reverselist([1,35,66,76,"Rakesh","sai","ramu",21,45]))

# Create a function count_even_odd(numbers)

def countevenodd(a):
    even = 0
    odd = 0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
    result = print(f"Even:{even}, Odd:{odd}")

countevenodd([1,23,4,56,77,87,86,56])



def marks_analyzer():
    marks = []
    sub = 1
    while sub <= 5:
        mark = int(input(f"Enter the marks of subject {sub}: "))
        marks.append(mark)
        sub += 1

    total = sum(marks)
    avg = total / len(marks)

    print(f"\nMarks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")

    if avg >= 90:
        print("Overall Grade: A")
    elif avg >= 80:
        print("Overall Grade: B")
    elif avg >= 70:
        print("Overall Grade: C")
    elif avg >= 60:
        print("Overall Grade: D")
    else:
        print("Overall Grade: F")

# marks_analyzer()

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
 

# string_tool()