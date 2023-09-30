def get_primes(numbers: list):
    def is_prime(num):
        if num <= 0 or num == 1:
            return False
        for i in (i for i in range(2,num)):
            if not num % i:
                return False
        return True
    return (i for i in numbers if is_prime(i))

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))
