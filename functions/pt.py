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