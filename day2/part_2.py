import sys

sys.path.append("..")
import utils_func

class Submarine:
    def __init__(self):
        self.aim = 0
        self.horizontal_position = 0
        self.depth = 0

    def forward(self, value: int):
        self.horizontal_position += value
        self.depth += self.aim * value
    
    def down(self, value: int):
        self.aim += value
    
    def up(self, value: int):
        self.aim -= value


def navigate_submarine(intructions) -> int:
    submarine = Submarine()

    for i in range(len(intructions)):
        if intructions[i][0] == 'f':
            submarine.forward(int(intructions[i][8:]))
        elif intructions[i][0] == 'd':
            submarine.down(int(intructions[i][5:]))
        elif intructions[i][0] == 'u':
            submarine.up(int(intructions[i][3:]))
    return submarine.depth * submarine.horizontal_position

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print("Solution : {}".format(navigate_submarine(lines)))
    # 1463827010
    return 0

if __name__ == '__main__':
    sys.exit(main())