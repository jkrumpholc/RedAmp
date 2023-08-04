import sys


def err_handler(error_text: str, help_text: str = None) -> None:
    """
    Error handler
    :param error_text: Error text
    :type error_text: str
    :param help_text: Explanation text
    :type help_text: str
    :return: None
    """
    sys.stderr.write(error_text+"\n")
    sys.stderr.flush()
    if help_text is not None:
        sys.stdout.write(help_text+"\n")
        sys.stdout.flush()
    input("Press Return to exit: ")
    sys.exit(1)
