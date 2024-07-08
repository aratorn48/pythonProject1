my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print (my_dict)
print (my_dict['Vasya'])
print (my_dict.get('Misha'))
my_dict.update({'Vera': 1987, 'Igor': 1956})
print (my_dict)
V = my_dict.pop('Vera')
print(V)
print(my_dict)

my_set = {1, 'Яблоко', 42.3141, 'Яблоко', 42.314}
print(my_set)
my_set.update({23, 'banana', 48.48})
my_set.discard('Яблоко')
print(my_set)
