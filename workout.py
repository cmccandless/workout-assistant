#!/usr/bin/env python
from tinydb import TinyDB
from parsers import main_parser

if __name__ == '__main__':
    opts = main_parser.parse_args()
    db = TinyDB(opts.db)
    opts.func(db, opts)
