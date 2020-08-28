from primesieve import *

def test_primes():
    primes(40)

test_primes()


# # Get an array of the primes <= 40
# >>>  primes(40)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# # Get an array of the primes between 100 and 120
# >>>  primes(100, 120)
# [101, 103, 107, 109, 113]

# # Get an array of the first 10 primes
# >>>  n_primes(10)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# # Get an array of the first 10 primes >= 1000
# >>>  n_primes(10, 1000)
# [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]

# # Get the 10th prime
# >>> nth_prime(10)
# 29

# # Count the primes below 10**9
# >>> count_primes(10**9)
# 50847534