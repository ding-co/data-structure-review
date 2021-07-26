# list element: each student's score
# return each student's rank using list
# if score equal => rank equal
# ex) [30, 90, 90, 20] => return [3, 1, 1, 4]

def rank(list):
  rank = []
  for i in range(len(list)):
    count = 0
    for j in range(len(list)):
      if list[i] < list[j]:
        count += 1
    rank.append(count + 1)
  return rank

print(rank([1,2,3,4,5]))
print(rank([1,1,1,1,1]))
print(rank([1,1,5,3,4]))
print(rank([30, 50, 10, 90, 90]))

""" output example:
[5, 4, 3, 2, 1]
[1, 1, 1, 1, 1]
[4, 4, 1, 3, 2]
[4, 3, 5, 1, 1]
"""