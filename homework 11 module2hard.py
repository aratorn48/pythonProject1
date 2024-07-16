import random

n = random.randint(3, 20)
print(n)

result = []
for i in range(1, 11):
    for j in range(1, 11):
        x = i + j
        if x % n == 0:
            result.append((i, j))
            print(result)

