# List loop
animals = ['cat', 'dog', 'monkey']
for animal in animals:
  print(animal)
# Prints cat dog monkey - each on its own line

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
  print("#%d: %s" % (idx + 1, animal))
  # Prints #1: cat #2: dog #3: monkey - each on its own line