def linear_search(a,value):
    for i,e in enumerate(a):
        if e == value:
            return i
    return None


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    value = int(input().strip())
    result = linear_search(a,value)
    if result is None:
        print('No value found')
    else:
        print('{} is found at index {} in the given input'.format(value, result))