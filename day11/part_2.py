import sys
import math

sys.path.append("..")
import utils_func

def is_in_cavern(x: int, y: int) -> bool:
    return x >= 0 and x < 10 and y >= 0 and y < 10

def increase_energy_neighbors(octopus, flashes, x, y):
    return  increase_energy(octopus, flashes, x - 1, y - 1) + \
            increase_energy(octopus, flashes, x - 1, y) + \
            increase_energy(octopus, flashes, x - 1, y + 1) + \
            increase_energy(octopus, flashes, x, y - 1) + \
            increase_energy(octopus, flashes, x, y + 1) + \
            increase_energy(octopus, flashes, x + 1, y - 1) + \
            increase_energy(octopus, flashes, x + 1, y) + \
            increase_energy(octopus, flashes, x + 1, y + 1)

def increase_energy(octopus: list, flashes: list,x: int, y: int) -> int:
    if is_in_cavern(x, y) == False or (x, y) in flashes:
        return 0
    flashes_neighbors = 0
    if octopus[y][x] < 9:
        octopus[y][x] += 1
        return 0
    octopus[y][x] = 0
    if (x, y) not in flashes:
        flashes.append((x, y))
        flashes_neigbours = increase_energy_neighbors(octopus, flashes, x, y)
    return 1 + flashes_neigbours

def get_total_flashes(octopus: list) -> int:
    step = 1
    while True:
        octopus_flashes = []
        for y in range(len(octopus)):
            for x in range(len(octopus[y])):
                increase_energy(octopus, octopus_flashes, x, y)
        if len(octopus_flashes) == 100:
            return step
        step += 1
    return flashes

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    octopus = []
    for line in lines:
        octopus.append([int(i) for i in line])
    print('Solution : {}'.format(get_total_flashes(octopus)))
    # 476
    return 0

if __name__ == '__main__':
    sys.exit(main())
