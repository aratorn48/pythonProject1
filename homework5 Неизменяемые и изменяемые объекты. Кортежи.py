immutable_var = (1, 2, 'a', 'b')
print(immutable_var) # кортеж это "неизменяемый объект", если необходимо часть данных перевести в "изменяемые", их нужно отобразить в виде списка "[]".

immutable_var = (1, 2, ['a', 'b'])
immutable_var [2][1] = 'z'
print(immutable_var)


mutable_list = [1, 2, 'a', 'b']
mutable_list.append ('Modified')
print (mutable_list)
mutable_list [2] = 'z'
print(mutable_list)

