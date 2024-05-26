def sum_product(*n,in_mode = 0):
    list_sum_product = [*n]
    sum_product_n = 1
    if in_mode == 0:
        sum_product_n = sum(list_sum_product)
        min_max = min(list_sum_product)
    else:
        for number in list_sum_product:
            sum_product_n = sum_product_n * number
        min_max = max(list_sum_product)
    return sum_product_n, min_max

sum_or_product, min_or_max = sum_product(-1,1,2,3,5,6,7, in_mode = 0)
print(f'Sum/Product:{sum_or_product} and the Min/Max:{min_or_max}')

