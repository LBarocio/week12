# nested loop = a loop within another loop (outer, inner)
    # outer loop:
        # inner loop:

# for x in range(1, 10):
#     print(x)
# to put all the results on the same line 
# for x in range(1, 10):
#     print(x, end=" ")

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()

# to print a rectangle
rows = int(input("enter the # of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()