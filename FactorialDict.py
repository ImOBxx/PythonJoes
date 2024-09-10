l = int(input("Enter Number: "))

# Initialize the dictionary to store factorials
factorials = {}

# Calculate factorials for numbers from 1 to l and store them in the dictionary
factorial = 1
for x in range(1, l + 1):
    factorial *= x
    factorials[x] = factorial

print("Factorials: ", factorials)

