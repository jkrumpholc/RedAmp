import os
import src.Logger as Logger
import requests
import re


def parse_data(data, url, database) -> tuple[int, int]:
    """
    :param data: Content of file
    :type data: str
    :param url: Source url
    :type url: str
    :param database: Database class
    :return: Number of entries for each type
    :rtype: tuple
    """
    ip_count = 0
    url_count = 0  # count of processed lines
    for line in data.split("\n"):
        if re.search(r"(?:^|\S)https?://\S+/", line) is not None:
            database.add_entry("url_ioc", line, url)  # insert line into "url_ioc" table
            url_count += 1
        elif re.search(r"(?:^|\S)(?:\d+\.){3}\d+", line) is not None:
            database.add_entry("ip_ioc", line, url)  # insert line into "ip_ioc" table
            ip_count += 1
    return ip_count, url_count


def parse_links(file_name, database) -> tuple[int, int]:
    """
    :param file_name: Name of file with links
    :type file_name: str
    :param database: Database class
    :return: Number of processed lines
    :rtype: tuple
    """
    if not os.path.exists(file_name):  # check if file exists
        Logger.err_handler("Target doesn't exists", f"Target file: {file_name} does not exists.")
    if not os.path.isfile(file_name):  # check if target is a file
        Logger.err_handler("Target is not a file")
    ip_rows = url_rows = 0
    with open(file_name, "r+") as file:
        for url in file:
            url = url.strip()
            req = requests.get(url)  # request to get file
            if req.status_code != 200:
                Logger.err_handler(f"Page error {req.status_code}",
                                   f"Page {url} returned code {req.status_code} ({req.reason})")
            resp = req.content.decode()  # decode response to get file content
            url = re.findall(r"https?://([^/]+)", url)[0]
            ip_temp, url_temp = parse_data(resp, url, database)
            database.execute()
            database.set_sources(ip_temp, url_temp, url)
            ip_rows += ip_temp
            url_rows += url_temp
    return ip_rows, url_rows
