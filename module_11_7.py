def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            print('Простое число')
        else:
            print('Составное число')
        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)