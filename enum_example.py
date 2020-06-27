"""
this is small example demonstrates how to use enums in python
https://docs.python.org/3/library/enum.html
"""
from enum import Enum

class operation_code(Enum):
    authorize = 1
    log_out = 2

print(operation_code.authorize == 1)