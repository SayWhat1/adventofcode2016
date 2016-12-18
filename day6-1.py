"""Module to find out what Santa is trying to say."""

import collections

def main():
    """Run the main function."""
    with open('data/day6data.txt', 'r') as f:
        data = f.readlines()

    message = ''

    # Transpose the data!
    data = [list(i) for i in zip(*data)]

    for line in data:
        mostCommon = collections.Counter(line).most_common()
        print(mostCommon)
        message += mostCommon[0][0]
    print('Your message is: {}'.format(message))


if __name__ == '__main__':
    main()
