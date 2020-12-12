recviz
===

Simple visualization for recursive functions in Python.

# Installing recviz

```sh
pip install recviz
```

# Usage

```py
from recviz import recviz

@recviz
def fib(n):
  if n == 0 or n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)
```
