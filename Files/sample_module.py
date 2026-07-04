root_lambda = lambda val: (val**0.5, -(val**0.5))
def median(values):
    '''
    Return the middle value (if odd)
    or the average of the two middle values (if even)
    >>> median([1, 4, 5])
    4
    >>> median([0, 2, 6, 100])
    4.0
    '''
    values = sorted(values)
    size = len(values)
    if size%2 == 0:
        left = values[int(size/2 - 1)]
        right = values[int(size/2)]
        return (left+right)/2
    else:
        return values[int(size/2)]
