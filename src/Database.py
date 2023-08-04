import os
import dotenv
import src.Logger as Logger


class Credentials:
    def __init__(self):
        dotenv.load_dotenv()
        self.credentials = dotenv.dotenv_values()
        if len(self.credentials) == 0:  # check if credentials exists
            Logger.err_handler("No credentials file found", "Please import proper '.env' file with keys: "
                               "'DATABASE_HOST', 'DATABASE_NAME', 'DATABASE_USERNAME', 'DATABASE_PASSWORD'")

    def value(self) -> dict:
        """
        :return: Credentials
        :rtype: dict
        """
        return self.credentials

    @staticmethod
    def get(name: str) -> str:
        """
        Get credentials from '.env' file
        :param name: Name of environv
        :type name: str
        :return: Value of environv
        :rtype: str
        """
        return os.environ.get(name)
