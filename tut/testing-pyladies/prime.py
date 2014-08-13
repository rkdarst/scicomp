
import math

def is_prime(n):
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
