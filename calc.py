#!/usr/bin/env python3

import sys
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)

expr = sys.stdin.read().strip()

try:
    result = parse_expr(expr, transformations=standard_transformations + (implicit_multiplication_application,))
    print(result)
except Exception:
    pass