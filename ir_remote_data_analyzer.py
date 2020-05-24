code = '''8870, 4484,  518, 1686,  550, 1656,  548, 540,  544, 572,  548, 540,  574, 540,  548, 540,  546, 1660,  518, 598,  516, 1688,  518, 1686,  550, 540,  548, 568,  548, 542,  516, 572,  574, 542,  548, 1656,  548, 540,  544, 572,  548, 542,  574, 540,  518, 572,  574, 540,  548, 542,  518, 596,  518, 1688,  548, 542,  516, 598,  546, 1658,  548, 540,  550, 540,  576, 1628,  576, 540,  548, 540,  574, 540,  548, 540,  544, 572,  548, 540,  518, 598,  548, 540,  550, 568,  546, 542,  548, 566,  518, 572,  546, 568,  516, 572,  548, 566,  518, 572,  548'''


def raw_to_hex(code):
    code_list = [ int(x) for x in code.split(',') if x.strip()][2:]

    # print(code_list)

    code_remove_space = []

    for idx, cd in enumerate(code_list):
        if idx % 2 != 0:
            code_remove_space.append(cd)

    # print(code_remove_space)

    code_encoded = ''

    for x in code_remove_space:
        if x > 1000:
            bit = '1'
        else:
            bit = '0'
        code_encoded += bit

    print(code_encoded)
    print(hex(int(code_encoded, 2)))


if __name__ == '__main__':
    raw_to_hex(code)
    code_list = [ int(x) for x in code.split(',') if x.strip()]
    code_list_vector = []
    v = True
    for x in code_list:
        vm = '+' if v else '-'
        code_list_vector.append('{}{}'.format(vm, x))
        v = not v

    print(' '.join(code_list_vector) + ' -40884')

