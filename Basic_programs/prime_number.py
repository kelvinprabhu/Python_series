def is_prime(n: int) -> bool:
    """check the number is prime"""
    if n<= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    """Why do we do this?

👉 Observation:
Any integer greater than 3 can be written in the form of 6k ± 1.

Multiples of 2 are even.

Multiples of 3 are divisible by 3.

So, after eliminating 2 and 3, any other prime number must be one more or less than a multiple of 6.

Examples:

5 = 6×1 − 1 ✅ prime

7 = 6×1 + 1 ✅ prime

11 = 6×2 − 1 ✅ prime

13 = 6×2 + 1 ✅ prime

17 = 6×3 − 1 ✅ prime

19 = 6×3 + 1 ✅ prime

But numbers like 6, 8, 9, 10, 12 are all divisible by 2 or 3 already, so we skip them."""

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
