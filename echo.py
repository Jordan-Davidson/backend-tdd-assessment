#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Jordan Davidson"


import sys
import argparse


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def to_title(text):
    return text.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', 
                        help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower', 
                        help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title',
                        help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    text = ns.text
    upper = ns.upper
    lower = ns.lower
    title = ns.title
    if text is sys.argv[1]:
        print(text)
    if upper:
        print(to_upper(text))
    elif lower:
        print(to_lower(text))
    elif title:
        print(to_title(text))


if __name__ == '__main__':
    main(sys.argv[1:])