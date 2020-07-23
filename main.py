import random

roll1 = [(random.randint(1,6))]

for x in range (0, 3):
  roll1.append(random.randint(1,6))

roll1.sort()

print (roll1)