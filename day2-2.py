class Keypad:

    def __init__(self, start=5):
        """Set the number of the keypad to start on."""
        self.position = start
        self.above = {1: 1, 2: 2, 3: 1, 4: 4, 5: 5, 6: 2, 7: 3, 8: 4, 9: 9,
                      'A': 6, 'B': 7, 'C': 8, 'D': 'B'}
        self.below = {1: 3, 2: 6, 3: 7, 4: 8, 5: 5, 6: 'A', 7: 'B', 8: 'C',
                      9: 9, 'A': 'A', 'B': 'D', 'C': 'C', 'D': 'D'}
        self.onRight = {1: 1, 2: 3, 3: 4, 4: 4, 5: 6, 6: 7, 7: 8, 8: 9, 9: 9,
                        'A': 'B', 'B': 'C', 'C': 'C', 'D': 'D'}
        self.onLeft = {1: 1, 2: 2, 3: 2, 4: 3, 5: 5, 6: 5, 7: 6, 8: 7, 9: 8,
                       'A': 'A', 'B': 'A', 'C': 'B', 'D': 'D'}

    def up(self):
        """Move position up."""
        self.position = self.above[self.position]

    def down(self):
        """Move position down."""
        self.position = self.below[self.position]

    def right(self):
        """Move position right."""
        self.position = self.onRight[self.position]

    def left(self):
        """Move position left."""
        self.position = self.onLeft[self.position]

    def move(self, dir):
        """Move the position of your finger."""
        if dir.upper() == 'U':
            self.up()
        if dir.upper() == 'D':
            self.down()
        if dir.upper() == 'R':
            self.right()
        if dir.upper() == 'L':
            self.left()

    def getPos(self):
        """Return your fingers position."""
        return self.position


def main():
    """Run main function."""
    keypad = Keypad()
    code = []

    with open('data/day2data.txt', 'r') as f:
        moveList = f.readlines()

    for line in moveList:
        line.split()
        for move in line:
            keypad.move(move)
        code.append(keypad.getPos())
    print('Your bathroom access code is: {}').format(code)


if __name__ == '__main__':
    main()
