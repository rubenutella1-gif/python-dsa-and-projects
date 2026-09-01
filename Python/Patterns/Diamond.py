rows=int(input("Enter number of rows :"))
star="*"
spaces=" "
middle=(rows//2)+1
for i in range(1,rows+1):
    if i<=middle:
        no_of_spaces=spaces*(middle-i)
        no_of_stars=star*(2*i-1)
    else:
        no_of_stars=star*(2*(rows-i)+1)
        no_of_spaces=(spaces*(i-middle))
    print(no_of_spaces,no_of_stars)