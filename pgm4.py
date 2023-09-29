print("-----List operations------")
nums = list(range(5))
print('Displaying list nums[]: ', nums)
nums[4] = 'test'
print("List consisting of different datatypes : ", nums)
nums.append('programs')
print("After inserting string /'programs' to the end of list nums: ", nums)

print('------Sublist of list nums-------')
print('A slice from index 2 to 4: ', nums[2:4])
print('A slice from index 2 to the end: ', nums[2:])
print('A slice of the whole list: ', nums[:])
nums[4:] = [8, 9]
print('After assigning a new sublist to nums: ')

for idx, val in enumerate(nums):
    print('Index:{} , value:{}'.format(idx, val))

print("Square of even numbers in nums list")
sqrs = [x**2 for x in nums if x % 2 == 0]
print(sqrs)
