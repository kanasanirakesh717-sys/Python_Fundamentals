for i in range(1,11):
    if i ==6:
        break
    print(i)

for i in range(1,11):
    if i ==5:
        continue
    print(i)

for i in range(1,11):
    if i%2==0:
        pass
    else:
        print(i)


for i in range(1,21):
    if i>10:
        if i%2==0:
            print(i)

for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"{i}:FIZZBUZZ")
    elif i%5==0:
        print(f"{i}:BUZZ")
    elif i%3==0:
        print(f"{i}:FIZZ")
    else:
        print(i)
    
n = int(input("Enter the num"))
intial = 1
add=0
while intial<=n:
 if intial%2!=0:
     add+=intial
 intial+=1
print(add)