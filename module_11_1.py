def apply_all_func(int_list, *functions):
    result = {}
    for j in functions:
        result[j.__name__] = j(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min), end=" ")
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
