counter = 0
total_miles = 0
total_gallons = 0
while True:
    gallons = float(input("Enter number of gallons used (input negative number to end script): "))
    if gallons < 0:
        print(f"The average miles/gallon for the above tanks are: {total_miles/total_gallons:.5f}.")
        break
    miles = float(input("Enter number of miles driven: "))
    total_miles = total_miles + miles
    total_gallons = total_gallons + gallons
    miles_per_gallon = miles/gallons
    print(f"The miles/gallon is {miles_per_gallon:.5f}.")  