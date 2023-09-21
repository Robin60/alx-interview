#!/usr/bin/python3
""" determine the fewest number of coins needed to meet
    a given amount total """


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total
    Args:
        coins: pile of coins to meet a total
        total: given amount total to be met with fewest coin
    """

    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1
    count = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1

