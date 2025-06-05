n = 6  

print("Lower Triangular:\n")
for i in range(1, n + 1):
    print("* " * i)


print("\nUpper Triangular:\n")
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)


print("\nPyramid:\n")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
