"""This module checks how many valid triangles are in the input data."""


def main():
    """Run main function."""
    with open('data/day3data.txt', 'r') as f:
        input = f.readlines()

    triangleList = [map(int, i.strip('\n').split()) for i in input]

    triangles = []

    for line in triangleList:
        if(isTriangle(line)):
            triangles.append(line)
    print('There are {} valid triagles.').format(len(triangles))


def isTriangle(input):
    """Check if list of three sides is a triangle."""
    if 2*max(input) < sum(input):
        return True
    return False


if __name__ == '__main__':
    main()
