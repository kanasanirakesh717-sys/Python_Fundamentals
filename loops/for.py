for i in range(1,11):
    if i%2==0:
        print(i)
        
n= int(input("Enter a number: "))
add = 0
count = 1
while count<=n:
    add+=count
    count+=1
print(add)

n= int(input("Enter a number: "))
count = 1
while count<=n:
    for i in range(count):
        print("*",end=" ")
    count+=1
    print()