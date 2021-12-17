import sys
sys.path.append("..")
from functools import reduce
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

def analyse_litteral_packet(packet: str, i: int, packets: list):
    tmp = packet[i:i+5]
    number = packet[i+1:i+5]
    print(packet[i:i+5])
    #packets.append(int(number, 2))
    while tmp[0] == '1':
        i += 5
        print(packet[i:i+5])
        number += packet[i+1:i+5]
        tmp = packet[i:i+5]
        print('packet:',packet[i:i+5])
    print(number, int(number,2))
    packets.append(int(number,2))
    return i + 5

def operation_on_packets(type: int, packets:list):
    print(type, packets)
    if type == 0:
        return sum(packets)
    elif type == 1:
        value = 1
        for x in packets:
            value *= x
        return value
    elif type == 2:
        return min(packets)
    elif type == 3:
        return max(packets)
    elif type == 5:
        return int(packets[0] > packets[1])
    elif type == 6:
        return int(packets[0] < packets[1])
    elif type == 7:
        return int(packets[0] == packets[1])

def analyse_packet(packet: str, start: int, packets_p: list):
    i = start
    type = int(packet[i + 3:i + 6], 2)
    i += 6
    if type == 4:
        return analyse_litteral_packet(packet, i, packets_p)
    else:
        packets = []
        length_type = int(packet[i:i+1],2)
        i += 1
        if length_type == 0:
            length = int(packet[i:i+15], 2)
            i += 15
            len_i = i
            while (i - len_i) < length:
                i = analyse_packet(packet, i , packets)
        elif length_type == 1:
            number = int(packet[i:i+11],2)
            i += 11
            sub_p = 0
            while sub_p < number:
                i = analyse_packet(packet, i, packets)
                sub_p += 1
        packets_p.append(operation_on_packets(type, packets))
    return i

def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    binary = convert_to_binary(lines[0])
    print(binary)
    versions = []
    analyse_packet(binary, 0, versions)
    print('Solution : {}'.format(sum(versions)))
    # 18234816469452
    # 37170285877507516
    return 0

if __name__ == '__main__':
    sys.exit(main())
