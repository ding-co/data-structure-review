# Return: count numbers (> num in list)
# don't use len() function
# if count = 0 => return 0

def compare(list, num):
  count = 0
  for element in list:
    if element > num:
      count += 1
  return count

print(compare([0,1,2,3,4,5,6,7,8,9], 7))
print(compare([1,2,3,4,5,6,7,8,9,10], 0))
print(compare([], 0))
print(compare([1, 2, 3], 3))
print(compare([1,2,3,3,3,3,3,3,4], 2))
print(compare([1,2,3,3,3,3,3,3,4], 3))

""" output example:
2
10
0
0
7
1
"""