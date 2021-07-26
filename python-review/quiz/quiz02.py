# score >= 90: return A
# score >= 70: return B
# score >= 60: return C
# score >= 50: return D
# else: return F
# 0 <= score n <= 100

def grade(n):
  if n >= 90:
    return 'A'
  elif n >= 70:
    return 'B'
  elif n >= 60:
    return 'C'
  elif n >= 50:
    return 'D'
  else:
    return 'F'

for n in [100, 95, 27, 44, 56, 62, 50, 70, 0]:
    print("%3d --> %s" % (n, grade(n)))

""" output example:
100 --> A
 95 --> A
 27 --> F
 44 --> F
 56 --> D
 62 --> C
 50 --> D
 70 --> B
  0 --> F
"""