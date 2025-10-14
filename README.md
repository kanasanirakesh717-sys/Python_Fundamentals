# 🐍 Python_Fundamentals
This repository covers Python fundamentals including functions, pseudo-codes, and built-in methods for data types.

---

## 🔹 LIST  
**Definition:**  
List is a kind of array used to store multiple values with different data types.

### 🧠 Example & Built-in Methods
```python
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


## 🔹 STRING
**Definition:**  
A string is a combination of Unicode characters enclosed within single or double quotes.
It is immutable — once created, it cannot be modified.

### 🧠 Example & Built-in Methods
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



## 🔹 TUPLE
**Definition:**  
Tuple is like an array that is immutable and ordered.
Items are enclosed in parentheses ( ) and separated by commas.

### 🧠 Example & Built-in Methods
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

# Tuples are read-only; to modify, convert to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
# Result: t = (1, 2, 3, 4)


🔹 SET

Definition:
A Set is an unordered, mutable collection that does not allow duplicates.
Sets are written using curly braces {}.

numbers = {10, 20, 30, 40, 50}
print("Original Set:", numbers)

1) numbers.add(60) = {10, 20, 30, 40, 50, 60}
2) numbers.update([70, 80]) = {10, 20, 30, 40, 50, 60, 70, 80}
3) numbers.remove(20) = removes 20 from set
4) numbers.discard(30) = removes 30 if present (no error if absent)
5) numbers.pop() = removes a random element
6) temp = numbers.copy(); temp.clear() = set()
7) a.union(b) = combines unique elements
8) a.intersection(b) = common elements
9) a.difference(b) = elements only in a
10) a.symmetric_difference(b) = elements in either set, not both
11) x.issubset(y) = True if x ⊆ y
12) y.issuperset(x) = True if y ⊇ x
13) m.isdisjoint(n) = True if no common elements
14) y.copy() = shallow copy of set
