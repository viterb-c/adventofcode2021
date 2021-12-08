import sys
import math

sys.path.append("..")
import utils_func

def get_fuel(distance: int):
    return distance * (1 + distance) // 2

def get_total_fuel(positions: list, destination: int) -> int:
    distances = [abs(position - destination) for position in positions]
    fuels = map(get_fuel, distances)
    return sum(fuels)

def fuel_crabs(positions: list):
    min_p = min(positions)
    max_p = max(positions)
    min_fuel = float('inf')
    for destination in range(min_p, max_p + 1):
        fuel = get_total_fuel(positions, destination)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(fuel_crabs([int(i) for i in lines[0].split(',')])))
    # 100347031
    return 0

if __name__ == '__main__':
    sys.exit(main())
