try:
    n=int(input("Enter n value : "))
    arr=list(map(int,input("Enter array of elements : ").split()))
    k=int(input("Enter k value : "))
    
except ValueError:
    print("Invalid input ")