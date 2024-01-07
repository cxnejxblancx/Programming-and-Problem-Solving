# input
num_rows = int(input("Rows: "))
num_columns = int(input("Columns: "))

# for-loop
for row in range(1, (num_rows + 1)): #[1, num_rows] inclusive
    for column in range(1, (num_columns + 1)): #[1, num_columns] inclusive
        power = (column) ** (row)
        print(power, end = "\t")
    print() #prints the next iteration through the row on a separate line
