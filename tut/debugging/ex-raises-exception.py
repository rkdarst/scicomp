import numpy
def func(x):
    x + numpy.array([1, 2])

def main():
    arr = numpy.array([0, 1, 10])
    func(arr)

if __name__ == '__main__':
    main()
