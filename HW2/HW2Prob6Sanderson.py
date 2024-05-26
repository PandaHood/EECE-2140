# Function returning reversed list anddictionary with freqencies for each number
def two_output_int(*ints):
    dic_frq = {}
    unique_num =[]
    for element in ints:
        if element not in unique_num:
            unique_num.append(element)
            dic_frq[element] = ints.count(element)
    unique_num = list(reversed(sorted(unique_num)))
    return dic_frq, unique_num

dic, uni = two_output_int(3,5,4,3,1,4,1,4,7)
print(f'The dictionary is {dic}, and the reversed sorted list is {uni}.')
print()

# Table for for numbers sorted with their frequencies 
print('{:<1}|'.format('Number:'),end='')
print('{:<1}'.format('Frequency:'))
for element in list(reversed(uni)):
    print('{:<7}|'.format(element),end='')
    print('{:<6}'.format(dic[element]))
print()

# The numbers not in the original list
not_in = set()
uni_set = set()
for elements in uni:
    uni_set.add(elements)
for elements in range(1,max(uni)+1):
    not_in.add(elements)
uni_set = uni_set.symmetric_difference(not_in)
print(f'The numbers not in the original list is/are {uni_set}')


