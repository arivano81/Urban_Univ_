for element in range(3, 21):
    password = f'{element} - '
    for i in range(1, element):
        for j in range(i+1, element):
            if element % (i + j) == 0:
                password += f'{i}{j}'
    print(password)
