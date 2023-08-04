import os
import psycopg2
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


class Database:
    def __init__(self):
        credentials = Credentials()
        self.db_host = credentials.get("DATABASE_HOST")
        self.db_name = credentials.get("DATABASE_NAME")
        self.db_user = credentials.get("DATABASE_USERNAME")
        self.db_pass = credentials.get("DATABASE_PASSWORD")
        self.conn = None
        self.cur = None

    def connect(self) -> bool:
        """
        Create connection to database
        :return: True if success, False otherwise
        :rtype: bool
        """
        try:
            self.conn = psycopg2.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_pass)
            self.cur = self.conn.cursor()
        except psycopg2.OperationalError:
            return False
        else:
            return True

    def add_entry(self, table, data, source):
        request = f"INSERT INTO {table}(source, data) VALUES ('{source}','{data}')"
        try:
            self.cur.execute(request)
        except psycopg2.OperationalError:
            Logger.err_handler("Cannot connect", "Cannot connect to database")
        except psycopg2.DataError:
            Logger.err_handler("Data error", f"Cannot work with data:\n    {data}")
        except psycopg2.ProgrammingError:
            Logger.err_handler("Wrong SQL querry", f"Wrong SQL querry:\n    {request}")

    def db_commit(self):
        try:
            self.conn.commit()
        except psycopg2.InternalError:
            Logger.err_handler("Integrity error")
        return True
