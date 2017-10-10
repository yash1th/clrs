def insertion_sort_decreasing(a):
    for j in range(len(a)-1,-1,-1):
        key = a[j]
        i = j+1
        while i < len(a) and a[i] > key:
            a[i-1] = a[i]
            i += 1
        a[i-1] = key

if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    insertion_sort_decreasing(a)
    print('sorted list = ',a)
