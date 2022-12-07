#!/usr/bin/env python3
import sys
from importlib import import_module

for i in range(7):
    if len(sys.argv) < 2:
        raise Exception("must provide session token")
    import_module(f"day{i+1}").day(str(i+1), sys.argv[1])
