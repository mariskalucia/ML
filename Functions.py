# Functions
print("Functions")

def print_pi():
    print("3.14159")

def print_double(x):
    print(x * 2)

def get_pi():
    return 3,14159

def get_double(x):
    return x * 2

def get_greatest(x, y):
    if x > y:
        return x
    else:
        return y

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

if is_even(42) == True:
    print("Even!")
else:
    print("Odd!")
