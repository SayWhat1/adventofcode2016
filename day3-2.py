"""This module checks how many valid triangles are in the input data."""


def main():
    """Run main function."""
    with open('data/day3data.txt', 'r') as f:
        input = f.readlines()

    dataList = [map(int, i.strip('\n').split()) for i in input]

    # Transpose the data.
    dataList = [list(i) for i in zip(*dataList)]

    # Flatten the list.
    triList = [item for sublist in dataList for item in sublist]

    triangles = 0

    for i in range(0, len(triList), 3):
        print([triList[i], triList[i + 1], triList[i + 2]])
        if isTriangle([triList[i], triList[i + 1], triList[i + 2]]):
            triangles += 1
    print('There are {} valid triagles.').format(triangles)


def isTriangle(input):
    """Check if list of three sides is a triangle."""
    if 2 * max(input) < sum(input):
        return True
    return False


if __name__ == '__main__':
    main()
