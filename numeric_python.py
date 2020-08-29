import numpy


# Arrays
def arrays():
    # Input
    arr = input().rstrip().split(" ")

    # Function
    return numpy.array(arr[::-1], float)


# Shape and Reshape
def shape_reshape():
    # Input
    arr = list(map(int, input().rstrip().split()))

    # Function
    np_arr = numpy.array(arr)
    print(numpy.reshape(np_arr, (3, 3)))


# Transpose and Flatten
def transpose_flatten():
    # Input
    n, m = map(int, input().rstrip().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Function
    np_arr = numpy.array(arr)
    print(np_arr.transpose())
    print(np_arr.flatten())


# Concatenate
def concatenate_arrays():
    # Input
    n, m, p = map(int, input().rstrip().split())
    array_1 = []
    array_2 = []
    for i in range(n):
        array_1.append(list(map(int, input().rstrip().split())))
    for i in range(m):
        array_2.append(list(map(int, input().rstrip().split())))

    # Function
    np_arr_1 = numpy.array(array_1)
    np_arr_2 = numpy.array(array_2)
    print(numpy.concatenate((array_1, array_2), axis=0))


# Zeros and ones
def zeros_and_ones():
    # Input
    t = tuple(map(int, input().rstrip().split()))

    # Function
    print(numpy.zeros(t, dtype=numpy.int))
    print(numpy.ones(t, dtype=numpy.int))


zeros_and_ones()
