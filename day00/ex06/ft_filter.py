def ft_filter(function, iterable):
    """
    ft_filter(function, iterable) --> filter object
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    new_list = [item for item in iterable if function(item)]
    return new_list
