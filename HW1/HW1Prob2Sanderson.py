for side1 in range(1,5001):
    for side2 in range(side1,5001):
        for hyp in range(side2,5001):
            if (((side1**2) + (side2**2)) == (hyp**2)):
                print(f"The triple is {side1}, {side2}, {hyp}.", end=' ')
print()