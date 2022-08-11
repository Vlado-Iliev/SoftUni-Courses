def is_number_prime(number):
    if number <= 1:
        return False
    for n in range(2,number):
        if number % n == 0:
            return False

    return True


def get_primes(number_list):
    for number in number_list:
        if is_number_prime(number):
            yield  number
        continue



print(list(get_primes([-2, 0, 0, 1, 1, 0])))