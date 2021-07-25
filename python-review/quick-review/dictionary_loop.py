# Dictionary loop
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
  legs = d[animal]
  print('A %s has %d legs' % (animal, legs))
# Prints A person has 2 legs, A cat has 4 legs, A spider has 8 legs

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
  print('A %s has %d legs' % (animal, legs))
# Prints A person has 2 legs, A cat has 4 legs, A spider has 8 legs

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square) # Prints {0: 0, 2: 4, 4: 16}