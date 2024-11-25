calls = 0

def count_calls():
    global calls
    calls += 1

def string_info (string):
    str_len = len(string)
    str_upcase = string.upper()
    str_lowcase = string.lower()
    unswer = (str_len, str_upcase, str_lowcase)
    count_calls()
    return unswer

def is_contains(string, llist):
    unswer = False
    for i in llist:
        if i.lower() == string.lower():
            unswer = True
            break
        else:
            unswer = False
    count_calls()
    return unswer

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
