def ft_filter(function, iterable):
    """Use filter with lamda on element of iterable and return the result"""
    result = []
    for element in iterable:
        if function(element):
            result.append(element)
    return result
