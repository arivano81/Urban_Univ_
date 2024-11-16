is_prime = False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes= []
for number in numbers:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            not_primes.append(number)
            break
        else:
            is_prime = True
    if is_prime:
        print(number)
