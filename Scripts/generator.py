import random
import numpy as np


def rand_float_range(start, end):
  return random.random() * (end - start) + start

while True:  # until a good sample was found
  s = [ rand_float_range(211, 302.8) for _ in range(2) ]
  v = 269.59 + (269.59 - (sum(s) / len(s))) * 2
  if 211 <= v <= 302.8:
    s.append(v)
    break
print(sum(s)/len(s))

print(s)

print(np.std(s))

PHB_MW=[1692, 1296, 1225, 1698, 331, 1645, 49, 1374]

#print(ss.mean([1.092,0.901,1.067]))
#print(ss.standard_deviation([1366,1358,1398]))
#print(ss.mean([1.349,1.309,1.533]))

#print(ss.mean([1366,1358,1398]))


y = [50.12698781491773, 48.974046381760544, 47.898965803321715]

randomlist = []
for i in range(0,23):
  n = random.randint(95,116)
  randomlist.append(n)

#print(randomlist)




