rowCountInput = input("Enter the number of rows: ")
columCountInput = input("Enter the number of columns: ")
rowCount = int(rowCountInput)
columCount = int(columCountInput)
print("Plotting shape for "+ str(rowCount) + " Rows and" + str(columCount) + " columns")
rowIndex = 2 * rowCount + 1
for row in range(rowIndex):
    for colum in range(1,columCount+1):
        if row == 0 :
            if colum % 2 == 1:
                print(" __ ", end = "")
            else:
                print("  ", end = "")
        elif row % 2 == 1:
            if colum % 2 == 1:
                print("/  \\", end = "")
            else:
                print("__", end = "")
        else:
            if colum % 2 == 1:
                print("\__/", end = "")
            else:
                print("  ", end = "")
    print("")


