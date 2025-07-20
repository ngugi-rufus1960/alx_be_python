size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle the rows
while row < size:
    # Use a for loop to print the stars in each row
    for col in range(size):
        print("*", end="")
    print()
    row += 1
