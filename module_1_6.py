my_dict = {'Artem': 1981, 'Maksim': 1999, 'Uliya': 2002}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Artem'])
print('Not existing value: ', my_dict.get('Maks', 'None'))
my_dict.update({'Maksimus': 2000, 'Elena': 2003})
print('Deleted value: ', my_dict.pop('Artem'))
print('Modified dictionary: ', my_dict)
# множества
my_set = {5, 'Kamal Singh', 5, 21.29, 'Kamal Singh'}
print('Set: ', my_set)
my_set.add(8)
my_set.add((1,2))
#   print('Modified set: ', my_set)
my_set.discard(8)
print('Modified set: ', my_set)
