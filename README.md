# Python_Fundamentals
This is for python Functions Scudo-codes and build in functions and methods
## LIST  
Def: List is kind of array use to store the multipule values with different data-types
## Build in Methods
age = [25, 30, 35, 25, 30, 455]

1) age.append(10) = [25, 30, 35, 25, 30, 455, 10]
2) age.extend([500, 600]) = [25, 30, 35, 25, 30, 455, 10, 500, 600]
3) age.insert(2, 99) = [25, 30, 99, 35, 25, 30, 455, 10, 500, 600]
4) age.remove(25) = [30, 99, 35, 25, 30, 455, 10, 500, 600]
5) age.pop() = removes last element → [30, 99, 35, 25, 30, 455, 10, 500]
6) age.pop(1) = removes element at index 1 → [30, 35, 25, 30, 455, 10, 500]
7) age.clear() = []
8) age = [25, 30, 35, 25, 30, 455]
   age.index(35) = 2
9) age.count(30) = 2
10) age.sort() = [25, 25, 30, 30, 35, 455]
11) age.sort(reverse=True) = [455, 35, 30, 30, 25, 25]
12) age.reverse() = [25, 25, 30, 30, 35, 455] → [455, 35, 30, 30, 25, 25]
13) age.copy() = [25, 30, 35, 25, 30, 455]

## List Slicing Examples

14) age[1:4] = elements from index 1 to 3 → [30, 35, 25]
15) age[:3] = first 3 elements → [25, 30, 35]
16) age[2:] = elements from index 2 to end → [35, 25, 30, 455]
17) age[-1] = last element → 455
18) age[-3:] = last 3 elements → [25, 30, 455]
19) age[::2] = every 2nd element → [25, 35, 30]
20) age[::-1] = reversed list → [455, 30, 25, 35, 30, 25]



## String
It is the combination of unicode characters closed with singel r double cots,Its is immutabule once created cant be modifiled.

## BUILD IN METHODS
1) string.capitalize() = "Hello world"
   → Converts first character to uppercase.

2) string.upper() = "HELLO WORLD"
   → Converts all characters to uppercase.

3) string.lower() = "hello world"
   → Converts all characters to lowercase.

4) string.title() = "Hello World"
   → Capitalizes first letter of each word.

5) string.swapcase() = "HELLO WORLD" → "hello world" or vice versa.
   → Swaps upper to lower and lower to upper.

6) string.count('l') = 3
   → Counts occurrences of a substring.

7) string.find('world') = 6
   → Returns the first index where substring is found, -1 if not found.

8) string.index('world') = 6
   → Same as find(), but raises an error if substring not found.

9) string.replace('world', 'Python') = "hello Python"
   → Replaces substring with another.

10) string.split() = ['hello', 'world']
    → Splits string into list based on whitespace (default) or given delimiter.

11) " ".join(['hello', 'world']) = "hello world"
    → Joins list elements into a single string separated by space.

12) string.strip() = "hello world"
    → Removes whitespace from both ends.

13) string.lstrip() = removes spaces from left side only.

14) string.rstrip() = removes spaces from right side only.

15) string.startswith('he') = True
    → Checks if string starts with given substring.

16) string.endswith('ld') = True
    → Checks if string ends with given substring.

17) string.isalpha() = False
    → True if all characters are alphabets (no spaces or numbers).

18) string.isdigit() = False
    → True if all characters are digits.

19) string.isalnum() = False
    → True if all characters are alphabets or digits (no spaces).

20) string.isspace() = False
    → True if string contains only whitespace.

21) string.islower() = True
    → True if all characters are lowercase.

22) string.isupper() = False
    → True if all characters are uppercase.