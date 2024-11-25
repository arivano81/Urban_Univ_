def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # 1.2
print_params(c = False) # 1.3
print_params(a = 2, c = False) # 1.3
print_params(b = 'строка2', a = 2,) # 1.3
print_params(b = 25) # 1.4
print_params(c = [1,2,3]) # 1.4
values_list = [10, 'стр', False] # 2.1
values_dict = {'a': 3, 'b': 'строка3', 'c': True} # 2.2
print_params(*values_list) # 2.3
print_params(**values_dict) # 2.3
values_list_2 = [54.32, 'Строка' ] # 3.1
print_params(*values_list_2, 42) # 3.2

