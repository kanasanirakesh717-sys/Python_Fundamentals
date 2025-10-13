t = (1, 2, 3) 

print(t[1])

t = (5, 10, 15)
print(10 in t)

t = (1, 2, 3, 4, 5)
sum=0
for i in t:
    sum+=i
print(sum)

t = (1, 2, 3, 4, 5)
for i in range(len(t)):
    print(t[i] * 2)

t = ((1, 2), (3, 4), (5, 6))
for i in range(len(t)):
        for j in range (len(t[i])):
                print(t[i][j])

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)

t = (1, 2, 3)
s=t * 2
print(s)


t = ((1,2), (3,4), (5,6))
s =[]
for i in range(len(t)):
      for j in range(len(t[i])):
            s.append(t[i][j])
print(tuple(s))