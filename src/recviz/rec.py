def pretty_args(args):
    """pretty prints the arguments in a string
    """
    return ", ".join([repr(arg) for arg in args])


def pretty_kwargs(kwargs):
    """pretty prints the keyword arguments in a string
    """
    return ", ".join([
        f"{key}={repr(value)}"
        for key, value in kwargs.items()
    ])


def pretty_func(fn, args, kwargs):
    # Pretty print args in a string
    args_str = pretty_args(args)

    # Pretty print kwargs in a string
    kwargs_str = pretty_args(kwargs)

    # Format the function string and return
    if args_str and kwargs_str:
        return f"{fn.__name__}({args_str, kwargs_str})"
    return f"{fn.__name__}({args_str or kwargs_str})"


def recviz(fn):
    """Decorator that pretty prints the recursion tree with
       args, kwargs and return values.
    """

    # holds the current recursion level
    recursion_level = 1

    def wrapper(*args, **kwargs):

        # we register a nonlocal recursion_level so that
        # it binds with the the recursion_level variable.
        # in this case, it will bind to the one defined
        # in recviz function.
        nonlocal recursion_level

        # Generate the pretty printed function string
        fn_str = pretty_func(fn, args, kwargs)

        # Generate the whitespaces as per the recursion level
        whitespace = "   " * (recursion_level - 1)

        # Pretty print the function with the whitespace
        print(f"{whitespace} -> {fn_str}")

        # increment the recursion level
        recursion_level += 1

        # Invoke the wrapped function and hold the return value
        return_value = fn(*args, **kwargs)

        # Post function evaluation we decrease the recursion level by 1
        recursion_level -= 1

        # Pretty print the return value
        print(f"{whitespace} <- {repr(return_value)}")

        # Return the return value of the wrapped function
        return return_value

    return wrapper
