l1=[12,34,545,25,56,356,8789,4678,65,578]
maximum=-float("inf")
minimum=float("inf")
for i in l1:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
difference=maximum-minimum
print(f"dufference of maximum and minimum is {difference}")