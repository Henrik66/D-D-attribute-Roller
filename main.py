import random

def rollonetime():
  roll1 = [(random.randint(1,6))]
  for x in range (0, 4):
    roll1.append(random.randint(1,6))
  roll1.sort()

  summary = roll1[1] + roll1[2] + roll1[3]
  return summary

roll2=[]
for x in range (0, 6):
  roll2.append(rollonetime())

roll2.sort()
product = [roll2[5], roll2[4], roll2[3], roll2[2], roll2[1], roll2[0]]
print ("D&D charater main attributes:", product)
