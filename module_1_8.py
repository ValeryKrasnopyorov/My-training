my_dict = {'Valery': 1989, 'Michail': 1988, 'Alexandr': 1986}
print(my_dict)
print(my_dict['Valery'])
my_dict['Pavel'] = 1980
print(my_dict)
print(my_dict.get('Andrey'))
my_dict.update({'Vasily': 1978, 'Artem': 1992})
print(my_dict)
del my_dict['Michail']
print(my_dict)
my_set = {1, 'a', 1, 'a', 2, 'b'}
print(my_set)
list = [1, 'a', 1, 'a', 2, 'b']
list = my_set
print(list)
print(list.add(3))
print(list.add('c'))
print(list)
print(list.discard(1))
print(list)