code = '11110000000010110000000100100000000000000000000011000001'

header = [8870, 4484, ]
space = 550
zero = space
one = 1650

encoded_code_list = []
encoded_code_list += header
for x in code:
    encoded_code_list.append(space)
    if int(x) == 1:
        encoded_code_list.append(one)
    else:
        encoded_code_list.append(zero)

encoded_code = ', '.join([str(x) for x in encoded_code_list])
print(encoded_code)