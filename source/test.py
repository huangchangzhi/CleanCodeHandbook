'''
'''


def m():
    src_name = ''
    dest_name = ''
    num_map = {}
    with open(src_name) as f:
        num = f.readline()
        while num:
            if num =='\n':
                continue
            num_map[num] = num_map.get(num, 0) + 1
            num = f.readline()
    with open(dest_name, 'a') as f:
        for num in num_map:
            if num_map[num] == 1:
                f.write("%d\n" % num)

if __name__ == '__main__':
    m = {}
    m.setdefault(4, 3)
    m[1100] = 10
    m.setdefault(1100, 3)
    print m
    print m[4]
    print m[1100]
