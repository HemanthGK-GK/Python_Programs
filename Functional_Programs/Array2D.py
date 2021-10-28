#A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
def array():
    rows = int(input("Enter the number of rows"))
    columns = int(input("Enter the number of columns"))
    arr = []
    # For user input
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append(int(input("Enter the number")))
        arr.append(col)
    # For printing the array
    for i in range(rows): 
        for j in range(columns): 
            print(arr[i][j], end = " ") 
        print() 

#callling function
array()