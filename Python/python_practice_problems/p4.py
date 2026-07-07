n=input().strip()
is_nagative=n[0]=='-'
n_string=n[1:] if is_nagative else n
reversed_n=n_string[::-1]
if is_nagative:
    reversed_n='-'+reversed_n
reversed_n=int(reversed_n)
print(reversed_n)
print(type(reversed_n))