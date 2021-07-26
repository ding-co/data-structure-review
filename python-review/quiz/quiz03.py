# return max number in list
# len(list) >= 1
# list elements >= 0

def max(list):
  max_number = list[0]
  for element in list:
    if element > max_number:
      max_number = element
  return max_number

print(max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max([9, 4, 7, 5, 6, 2, 1, 0, 3, 8]))
print(max([2, 6, 8, 4, 9, 9, 8, 8, 8, 7]))
print(max([1]))

""" output example:
9
9
9
1
"""