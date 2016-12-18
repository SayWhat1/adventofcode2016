"""Module to find real rooms in data and sum their sector IDs."""


def main():
    """Run the main function."""
    with open('data/day4data.txt', 'r') as f:
        dataList = f.readlines()

    sum = 0

    for line in dataList:
        data = line.strip("\n").split('-')
        name = [item for sublist in data[:-1] for item in sublist]
        id, checkSum = data[-1].strip(']').split('[')

        nameCheck = {}

        for i in name:
            if i not in nameCheck.keys():
                nameCheck[i] = 1
            else:
                nameCheck[i] += 1
        nameCheck = sorted(nameCheck.iteritems(), key=lambda x: x[0])
        nameCheck = sorted(nameCheck, key=lambda x: x[1], reverse=True)
        nameCheck = [i[0] for i in nameCheck]
        if ''.join(nameCheck[0:len(checkSum)]) == checkSum:
            sum += int(id)

    print('Sum of SectorId of valid rooms is {}.').format(sum)


if __name__ == '__main__':
    main()
