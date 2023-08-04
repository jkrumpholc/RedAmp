import os
import src.Logger as Logger
import requests
import re


def parse_data(data, url, database) -> int:
    """
    :param data: Content of file
    :type data: str
    :param url: Source url
    :type url: str
    :param database: Database class
    :return: Number of entries
    :rtype: int
    """
    count = 0  # count of processed lines
    for line in data.split("\n"):
        if re.search(r"(?:^|\S)https?://\S+/", line) is not None:
            database.add_entry("url_ioc", line, url)  # insert line into "url_ioc" table
            count += 1
        elif re.search(r"(?:^|\S)(?:\d+\.){3}\d+", line) is not None:
            database.add_entry("ip_ioc", line, url)  # insert line into "ip_ioc" table
            count += 1
    return count


def parse_links(file_name, database) -> bool:
    """
    :param file_name: Name of file with links
    :type file_name: str
    :param database: Database class
    :return: True if success
    :rtype: bool
    """
    if not os.path.exists(file_name):   # check if file exists
        Logger.err_handler("Target doesn't exists", f"Target file: {file_name} does not exists.")
    if not os.path.isfile(file_name):   # check if target is a file
        Logger.err_handler("Target is not a file")
    with open(file_name, "r+") as file:
        for url in file:
            req = requests.get(url)  # request to get file
            resp = req.content.decode()     # decode response to get file content
            url = re.findall(r"https?://([^/]+)", url)[0]
            parse_data(resp, url, database)
            database.db_commit()
    return True


