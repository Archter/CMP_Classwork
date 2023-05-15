def is_prime(num):
    """Returns True if num is prime, False otherwise"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def print_primes(max_num):
    """Prints all prime numbers from 0 to max_num"""
    primes = []
    for num in range(2, max_num+1):
        if is_prime(num):
            primes.append(num)
    print(primes)

# Example usage
print_primes(20) # prints [2, 3, 5, 7, 11, 13, 17, 19]
