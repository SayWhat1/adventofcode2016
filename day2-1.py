class Keypad:

    def __init__(self, start=5):
        """Set the number of the keypad to start on."""
        self.position = start
        self.above = {1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6}
        self.below = {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 7, 8: 8, 9: 9}
        self.onRight = {1: 2, 2: 3, 3: 3, 4: 5, 5: 6, 6: 6, 7: 8, 8: 9, 9: 9}
        self.onLeft = {1: 1, 2: 1, 3: 2, 4: 4, 5: 4, 6: 5, 7: 7, 8: 7, 9: 8}

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
