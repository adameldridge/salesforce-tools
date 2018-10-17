import re

# TODO: take input id as a parameter from command line
input_id = '001A000010khP8J'

# Split id into list of 5 character chunks
split_id = [input_id[i:i+5] for i in range(0, len(input_id), 5)]
print 'split_id: ' + str(split_id)

# Reverse the strings in split_id
split_id_reversed = [chunk[::-1] for chunk in split_id]
print 'split_id_reversed: ' + str(split_id_reversed)

# TODO: Convert uppercase chars to 1 and lowercase to 0
split_id_binary = [re.sub(r'[a-z,2-9]', "0", chunk) for chunk in split_id_reversed]
split_id_binary = [re.sub(r'[A-Z]', "1", chunk) for chunk in split_id_reversed]
print 'split_id_binary: ' + str(split_id_binary)

# TODO: Look up the corresponding char in the BinaryIdLookup


# TODO: Append binary_look_up to input_id


# TODO: Return converted_id