import os
import src.Logger as Logger
import requests


def parse_links(file_name) -> bool:
    """
    :param file_name: Name of file with links
    :type file_name: str
    :rtype: bool
    """
    if not os.path.exists(file_name):   # check if file exists
        Logger.err_handler("Target doesn't exists", f"Target file: {file_name} does not exists.")
    if not os.path.isfile(file_name):   # check if target is a file
        Logger.err_handler("Target is not a file")
    with open(file_name, "r+") as file:
        for url in file:
            req = requests.get(url)
            resp = req.content.decode()     # decode response to get file content
            url = re.findall(r"https?://([^/]+)", url)[0]
            parse_data(resp, url, database)
            database.db_commit()
    return True


