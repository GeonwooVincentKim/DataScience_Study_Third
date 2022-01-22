import tqdm
import random
from typing import List


for i in tqdm.tqdm(range(100)):
    _ = [random.random() for _ in range(1000000)]
    

def primes_up_to(n: int) -> List[int]:
    primes = [2]

    with tqdm.trange(3, n) as t:
        for i in t:
            # If `i` does not divide to minority which is smaller.
            i_is_prime = not any(i % p == 0 for p in primes)
            print("I-Is-Prime -> {0}".format(i_is_prime))

            if i_is_prime:
                primes.append(i)

            t.set_description(f"{len(primes)} primes")
    
    return primes


my_primes = primes_up_to(100_000)
print("My Primes -> {0}".format(my_primes))
