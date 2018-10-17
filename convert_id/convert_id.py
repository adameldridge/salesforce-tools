# TODO: take input id as a parameter from command line
input_id = '001A000010khO8J'

# Split the string into groups of 5 characters
split_id = [input_id[i:i+5] for i in range(0, len(input_id), 5)]
print 'split_id: ' + str(split_id)

# Reverse the strings in split_id
split_id_reversed = [group[::-1] for group in split_id]
print 'split_id_reversed: ' + str(split_id_reversed)

# TODO: Convert uppercase chars to 1 and lowercase to 0


# TODO: Look up the corresponding char in the BinaryIdLookup


# TODO: Append binary_look_up to input_id


# TODO: Return converted_id