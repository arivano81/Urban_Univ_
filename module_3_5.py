def get_multiplied_digits (number):
    number = str(int(number))
    if len(number) == 1 and number[0] != '0':
        return int(number)
    elif len(number) == 1 and number[0] == '0':
        return 1
    else:
        return int(number[0]) * get_multiplied_digits(str(number)[1:])

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
