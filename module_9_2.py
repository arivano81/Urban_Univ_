def custom_write(file_name, strings):
    strings_positions = {}
    st = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            strings_positions[(st, file.tell())] = string
            file.write(string)
            file.write('\n')
            st += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
