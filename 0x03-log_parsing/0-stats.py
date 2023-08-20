#!/usr/bin/python3

import sys


def print_msg(dict_, file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(dict_.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
counter = 0
dict_ = {"200": 0,
         "301": 0,
         "400": 0,
         "401": 0,
         "403": 0,
         "404": 0,
         "405": 0,
         "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]
        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_.keys()):
                    dict_[code] += 1

            if (counter == 10):
                print_msg(dict_sc, file_size)
                counter = 0

finally:
    print_msg(dict_, file_size)
