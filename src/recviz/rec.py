def recviz(fn):
  """Wrapper decorator that pretty prints the recursion tree with
      arguments, keyword arguments and return values.
  """
  
  # to hold the recursion level
  recursion_level = 1

  def wrapper(*ar, **kw):
      
    # we register a nonlocal recursion_level so that it binds with the
    # the recursion_level variable defined in recviz function.
    nonlocal recursion_level
    
    # format the arguments, keyword arguments and whitespace
    # and keep them ready for pretty printing
    args_str = ", ".join([repr(a) for a in ar])
    kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kw.items()])
    whitespace = "   " * (recursion_level - 1)

    # create the final human readable pretty function string
    fn_str = f"{whitespace} -> {fn.__name__}"
    if args_str and kwargs_str:
      fn_str = f"{fn_str}({args_str}, {kwargs_str})"
    else:
      fn_str = f"{fn_str}({args_str or kwargs_str})"

    # pretty print the function
    print(fn_str)

    # we increase the recursion level
    recursion_level += 1
    
    # invoke the wrapped function
    return_value = fn(*ar, **kw)
    
    # post function evaluation we decrease the recursion level by 1
    recursion_level -= 1

    # pretty print the return value
    print(f"{whitespace} <- {repr(return_value)}")
    
    # return the return value of the wrapped function
    return return_value

  return wrapper
