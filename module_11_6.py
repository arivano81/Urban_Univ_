def all_variants(text):
    length = len(text)
    for x in range(length):
        for y in range(x, length):
            yield text[y-x:y + 1]

a = all_variants("abc")
print(list(a))
for i in a:
    print(i)