l = [1,2,3,4,5]
add = 0
mul = 1
for i in l:
    add+=i
    mul*=i
print(f"Sum of {l} = {add} \n Mul of P{l} ={mul}")


l = [1,2,3,4,5]
for i in l:
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

t =(21,4,65,89,38,80,3)
print(f"Max:{max(t)} \nMin:{min(t)}")


l = [10, 20, 10, 30, 20, 10]

for i in l:
    print(f"{i} count is :{l.count(i)}")


l = [1,2,2,3,4,5,6]
l1 = set(l)
print(l1)

l = [122, 23, 33, 42, 5, 56]
L = len(l)-1
while L>=0:
    print(l[L])
    L-=1


init =0
limit =50
while init<=50:
    if init%3==0 and init%5==0:
        print(f"{init} is divisible by both 3 and 5 ")
    init+=1

t = (1,3,4)
t1 = (1,3,2,4)
if t==t1:
    print(f"{t}\n{t1}\nare identical")
else:
    print(f"{t}\n{t1}\nare not identical")


l =  [5, 10, 15, 20, 25]
l.append(30)
l.remove(10)
l.insert(1,12)
print(l)

init = 1
limit = 5
while init<=limit:
    for i in range(0,init):
        print('*',end=" ")
    print("")
    init+=1