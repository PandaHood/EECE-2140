import math
sums = 0
k = 1
n = 0
def dismember(number, dec_places):
    new_num = ((number * 10**(dec_places)//1)/(10**(dec_places)))
    return new_num

def print_table(input_table):
    for row in range(len(input_table)):
        for col in range(len(input_table[0])):
            print('|{:<8}|'.format(input_table[row][col]), end='')
        print()
            
table =[['N Value','Pi Value']]   
while k < 5:
    sums = sums + (((-1)**n)/(2*n + 1))
    pie = sums*4
    if n <= 10:
        table.append([n,format(pie,'.6f')])
        if n == 10:
            print_table(table)
    if dismember(3.14159, k) == dismember(pie, k):
        print(f'It takes {n} terms to first get {dismember(pie,k)}.')
        k += 1
    n += 1

    