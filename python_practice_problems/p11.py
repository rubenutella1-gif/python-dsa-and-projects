try:
    m=int(input("Enter no of rows"))
    n=int(input("Enter no of columns"))
    a=[]
    for i in range(m):
        row=[]
        for j in range(n):
            val=int(input(f"Enter value at({i},{j})"))
            row.append(val)
        a.append(row)
    print("Matrix is :")
    for i in range(m):
        for j in range(n):
            print(a[i][j],end=" ")
        print()
except:
    print("Invalid input")