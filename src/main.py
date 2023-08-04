import argparse
import src.Logger as Logger


def arg_parsing() -> argparse.Namespace:
    """
    :return: Arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action='store_true', help="Show help.")
    parser.add_argument("--file", help="Source file with links to data sources.")  # argument for file with links
    parse_args = parser.parse_args()
    if parse_args.help:
        pass
    if not parse_args.file:
        Logger.err_handler("No input data", "Please set argument '--file'. For info use '--help'")
    return parse_args


if __name__ == '__main__':
    args = arg_parsing()
    
