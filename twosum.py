import array as arr

a = arr.array('i',[2,7,11,15])

sum=0
target=9
def twosum():
    for i in range(len(a)):
        for j in range(i+1,len(a)):
                sum=a[i]+a[j]
                if sum == target:
                    return[i,j]
x = twosum()
print(x)

#Output [0, 1]

# less than O(n2) time complexity 

# target=6
# sum=0
# j = []
# for i in range(len(a)):
#     sum=target-a[i]
#     if sum in a:
#         j.append(i)
# print(j)      # Failde in case of Input: nums = [3,2,4], target = 6   Output: [1,2]
