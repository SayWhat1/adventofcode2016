"""Module to find real rooms in data and sum their sector IDs."""


def main():
    """Run the main function."""
    with open('data/day4data.txt', 'r') as f:
        dataList = f.readlines()

    realRoomList = []
    roomNames = []
    sum = 0

    for line in dataList:
        data = line.strip("\n").split('-')
        name = '-'.join(data[:-1])
        id, checkSum = data[-1].strip(']').split('[')

        nameCheck = {}

        check = [item for sublist in name.split('-') for item in sublist]

        for i in check:

            if i not in nameCheck.keys():
                nameCheck[i] = 1
            else:
                nameCheck[i] += 1
        nameCheck = sorted(nameCheck.iteritems(), key=lambda x: x[0])
        nameCheck = sorted(nameCheck, key=lambda x: x[1], reverse=True)
        nameCheck = [i[0] for i in nameCheck]
        if ''.join(nameCheck[0:len(checkSum)]) == checkSum:
            realRoomList.append((name, id))

    for room in realRoomList:
        encriptedName = room[0]
        decriptedName = []
        for i in encriptedName:
            decriptedName.append(decriptLetter(i, room[1]))
        sum += int(room[1])
        roomNames.append([''.join(decriptedName), room[1]])
    for i in roomNames:
        print('{}').format(i)
    print(sum)


def decriptLetter(c, shift):
    """Decript a letter using the shift cipher."""
    if c == '-':
        return ' '
    return chr((((ord(c) - 97) + int(shift)) % 26) + 97)


if __name__ == '__main__':
    main()
