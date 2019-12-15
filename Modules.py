import random

def generate_number(min, max):
    return random.randint(min,max)

print(generate_number(2,200))


for i, n in enumerate(range(20)):
    print(n, generate_number(2, 200))
