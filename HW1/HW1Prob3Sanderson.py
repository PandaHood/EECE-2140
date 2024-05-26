cur_num = int(input("Is this number a palindrone? "))
num_digits = 0
cur_num_t = cur_num
cur_numf = cur_num
cur_numb = cur_num

while cur_num_t > 0:
    cur_num_t//=10
    num_digits += 1
while num_digits > 0:
    digitf = cur_numf//10**(num_digits-1)
    digitb = cur_numb%10
    if digitf != digitb:
        print("Not a palindrone")
        break
    cur_numb = cur_numb//10
    cur_numf = cur_numf - digitf*10**(num_digits-1)
    num_digits -= 1
else:
    print("Is a palindrone")