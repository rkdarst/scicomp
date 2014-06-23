

def A(a):
    B(a+1)

def B(b):
    import ipdb
    ipdb.set_trace()
    print b

A(5)
