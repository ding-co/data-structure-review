# Lists
xs = [3, 1, 2]          # Create a list
print(xs, xs[2])        # Prints [3, 1, 2] 2
print(xs[-1])           # Negative indices count from the end of the list; Prints 2
xs[2] = 'foo'           # Lists can contain elements of different types
print(xs)               # Prints [3, 1, 'foo']
xs.append('bar')        # Add a new element to the end of the list
print(xs)               # Prints [3, 1, 'foo', 'bar']
x = xs.pop()            # Remove and return the last element of the list
print(x, xs)            # 'bar' [3, 1, 'foo']

# Slicing
nums = list(range(5))   # range is a built-in function that creates a list of integers
print(nums)             # Prints [0, 1, 2, 3, 4]
print(nums[2:4])        # Get a slice from index 2 to 4 (exclusive); Prints [2, 3]
print(nums[2:])         # Get a slice from index 2 to the end; Prints [2, 3, 4]
print(nums[:2])         # Get a slice from the start to index 2 (exclusive); Prints [0, 1]
print(nums[:])          # Get a slice of the whole list; Prints [0, 1, 2, 3, 4]
print(nums[:-1])        # Slice indices can be negative; Prints [0, 1, 2, 3]
nums[2:4] = [8, 9]      # Assign a new sublist to a slice
print(nums)             # Prints [0, 1, 8, 9, 4]
