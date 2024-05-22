#Create lower triangular, upper triangular and pyramid containing the "*" character.
def lower_triangular(n):
    for i in range(n):
        print("* " * (i + 1))
def upper_triangular(n):
    for i in range(n, 0, -1):
        print("* " * i)
def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
n =5
print("Lower Triangular Pattern:")
lower_triangular(n)
print("\nUpper Triangular Pattern:")
upper_triangular(n)
print("\nPyramid Pattern:")
pyramid(n)