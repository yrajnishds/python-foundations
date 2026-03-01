# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i * i)

print("Traditional:", squares)

# Pythonic way
squares_pythonic = [i * i for i in range(1, 6)]
print("Pythonic:", squares_pythonic)