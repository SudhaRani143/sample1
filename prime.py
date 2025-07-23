def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # We only need to check up to the square root because if a number 'n' has a divisor 'd' greater than sqrt(n),
    # then it must also have a divisor 'n/d' which is less than sqrt(n).
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

def find_primes_in_range(start, end):
    """
    Finds all prime numbers within a specified range (inclusive).
    """
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Find and print prime numbers from 1 to 100
primes_1_to_100 = find_primes_in_range(1, 100)
print(f"Prime numbers from 1 to 100 are: {primes_1_to_100}")
