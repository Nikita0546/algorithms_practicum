def huffman_decode(codes, encoded_string):
    code_to_char = {code: char for char, code in codes.items()}

    decoded_string = ""
    current_code = ""
    
    for bit in encoded_string:
        current_code += bit
        if current_code in code_to_char:
            decoded_string += code_to_char[current_code]
            current_code = ""
    
    return decoded_string

def main():
    input_data = [
        "12 60",
        "' ': 1011",
        "'.': 1110",
        "'D': 1000",
        "'c': 000",
        "'d': 001",
        "'e': 1001",
        "'i': 010",
        "'m': 1100",
        "'n': 1010",
        "'o': 1111",
        "'s': 011",
        "'u': 1101",
        "100011110001001101000111111011001010011000010110011010111110"
    ]
    
    first_line = input_data[0].split()
    unique_char_count = int(first_line[0])
    encoded_size = int(first_line[1])
    
    codes = {}

    for line in input_data[1:unique_char_count + 1]:
        char, code = line.split(': ')
        codes[char.strip("'")] = code.strip()

    encoded_string = input_data[unique_char_count + 1]

    decoded_string = huffman_decode(codes, encoded_string)

    print(decoded_string)

if __name__ == "__main__":
    main()