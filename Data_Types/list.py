a = [1, 2, 3]
b = a
b.append(4)
print(a)

nums = [2, 4, 6, 8]
nums2 = nums.copy()
nums2.pop(0)
print(nums)
print(nums2)


x = [10, 20, 30]
y = [40, 50, 60]
y+=x
print(y)

# remove the duplicates from list
data = [10, 20, 30, 10, 20, 40, 50,"Rakesh","Ravi","Rakesh"]
unique_data = []

for i in range(0,len(data)):
    if data[i] not in unique_data:
        unique_data.append(data[i])
print(unique_data)