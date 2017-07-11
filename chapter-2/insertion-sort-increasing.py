def insertion_sort_increasing(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key

if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    insertion_sort_increasing(a)
    print('sorted list = ')
