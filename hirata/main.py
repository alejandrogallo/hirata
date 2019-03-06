import argparse
from . import process_file


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=""
    )

    parser.add_argument("-f", "--file",
        help="Input file",
        action="store"
    )

    parser.add_argument("-o", "--out",
        help="Output file (hirata.out)",
        default="hirata.cpp",
        action="store"
    )

    parser.add_argument("--fock",
        help="Kill non-fock contributions (i.e. Fai etc..)",
        action="store_true"
    )

    parser.add_argument("--no-comments",
        help="Strip out the comments",
        action="store_true"
    )

    parser.add_argument("--contract-with",
        help="The name of the operator you want to contract with",
        action="store"
    )

    parser.add_argument("--with-indices",
        help="The indices of the operator that you want, for example abij etc...",
        default=None,
        action="store"
    )

    parser.add_argument("--prepend",
        help="Prepend anything to every line of the equations",
        default="",
        action="store"
    )

    parser.add_argument("--with-intermediates",
        help="""Put every line equal to some intermediate, you need to provide
        a name""",
        default="",
        action="store"
    )

    parser.add_argument("--python-tuples-out",
        help="Export data in python tuples to a file",
        default="",
        action="store"
    )

    # Parse arguments
    args = parser.parse_args()
    print(args)

    if not args.file:
        parser.print_help()
        sys.exit(1)

    result_lines = process_file(args)
    fd = open(args.out, "w+")
    for line in result_lines:
        fd.write("%s\n" % line)


if __name__ == "__main__":
    main()
