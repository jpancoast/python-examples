#!/usr/bin/env python

import argparse

from test_class import test_class


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Example script using argparse.")

    parser.add_argument("first_key", help="value for the first key")
    parser.add_argument("second_key", help="value for the second key")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable verbose output")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug output")
    parser.add_argument("-u", "--url",
                        help="URL to fetch with a GET request")

    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if args.verbose:
        print(f"first_key={args.first_key} second_key={args.second_key}")

    test_obj = test_class(args.first_key, args.second_key, args.debug)
    test_obj.print_something()

    if args.url:
        test_obj.run_get(args.url)
        print(test_obj.get_content())

    test_obj.work_map()

if __name__ == "__main__":
    main()
