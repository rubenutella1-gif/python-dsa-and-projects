# '''Star Patterns
#  Print star patterns like:
#  markdown
#  Copy
#  Edit
#  *
#  **
#  *** '''
'''for i in range(1,4):
     for j in range(i):
         print("*",end=" ")
     print()'''
#Print a square of stars (5x5).
'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()   ''' 
#Print an inverted triangle of stars:
'''****
   ***
   **
   *'''
'''n=4
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''
#Print a pyramid pattern of stars:
'''*
  ***
 *****'''
'''n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''
#Print numbers in a triangle pattern:
'''1
   12
   123
   1234'''
'''n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
'''n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()'''
""" n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print() """
n=int(input("Enter n value : "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()