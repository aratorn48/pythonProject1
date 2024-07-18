def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [48, 'Urban', False]
value_dict = {'a': 99, 'b': 'Kapybara', 'c': [True, False]}

print_params(*values_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)