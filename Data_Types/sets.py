numbers = {10, 20, 30, 40, 50,10,20}
numbers.add(60)
print(numbers)

numbers.update((70, 80))
print(numbers)

numbers.remove(20)
print(numbers)

temp = numbers.copy()
print(temp)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))