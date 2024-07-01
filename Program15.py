# Impliment 2D array
r = int(input("Enter row size of array:\n"))
c = int(input("Enter column size of array:\n"))

array=[]

for i in range(r):
    arr=[] #is necessary to collect values row-wise before adding them to the main 2D list array
    for j in range(c):
        arr.append(input("Enter value\n"))
    array.append(arr)

for i in range(r):
    print()
    for j in range(c):
        print(array[i][j], end=" ")