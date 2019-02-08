import argparse
from besttags.web.manager import WebManager


def cli_web():
    parser = argparse.ArgumentParser(
        description="Get the best hashtags for your post")

    parser.add_argument('tags', nargs='+',
                        help="The tags you are interested in")

    parser.add_argument('--fix', nargs='+',
                        help="Some fix tags")

    parser.add_argument('--limit', type=int, default=30,
                        help="Some fix tags")

    parser.add_argument('--kind', type=str, default='simple',
                        choices=['simple', 'all', 'test'],
                        help="Different types of how the tags are determined")

    parser.add_argument('--file', type=str,
                        help="Save the result in a file")

    parser.add_argument('--list', action='store_true',
                        help="Display every tag in a single line")

    args = parser.parse_args()

    values = {
        'limit': int(args.limit),
        'fix': args.fix if args.fix else [],
        'kind': args.kind,
    }

    best = WebManager(**values)
    result = best(args.tags)

    if args.list:
        for tag in result:
            print(tag)

    elif args.file:
        result.save(args.file)

    else:
        print(result)
