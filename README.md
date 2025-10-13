# Python_Fundamentals
This is for python Functions Scudo-codes and build in functions and methods
<!-- LIST -->
Def: List is kind of array use to store the multipule values with different data-types
<!-- Build in Methods -->
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
