#!/usr/bin/env python3
import sys
from importlib import import_module

for i in range(3):
    if len(sys.argv) < 2:
        raise Exception("must provide path to input files")
    import_module(f"day{i+1}").day(f"{sys.argv[1]}/{i+1}.txt")  # type: ignore
