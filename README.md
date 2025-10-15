🔹 LIST

Definition:
A List is a type of array used to store multiple values with different data types.

🧠 Example & Built-in Methods
age = [25, 30, 35, 25, 30, 455]

1) age.append(10) = [25, 30, 35, 25, 30, 455, 10]
2) age.extend([500, 600]) = [25, 30, 35, 25, 30, 455, 10, 500, 600]
3) age.insert(2, 99) = [25, 30, 99, 35, 25, 30, 455, 10, 500, 600]
4) age.remove(25) = [30, 99, 35, 25, 30, 455, 10, 500, 600]
5) age.pop() = removes last element → [30, 99, 35, 25, 30, 455, 10, 500]
6) age.pop(1) = removes element at index 1 → [30, 35, 25, 30, 455, 10, 500]
7) age.clear() = []
8) age.index(35) = 2
9) age.count(30) = 2
10) age.sort() = [25, 25, 30, 30, 35, 455]
11) age.sort(reverse=True) = [455, 35, 30, 30, 25, 25]
12) age.reverse() = [455, 35, 30, 30, 25, 25]
13) age.copy() = [25, 30, 35, 25, 30, 455]
14) age[1:4] = [30, 35, 25]
15) age[:3] = [25, 30, 35]
16) age[2:] = [35, 25, 30, 455]
17) age[-1] = 455
18) age[-3:] = [25, 30, 455]
19) age[::2] = [25, 35, 30]
20) age[::-1] = [455, 30, 25, 35, 30, 25]

🔹 STRING

Definition:
A String is a combination of Unicode characters enclosed in single or double quotes.
Immutable — cannot be modified once created.

🧠 Example & Built-in Methods
1) string.capitalize() = "Hello world"
2) string.upper() = "HELLO WORLD"
3) string.lower() = "hello world"
4) string.title() = "Hello World"
5) string.swapcase() = "HELLO WORLD" → "hello world"
6) string.count('l') = 3
7) string.find('world') = 6
8) string.index('world') = 6
9) string.replace('world', 'Python') = "hello Python"
10) string.split() = ['hello', 'world']
11) " ".join(['hello', 'world']) = "hello world"
12) string.strip() = "hello world"
13) string.lstrip() → removes spaces from left
14) string.rstrip() → removes spaces from right
15) string.startswith('he') = True
16) string.endswith('ld') = True
17) string.isalpha() = False
18) string.isdigit() = False
19) string.isalnum() = False
20) string.isspace() = False
21) string.islower() = True
22) string.isupper() = False

🔹 TUPLE

Definition:
A Tuple is an immutable ordered array. Items are enclosed in parentheses ( ) and separated by commas.

🧠 Example & Built-in Methods
my_tuple = (10, 20, 30, 40, 50)
1) my_tuple.count(20) = 1
2) my_tuple.index(30) = 2

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2 = (1, 2, 3, 4)

# Repetition
t1 = (1, 2)
t2 = t1 * 3 = (1, 2, 1, 2, 1, 2)

# Membership Test
5 in (1, 2, 3, 4, 5) = True
6 not in (1, 2, 3) = True

# Indexing
t = (10, 20, 30)
t[0] = 10
t[-1] = 30

# Slicing
t = (10, 20, 30, 40, 50)
t[1:4] = (20, 30, 40)
t[:3] = (10, 20, 30)
t[::2] = (10, 30, 50)
t[::-1] = (50, 40, 30, 20, 10)

# Length, Min, Max
len((1, 2, 3, 4)) = 4
min((10, 20, 5)) = 5
max((10, 20, 5)) = 20

# Conversion
list1 = [1, 2, 3]
tuple(list1) = (1, 2, 3)
tuple("hello") = ('h', 'e', 'l', 'l', 'o')

# Nested Tuples
t = ((1, 2), (3, 4))
t[1][0] = 3

# Modify tuple via list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)  # Result: (1, 2, 3, 4)

🔹 SET

Definition:
A Set is an unordered mutable collection that does not allow duplicates. Curly braces {} are used.

🧠 Example & Methods
numbers = {10, 20, 30, 40, 50}

1) numbers.add(60) = {10, 20, 30, 40, 50, 60}
2) numbers.update([70, 80]) = {10, 20, 30, 40, 50, 60, 70, 80}
3) numbers.remove(20)
4) numbers.discard(30)
5) numbers.pop()
6) temp = numbers.copy(); temp.clear()
7) a.union(b)
8) a.intersection(b)
9) a.difference(b)
10) a.symmetric_difference(b)
11) x.issubset(y)
12) y.issuperset(x)
13) m.isdisjoint(n)
14) y.copy()

🔹 DICT

Definition:
A Dictionary is an unordered mutable collection of key-value pairs. Duplicate keys are not allowed.

🧠 Example & Built-in Methods
person = {"name": "Alice", "age": 25, "city": "Chennai"}

# Adding/Updating
person["email"] = "alice@example.com"
person.update({"age": 26, "city": "Chennai"})

# Accessing
person.get("name")
person.setdefault("age", 30)

# Keys, Values, Items
person.keys()
person.values()
person.items()

# Copy & Clear
temp = person.copy()
temp.clear()

🔹 Python Data Types – Quick Comparison
Data Type	Ordered	Mutable	Allows Duplicates	Syntax
List	✅ Yes	✅ Yes	✅ Yes	[ ]
Tuple	✅ Yes	❌ No	✅ Yes	( )
String	✅ Yes	❌ No	✅ Yes (chars)	" " or ' '
Set	❌ No	✅ Yes	❌ No	{ }
🔹 Python Conditional Statements (if, elif, else)

Definition:
Used to make decisions in a program.

if condition:
    # code if True
elif another_condition:
    # code if first is False & this is True
else:
    # code if all False


Example:

age = 20
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

🔹 Python Nested if Statements

Definition:
Writing one if inside another for multiple related checks.

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative Number")

🔹 Python match-case (Switch Case)

Definition:
Introduced in Python 3.10 as an alternative to multiple if-elif-else.

match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default


Example:

day = "3"
match day:
    case "1": print("Monday")
    case "2": print("Tuesday")
    case "3": print("Wednesday")
    case _: print("Invalid day")

🔹 Python Loops

Definition: Loops repeat a block of code multiple times.

🌀 For Loop
for i in range(1, 6):
    print(i)


Prints numbers from 1 to 5.

Even numbers example:

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

🔄 While Loop
n = 5
total = 0
count = 1
while count <= n:
    total += count
    count += 1
print(total)  # 15

⭐ Nested Loops
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()


Output:

*
* *
* * *
* * * *
* * * * *

🔹 Python Loop Control Statements

Definition: Control the flow of loops.

🔹 break

Stops the loop immediately.

for i in range(1, 11):
    if i == 6:
        break
    print(i)
# Output: 1 2 3 4 5

🔹 continue

Skips the current iteration.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output: 1 2 3 4 6 7 8 9 10

🔹 pass

Does nothing — placeholder.

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print(i)
# Output: 1 3 5 7 9

⚙️ Summary

break → stop loop

continue → skip iteration

pass → do nothing