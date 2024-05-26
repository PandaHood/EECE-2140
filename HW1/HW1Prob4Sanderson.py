p = int(input("What value for p? "))
q = int(input("What value for q? "))
n = 0
x = 0
while True:
    x =  n * (n+1)
    if q < x:
        break
    if p <= x or q == x:
        print(f"{n}: {x}")
    n += 1  