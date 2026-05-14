# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Lekce 10: Prvočísla a jednoduché algoritmy v Pythonu (pracovní verze).

V tomto modulu budete krok za krokem implementovat různé algoritmy
pro testování prvočíselnosti a generování prvočísel:

ČÁST 1: Zbytek po dělení a základní test dělitelnosti
ČÁST 2: Triviální test prvočíselnosti
ČÁST 3: Generování prvočísel – jednoduchý přístup
ČÁST 4: Efektivnější test – dělení pouze do √n
ČÁST 5: Eratosthenovo síto
ČÁST 6: Porovnání výkonu algoritmů
ČÁST 7 (bonus): Prvočíselný rozklad a aplikace
ÚKOLY K PROCVIČENÍ: Další funkce na práci s prvočísly

Co se naučíte:
- použít zbytek po dělení pro test dělitelnosti,
- naivně i efektivněji testovat, zda je číslo prvočíslo,
- generovat všechna prvočísla do dané meze různými algoritmy,
- prakticky porovnat výkon odlišných implementací,
- rozložit číslo na prvočinitele a vidět souvislost s kryptografií,
- navrhnout vlastní pomocné funkce nad již napsanými algoritmy.
"""

from __future__ import annotations

import math
import time
from typing import List


##############################################################
### ČÁST 1: Zbytek po dělení a základní test dělitelnosti
##############################################################


def is_divisible(dividend: int, divisor: int) -> bool:
    """Check if one integer is divisible by another.

    This helper wraps the modulo operation and adds a guard against
    division by zero. It will be reused in later functions that
    implement primality tests.

    Args:
        dividend: The number to be divided.
        divisor: The potential divisor (should not be zero).

    Returns:
        True if dividend is divisible by divisor (remainder equals zero),
        otherwise False.

    Raises:
        ValueError: If divisor is zero.

    Example:
        >>> is_divisible(10, 2)
        True
        >>> is_divisible(10, 3)
        False
    """
    if divisor == 0:
        raise ValueError("Divisor nesmí být nula (dělení nulou není definováno).")
    return dividend % divisor == 0


##############################################################
### ČÁST 2: Triviální test prvočíselnosti
##############################################################


def is_prime_naive(n: int) -> bool:
    """Determine if a number is prime using a naive algorithm.

    This function checks divisibility by all integers from 2 to n-1.
    It is intentionally simple and inefficient for larger n to serve
    as a baseline for comparison with more advanced algorithms.

    Args:
        n: Integer to be tested.

    Returns:
        True if n is a prime number, False otherwise.

    Example:
        >>> is_prime_naive(2)
        True
        >>> is_prime_naive(15)
        False
        >>> is_prime_naive(17)
        True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if is_divisible(n, i):
            return False
    return True


##############################################################
### ČÁST 3: Generování prvočísel – jednoduchý přístup
##############################################################


def generate_primes_naive(limit: int) -> List[int]:
    """Generate a list of prime numbers up to a given limit (inclusive).

    This implementation uses the naive primality test `is_prime_naive`
    for each number from 2 to limit. It is easy to understand but becomes
    slow for larger limits.

    Args:
        limit: Upper bound (inclusive) for generated primes. Must be >= 2
            to produce any primes.

    Returns:
        A list of prime numbers up to the given limit.

    Example:
        >>> generate_primes_naive(10)
        [2, 3, 5, 7]
    """
    if limit < 2:
        return []
    primes = []
    for n in range(2, limit + 1):
        if is_prime_naive(n):
            primes.append(n)
    return primes


##############################################################
### ČÁST 4: Efektivnější test – dělení pouze do √n
##############################################################


