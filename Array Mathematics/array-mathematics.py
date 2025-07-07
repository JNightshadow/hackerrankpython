import numpy
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = numpy.array(input().split(),int)
    b = numpy.array(input().split(),int)
    a = a.reshape(1,-1)
    b = b.reshape(1,-1)
    print (numpy.add(a,b))
    print (numpy.subtract(a,b))
    print (numpy.multiply(a,b))
    print (numpy.floor_divide(a,b))
    print (numpy.mod(a,b))
    print (numpy.power(a,b))
