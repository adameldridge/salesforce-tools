import re

# TODO: take input id as a parameter from command line
id_input = '001A000010khO8J'
print 'id_input: ' + id_input

# Split id into list of 5 character chunks
id_split = [id_input[i:i+5] for i in range(0, len(id_input), 5)]
print 'id_split: ' + str(id_split)

# Reverse the strings in split_id
id_split_reversed = [chunk[::-1] for chunk in id_split]
print 'id_split_reversed: ' + str(id_split_reversed)

# Convert uppercase chars to 1 and everything else to 0
id_split_binary = [re.sub(r'[a-z,0-9]', "0", chunk) for chunk in id_split_reversed]
id_split_binary = [re.sub(r'[A-Z]', "1", chunk) for chunk in id_split_binary]

print 'id_split_binary: ' + str(id_split_binary)

# Look up the corresponding char in the binary_char_lookup
binary_char_lookup = {
    "00000": "A", "00001": "B", "00010": "C", "00011": "D", "00100": "E",
    "00101": "F", "00110": "G", "00111": "H", "01000": "I", "01001": "J",
    "01010": "K", "01011": "L", "01100": "M", "01101": "N", "01110": "O",
    "01111": "P", "10000": "Q", "10001": "R", "10010": "S", "10011": "T",
    "10100": "U", "10101": "V", "10110": "W", "10111": "X", "11000": "Y",
    "11001": "Z", "11010": "0", "11011": "1", "11100": "2", "11101": "3",
    "11110": "4", "11111": "5"
}

id_split_mapped = [binary_char_lookup[chunk] for chunk in id_split_binary]
print 'id_split_mapped: ' + str(id_split_mapped)

# Append binary_look_up to input_id
id_converted = id_input + ''.join(id_split_mapped)
print 'id_converted: ' + id_converted

# TODO: Return converted_id
