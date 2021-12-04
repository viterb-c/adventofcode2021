import sys

sys.path.append("..")
import utils_func

def parse_numbers_bingo(line: str) -> list:
    return [int(i) for i in line.split(',')]

def get_board(i: int, boards: list, lines: list) -> int:
    board = []
    while i < len(lines) and len(lines[i]) > 0:
        board.append([int(i) for i in lines[i].split()])
        i += 1
    boards.append(board)
    return i

def parse_boards(lines: list) -> list:
    boards = []
    i = 1
    while i < len(lines):
        if len(lines[i]) > 0:
            i = get_board(i, boards, lines)
        i += 1
    return boards

def check_line(numbers: list, line: list) -> bool:
    for i in range(0, len(line)):
        if line[i] not in numbers:
            return False
    return True

def check_column(i: int, numbers: list, board: list) -> bool:
    for j in range(0, len(board)):
        if board[j][i] not in numbers:
            return False
    return True

def is_board_valid(numbers: list, board: list) -> bool:
    for i in range(0, len(board)):
        if check_line(numbers, board[i]):
            print('check_line', board[i])
            return True
        if check_column(i, numbers, board):
            print('check_column', i)
            return True
    return False

def find_board_numbers(numbers: list, boards: list) -> list:
    winning_boards = []
    i_number = 4
    while i_number < len(numbers) and len(boards) != len(winning_boards):
        i_number += 1
        for i_board in range(0, len(boards)):
            if i_board not in winning_boards and is_board_valid(numbers[0:i_number], boards[i_board]):
                winning_boards.append(i_board)
    return (boards[winning_boards[-1]], numbers[0:i_number])

def get_final_score(tuple) -> int:
    winning_board = tuple[0]
    numbers = tuple[1]
    unmarked = 0
    print(winning_board)
    print(numbers)
    for i in range(0, len(winning_board)):
        for j in range(0, len(winning_board[i])):
            if winning_board[i][j] not in numbers:
                unmarked += winning_board[i][j]
    return unmarked * numbers[-1]

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    numbers = parse_numbers_bingo(lines[0])
    boards = parse_boards(lines)
    board_numbers = find_board_numbers(numbers, boards)
    print(get_final_score(board_numbers))
    # 12080
    return 0

if __name__ == '__main__':
    sys.exit(main())