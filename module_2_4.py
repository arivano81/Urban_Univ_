numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes= []
for number in numbers:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            not_primes.append(number)
            break
    if is_prime and number!=1:
        primes.append(number)
print(numbers)
print('Primes: ', primes)
print('Not primes: ', not_primes)
