#!/usr/bin/env python
from parsers import main_parser

if __name__ == '__main__':
    opts = main_parser.parse_args()
    opts.func(opts)
