#!/usr/bin/python3

"""
Method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compaer if key is idx or not in order to open
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        ischecked = False
        for idx in range(len(boxes)):
            ischecked = k in boxes[idx] and k != idx
            if ischecked:
                break
        if ischecked is False:
            return ischecked
    return True
