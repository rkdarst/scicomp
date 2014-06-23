

def A(x):
    print 'begin A'
    a = x + 1
    B(x)
    print 'end A'

def B(y):
    print 'begin B'
    c = y * 2
    print c
    print 'end B'

def main():
    A(5)

if __name__ == '__main__':
    main()
