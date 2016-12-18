class Path:
    """Class to handle turning and walking along a path."""

    def __init__(self, direction=0, x=0, y=0):
        """
        Set direction to NSEW and origin in x,y cordinates.

        N is positive y.
        """
        self.direction = direction
        self.x = x
        self.y = y

    def move(self, head, steps):
        """Turn in head and walk for steps."""
        self.turn(head)
        if self.direction == 0:
            self.x += int(steps)
        if self.direction == 1:
            self.y += int(steps)
        if self.direction == 2:
            self.x -= int(steps)
        if self.direction == 3:
            self.y -= int(steps)

    def turn(self, dir):
        """Turn in direction dir."""
        if dir.upper() == 'R':
            if self.direction == 3:
                self.direction = 0
            else:
                self.direction += 1
        if dir.upper() == 'L':
            if self.direction == 0:
                self.direction = 3
            else:
                self.direction -= 1

    def setX(self, x):
        """Set x position."""
        self.x = x

    def setY(self, y):
        """Set y position."""
        self.y = y

    def setXY(self, x, y):
        """Set x and y position"""
        self.x = x
        self.y = y


visited = []


def main():
    """Main function to run path."""
    moveList = ('R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, '
                'L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, '
                'R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, '
                'R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, '
                'R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, '
                'L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, '
                'L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, '
                'L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, '
                'R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, '
                'L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, '
                'R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, '
                'R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1')
    moveList = moveList.replace(' ', '').split(',')

    elf = Path()

    for move in moveList:
        start = [elf.x, elf.y]
        print('Elf turning {} and walking for {} steps.').format(
            move[0], move[1:])
        elf.move(move[0], move[1:])
        end = [elf.x, elf.y]
        if(addMoveToList(elf, start, end)):
            break
    print('Elf ended in position {},{}').format(elf.x, elf.y)
    print('Shortest distance from origin to EB HQ is: {}').format(
        abs(elf.x) + abs(elf.y))


def addMoveToList(path, start, end):
    """Add a move to the visisted list.

    Return True if the point is already in the visited list
    """
    if start[1] == end[1]:
        if start[0] > end[0]:
            for i in range(start[0], end[0], -1):
                if [i, end[1]] in visited:
                    print("Point: {}, {} already visited.").format(i, end[1])
                    visited.append([i, end[1]])
                    path.setXY(i, end[1])
                    path
                    return True
                visited.append([i, end[1]])
        else:
            for i in range(start[0], end[0]):
                if [i, end[1]] in visited:
                    print("Point: {}, {} already visited.").format(i, end[1])
                    visited.append([i, end[1]])
                    path.setXY(i, end[1])
                    return True
                visited.append([i, end[1]])

    else:
        if start[1] > end[1]:
            for i in range(start[1], end[1], -1):
                if [end[0], i] in visited:
                    print("Point: {}, {} already visited.").format(end[0], i)
                    visited.append([end[0], i])
                    path.setXY(end[0], i)
                    return True
                visited.append([end[0], i])

        else:
            for i in range(start[1], end[1]):
                if [end[0], i] in visited:
                    print("Point: {}, {} already visited.").format(end[0], i)
                    visited.append([end[0], i])
                    path.setXY(end[0], i)
                    return True
                visited.append([end[0], i])

    return False


main()
