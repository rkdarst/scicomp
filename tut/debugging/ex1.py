def a():
    a = 1
    b = 2
    c = a+b
    import code; code.interact(local=locals())
    print c

if __name__ == '__main__':
    a()
