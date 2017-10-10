def adding(a,b):
    carry = 0
    c = [0]*(len(a)+1)
    for i in range(len(a)-1,-1,-1):
        temp = a[i]+b[i]+carry
        carry = temp//2
        c[i+1] = temp%2
    c[0] = (a[0]+b[0]+carry)%2
    return c

if __name__ == '__main__':
    a = [1,1,1,1]
    b = [1,1,1,1]
    print(adding(a,b))