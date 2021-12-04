import sys

sys.path.append("..")
import utils_func

def get_oxygen_generator_rating(binaries, index) -> list:
    if len(binaries) == 1:
        return binaries
    one_bit_list = []
    zero_bit_list = []
    for binary in binaries:
        if binary[index] == '1':
            one_bit_list.append(binary)
        elif binary[index] == '0':
            zero_bit_list.append(binary)
    if len(one_bit_list) >= len(zero_bit_list):
        return get_oxygen_generator_rating(one_bit_list, index + 1)
    else:
        return get_oxygen_generator_rating(zero_bit_list, index + 1)

def get_co2_scrubber_rating(binaries, index) -> list:
    if len(binaries) == 1:
        return binaries
    one_bit_list = []
    zero_bit_list = []
    for binary in binaries:
        if binary[index] == '1':
            one_bit_list.append(binary)
        elif binary[index] == '0':
            zero_bit_list.append(binary)
    if len(zero_bit_list) <= len(one_bit_list):
        return get_co2_scrubber_rating(zero_bit_list, index + 1)
    else:
        return get_co2_scrubber_rating(one_bit_list, index + 1)
        
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
    print(int(get_oxygen_generator_rating(lines, 0)[0], 2) * int(get_co2_scrubber_rating(lines, 0)[0], 2))
    # 7440311
    return 0

if __name__ == '__main__':
    sys.exit(main())