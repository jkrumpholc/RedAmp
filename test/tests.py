import unittest
from unittest import mock
import argparse
from src.Database import Database, Credentials
import src.main as main


class RedAmpTest(unittest.TestCase):

    def test_empty_args(self):
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 1)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(help=True))
    def test_help_args(self, mock_args):
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 0)

    def test_dotenv(self):
        """
        test for .env file
        """
        self.assertGreaterEqual(len(Credentials().value()), 0)

    def test_db_connect(self):
        """
        test for database connection
        """
        self.assertEqual(Database().connect(), True)




if __name__ == '__main__':
    unittest.main()
