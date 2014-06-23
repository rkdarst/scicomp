def a():
    a = 1
    b = 2
    c = a+b
    import code; code.interact(local=locals())
    print c

a()
