#!/usr/bin/python3
"""Prime game involving two players"""


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


def remove_multiples(lst, x):
    """Removes multiple primes"""
    for i in range(2, len(lst)):
        try:
            lst[1 * x] = 0
        except (IndexError, ValueError):
            break
