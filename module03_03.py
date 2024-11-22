def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(a = True, )
print_params(a = False, c = 'string')
print_params(b = 25, c = [1,2,3])

values_list = [5, 'five', False]
values_dict = {'a' : 'six', 'b' : 7, 'c' : 8.08}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['stay', True]
print_params(*values_list_2, 'everyday')