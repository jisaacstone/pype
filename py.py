#!/usr/bin/env python
from __future__ import unicode_literals

import sys
from sys import stdin as IN
from sys import stdout as OUT
import itertools as IT
import functools as FT
import operator as OP
from pprint import pprint as PP

def main():
    args = list(sys.argv)
    if len(args) < 2:
        raise StandardError("No python statement supplied for execution")
    command = args.pop(1)
    sys.argv = args
    eval(command)


if __name__ == '__main__':
    main()