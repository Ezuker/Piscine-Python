def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            nonlocal function
            if count < limit:
                function()
                count = count + 1
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
