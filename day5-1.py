"""Module to find the passowrd on a bunny door."""


import hashlib


def main():
    """Run the main function."""
    id = 'cxdnnyjw'
    password = []
    begin = '00000'
    index = 0

    while len(password) < 8:
        test = id + str(index)
        if begin == hashlib.md5(test).hexdigest()[0:5]:
            password.append(hashlib.md5(test).hexdigest()[5])
        index += 1
    print('The password is: {}'.format(''.join(password)))


if __name__ == '__main__':
    main()
