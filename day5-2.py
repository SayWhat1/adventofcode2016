"""Module to find the passowrd on a bunny door."""


import hashlib
from collections import OrderedDict


def main():
    """Run the main function."""
    id = 'cxdnnyjw'
    password = OrderedDict((i, 'x') for i in '01234567')
    begin = '00000'
    index = 0

    while 'x' in password.values():
        test = id + str(index)
        if begin == hashlib.md5(test).hexdigest()[0:5]:
            if hashlib.md5(test).hexdigest()[5] not in password.keys():
                index += 1
                continue
            if password[hashlib.md5(test).hexdigest()[5]] == 'x':
                password[hashlib.md5(test).hexdigest()[5]] = hashlib.md5(test).hexdigest()[6]
        if index % 1000000 == 0:
            print('Loop number: {}  Password: {}'.format(index, ''.join(password.values())))
        index += 1
    print('The password is: {}'.format(''.join(password.values())))


if __name__ == '__main__':
    main()
