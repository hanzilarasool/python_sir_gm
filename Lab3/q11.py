def generate2dArray(m, n):
    array = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(i * j)
        array.append(row)
    return array

# Prompt user for the number of rows and columns
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Generate the 2D array with the specified dimensions
result = generate2dArray(rows, columns)

# Print the resulting 2D array
for row in result:
    print(row)
