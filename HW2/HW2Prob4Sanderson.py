# Function for summerize_letters 
def summerize_letters(string):
    string = string.lower()
    punc_space = " !,.:;?!'"
    unique_ele = []
    unique_ele_frq = []
    unique_dic = {}
    for elements in string:
        if elements not in punc_space:
            if elements not in unique_ele:
                unique_ele.append((elements))
                unique_ele_frq.append((elements, string.count(elements)))
                unique_dic[elements] = string.count(elements)
    return unique_ele_frq, unique_dic

# output of the two return variables
user_string = input("Put in a string! ")
ele_frq,uni = summerize_letters(user_string)
print(f'The list is {ele_frq}, and the dictionary is {uni}')

# Determining if all letters are in string
alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
uni_set = set()
for elements in uni:
    uni_set.add(elements)
uni_set = uni_set.symmetric_difference(alphabet)
if len(uni_set) == 0:
    print("The string has all the letters of the alphabet!") 
else:
    print('The string does not have all the letters of the alphabet.')




