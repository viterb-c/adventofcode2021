import sys

sys.path.append("..")
import utils_func

def binary_diagnostic(binaries) -> int:
    length_binary = len(binaries[0])
    binary_array = [0] * length_binary
    gamma_rate = ''
    epsilon_rate = ''

    for binary in binaries:
        for i in range(length_binary):
            binary_array[i] += int(binary[i])
    for i in range(length_binary):
        gamma_rate += '1' if binary_array[i] > len(binaries) / 2 else '0'
        epsilon_rate += '0' if binary_array[i] > len(binaries) / 2 else '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print("Solution : {}".format(binary_diagnostic(lines)))
    # 3959450
    return 0

if __name__ == '__main__':
    sys.exit(main())