def A():
    def B():
        a = 1
        b = 2
        a += c
    x = 0
    B()
if __name__ == '__main__':
    A()
