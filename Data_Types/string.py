s = "hello world"
print(s.upper())

s = "python"
print(s.capitalize())


s = "python programming"
print(s.count('p'))

print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
 
# for i in range(0,len(s)):
#     print(s[i])

word = "Hello World"

vowles = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in range(0,len(word)):
    if word[i] in vowles:
        count+=1
print(count) 

s = "PyThOn StrIng"
for i in range(0,len(s)):
    if s[i].isupper():
        print(f"{s[i]} is upper case")

print(s[::-1])

size = len(s)
while size>0:
    print(s[size-1],end="")
    size-=1

s="Python is amazing"
print(s.upper())

words = ["python", "java", "c++", "ruby"]
new_words = []
for i in range(0,len(words)):
    new_words.append(words[i].capitalize())
print(new_words)

s = "hello world"
vowles = ['a','e','i','o','u']
new_word = []
for i in range(0,len(s)):
    if s[i] in vowles:
        new_word.append("*")
    else:
        new_word.append(s[i])
print("".join(new_word))

s = "hello world hello"
print(s.count("hello"))

s = "a1b2c3d4"
for i in range(0,len(s)):
    if s[i].isdigit():
        print(s[i],end=" ")


s = "racecar"
palindrome = s[::-1]
if s == palindrome:
    print(f"{s} is palindrome")

sentence = "Python is fun and Python is easy"
s=sentence.replace("Python","Java")
print(s)