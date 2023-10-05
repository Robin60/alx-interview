#!/usr/bin/python3
"""Prime game involving two players"""


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def winningPlayer(n):
    """
    If n is even, Maria wins because she starts first.
    If n is odd, Ben wins because he can mirror Maria's moves.
    """
    if n % 2 == 0:
        return "p1"
    else:
        return "p2"


def remove_multiples(lst, x):
    """Removes multiple primes"""
    for i in range(2, len(lst)):
        try:
            lst[1 * x] = 0
        except (IndexError, ValueError):
            break


def isWinner(x, nums):
    """Returns the winner of Prime game
       Args:
          x: rounds of the game
          nums: array of n
       Return: the winner
    """
    Maria = 0
    Ben = 0

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    al = [1 for x in range(sorted(nums)[-1] + 1)]
    al[0], al[1] = 0, 0
    for i in range(2, len(al)):
        remove_multiples(al, i)

    for n in nums:
        #prime_counts = sum(1 for i in range(1, n + 1) if isPrime)
        #winner = winningPlayer(prime_counts)
        
        if sum(al[0:i + 1]) % 2 != 0:
            Maria += 1
        else:
            Ben += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