def is_prime_sqrt(n: int) -> bool:
    """Determine if a number is prime using division up to sqrt(n).

    This function improves on the naive approach by only testing potential
    divisors up to and including floor(sqrt(n)). Any non-trivial divisor
    larger than sqrt(n) would necessarily be paired with a smaller divisor
    that we would have already encountered.

    Args:
        n: Integer to be tested.

    Returns:
        True if n is a prime number, False otherwise.

    Example:
        >>> is_prime_sqrt(2)
        True
        >>> is_prime_sqrt(15)
        False
        >>> is_prime_sqrt(17)
        True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if is_divisible(n, i):
            return False
    return True


##############################################################
### ČÁST 5: Eratosthenovo síto
##############################################################


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Generate primes up to a limit using the Sieve of Eratosthenes.

    The Sieve of Eratosthenes is a classic algorithm for finding all primes
    up to a given limit. It iteratively marks multiples of each prime,
    starting from 2, and the remaining unmarked numbers are primes.

    Args:
        limit: Upper bound (inclusive) for generated primes.

    Returns:
        A list of prime numbers up to the given limit.

    Example:
        >>> sieve_of_eratosthenes(10)
        [2, 3, 5, 7]
    """
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    sqrt_limit = math.isqrt(limit)
    for number in range(2, sqrt_limit + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


##############################################################
### ČÁST 6: Porovnání výkonu algoritmů
##############################################################


def benchmark_prime_algorithms(limit: int) -> None:
    """Benchmark different prime number generation algorithms.

    This function compares the running time of:
    - the naive prime generator `generate_primes_naive`, and
    - the Sieve of Eratosthenes `sieve_of_eratosthenes`.

    It prints the runtime of each approach in seconds and verifies that
    both algorithms produce the same list of primes.

    Args:
        limit: Upper bound (inclusive) for generated primes in the benchmark.

    Returns:
        None. The results are printed to the console.

    Example:
        >>> benchmark_prime_algorithms(1000)
        === Benchmark for limit = 1000 ===
        ...
    """
    print("=" * 45)
    print(f"=== Benchmark for limit = {limit} ===")
    print("=" * 45)

    start = time.perf_counter()
    primes_naive = generate_primes_naive(limit)
    elapsed_naive = time.perf_counter() - start

    start = time.perf_counter()
    primes_sieve = sieve_of_eratosthenes(limit)
    elapsed_sieve = time.perf_counter() - start

    print(f"generate_primes_naive:      {elapsed_naive:.6f} s")
    print(f"sieve_of_eratosthenes:      {elapsed_sieve:.6f} s")
    print(f"Výsledky jsou shodné:       {primes_naive == primes_sieve}")
    print(f"Počet nalezených prvočísel: {len(primes_sieve)}")


##############################################################
### ČÁST 7 (bonus): Prvočíselný rozklad a aplikace
##############################################################


def prime_factorization(n: int) -> List[int]:
    """Compute the prime factorization of a positive integer.

    The factorization is returned as a list of prime factors in non-decreasing
    order. For example, 12 -> [2, 2, 3]. The algorithm is simple but effective
    for moderately sized integers and reuses the idea of trial division up to
    sqrt(n).

    Args:
        n: Positive integer to be factorized.

    Returns:
        A list of prime factors in non-decreasing order. For n <= 1, returns
        an empty list.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> prime_factorization(1)
        []
        >>> prime_factorization(12)
        [2, 2, 3]
        >>> prime_factorization(13)
        [13]
    """
    if n < 0:
        raise ValueError("Záporná čísla nelze rozložit na prvočinitele.")
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2
    if n > 1:
        factors.append(n)
    return factors



##############################################################
### ÚKOLY K PROCVIČENÍ (bonusové návrhy)
##############################################################


def count_primes_in_interval(start: int, end: int) -> int:
    """Count how many primes are in a given inclusive interval.

    Suggested exercise:
    - Reuse one of the primality tests implemented above.
    - Think about input validation (what if start > end?).

    Args:
        start: Start of the interval (inclusive).
        end: End of the interval (inclusive).

    Returns:
        Number of primes in the interval.

    """
    if start > end:
        start, end = end, start
    count = 0
    for n in range(start, end + 1):
        if is_prime_sqrt(n):
            count += 1
    return count


def largest_prime_below(limit: int) -> int | None:
    """Find the largest prime number less than or equal to a limit.

    Suggested exercise:
    - Iterate from limit downward and return the first prime.
    - Consider what should happen for limit < 2.

    Args:
        limit: Upper bound for the search.

    Returns:
        The largest prime <= limit, or None if no such prime exists.

    """
    if limit < 2:
        return None
    for n in range(limit, 1, -1):
        if is_prime_sqrt(n):
            return n
    return None


def primes_with_fixed_digit_count(num_digits: int) -> List[int]:
    """Generate all primes with a fixed number of digits.

    Suggested exercise:
    - Compute the interval [10^(d-1), 10^d - 1] and search for primes there.
    - Discuss performance for larger numbers of digits.

    Args:
        num_digits: Number of decimal digits (must be >= 1).

    Returns:
        A list of primes that have exactly num_digits digits.

    """
    if num_digits < 1:
        return []
    lower = 10 ** (num_digits - 1) if num_digits > 1 else 2
    upper = 10 ** num_digits - 1
    primes = []
    for n in range(lower, upper + 1):
        if is_prime_sqrt(n):
            primes.append(n)
    return primes


##############################################################
### DEMONSTRAČNÍ MAIN BLOK
##############################################################


def _demo_basic() -> None:
    """Run a basic demonstration of the implemented functionality."""
    limit = 30
    print("=" * 50)
    print(f"Prvočísla do {limit} (naivní metoda):")
    print(generate_primes_naive(limit))

    print(f"\nPrvočísla do {limit} (Eratosthenovo síto):")
    print(sieve_of_eratosthenes(limit))

    print("\nTest prvočíselnosti (naivní vs. sqrt):")
    test_numbers = [1, 2, 3, 15, 17, 97, 100]
    for n in test_numbers:
        naive = is_prime_naive(n)
        sqrt  = is_prime_sqrt(n)
        print(f"  n={n:4d}: naivní={naive}, sqrt={sqrt}")

    print("\nPrvočíselný rozklad:")
    for n in [1, 12, 13, 60, 360, 97]:
        print(f"  {n} -> {prime_factorization(n)}")
    print("=" * 50)


if __name__ == "__main__":
    # PRO TESTOVÁNÍ: Odkomentujte postupně po implementaci jednotlivých částí.
    # Doporučené pořadí:
    #
    print(is_divisible(10, 2))
    print(is_prime_naive(17))
    print(generate_primes_naive(30))
    print(is_prime_sqrt(97))
    print(sieve_of_eratosthenes(50))
    benchmark_prime_algorithms(limit=10_000)
    print(prime_factorization(120))
    print(count_primes_in_interval(1, 100))
    print(largest_prime_below(100))
    print(primes_with_fixed_digit_count(2))
    _demo_basic()