import argparse
import src.Database as Database
import src.Data_processing as Data_processing
import src.Logger as Logger


def arg_parsing() -> argparse.Namespace:
    """
    :return: Arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(add_help=False, description="RedAmp Python Developer Assignment")
    parser.add_argument("--help", action='store_true', help="Show help.")
    parser.add_argument("--file", help="Source file with links to data sources.")  # argument for file with links
    parse_args = parser.parse_args()
    if parse_args.help:
        Logger.info_handler("\nRedAmp Python Developer Assignment. Start with:\n      python3 main.py --file [path_to_file]\n"
                            "Options:\n    --help:    Shows this help\n    --file:    Path to file with links\n")

    elif not parse_args.file:
        Logger.err_handler("No input data", "Please set argument '--file'. For info use '--help'")
    return parse_args


if __name__ == '__main__':
    args = arg_parsing()
    Database.Credentials()
    db = Database.Database()  # initialize database
    db.connect()  # initialize connection
    Data_processing.parse_links(args.file, db)  # parse file
