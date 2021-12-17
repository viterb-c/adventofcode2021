import sys
sys.path.append("..")

import utils_func.file

DICT_HEXA = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def convert_to_binary(hexa: str) -> str:
    binary = ''.join([DICT_HEXA[hex] for hex in hexa])
    return binary

def analyse_litteral_packet(packet: str, i: int):
    number = packet[i:i+5]
    while number[0] == '1':
        i += 5
        number = packet[i:i+5]
    return i + 5

def analyse_packet(packet: str, start: int, versions: list):
    i = start
    versions.append(int(packet[i:i + 3],2))
    i += 3
    type = int(packet[i:i + 3], 2)
    i += 3
    if type == 4:
        return analyse_litteral_packet(packet, i)
    else:
        length_type = int(packet[i:i+1],2)
        i += 1
        if length_type == 0:
            length = int(packet[i:i+15], 2)
            i += 15
            len_i = i
            while (i - len_i) < length:
                i = analyse_packet(packet, i , versions)
        elif length_type == 1:
            number = int(packet[i:i+11],2)
            i += 11
            sub_p = 0
            while sub_p < number:
                i = analyse_packet(packet, i, versions)
                sub_p += 1
    return i

def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    binary = convert_to_binary(lines[0])
    versions = []
    analyse_packet(binary, 0, versions)
    print('Solution : {}'.format(sum(versions)))
    # 986
    return 0

if __name__ == '__main__':
    sys.exit(main())
