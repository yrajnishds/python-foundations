x = 10  # Global variable

def show():
    y = 5  # Local variable
    print("Inside function:", x, y)

show()
print("Outside function:", x)