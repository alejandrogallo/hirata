import argparse
import logging
from .line import HirataLine
from .cc4s import Cc4sLine
from .utils import get_tensor_name_with_indices
import re
import sys


def process_file(args):
    logger = logging.getLogger("main")
    result_lines = []
    logger.info("Processing %s ", args.file)
    indices = None
    fd = open(args.file)
    for line in fd:
        print("")
        h_line = HirataLine(line)
        cc4s_line = Cc4sLine(h_line)
        lines = cc4s_line.to_cpp()
        result_lines.append("// orig  : %s" % line.replace("\n", ""))
        result_lines.append("// conv  : %s" % cc4s_line)
        result_lines.append("// free  : %s" % cc4s_line.free_indices)
        result_lines.append("// summed: %s" % cc4s_line.summation_indices)
        if args.contract_with:
            if args.with_indices:
                indices = args.with_indices
            tensor_name = get_tensor_name_with_indices(
                args.contract_with,
                args.with_indices,
                cc4s_line.free_indices.replace(" ", "")
            )
            logger.debug("Contracting with tensor %s" % tensor_name)
            lines = [
                re.sub(r"\)\s*\*\s*", ") * %s * " % tensor_name, li)
                for li in lines
            ]
        if args.python_tuples_out:
            with open(args.python_tuples_out, 'a+') as fd:
                for line in lines:
                    fd.write(
                        str(
                            line.replace(' ', '')
                                .replace(';', '')
                                .split('*')[1:]
                        )
                    )
                    fd.write('\n')
        if args.prepend:
            logger.debug("Prepending %s" % args.prepend)
            lines = [args.prepend + li for li in lines]
        if args.with_intermediates:
            if args.with_indices:
                indices = args.with_indices
            tensor_name = args.with_intermediates
            free_indices = cc4s_line.free_indices.replace(" ", "")
            tensor = get_tensor_name_with_indices(
                tensor_name,
                indices,
                free_indices
            )
            logger.debug("Intermediate %s" % tensor)
            lines = [
                "%s = %s" % (tensor, li)
                for li in lines
            ]
        result_lines += lines
        result_lines.append("")
    if args.no_comments:
        logger.debug("Getting rid of comments")
        result_lines = [
            li for li in result_lines if not re.match(r"^//.*$", li)
        ]
    return result_lines


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
