import unittest
from unittest import mock
import argparse
import psycopg2
from src.Database import Database, Credentials
import src.main as main


class RedAmpTest(unittest.TestCase):

    def test_empty_args(self):
        """
        test with no args
        """
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 1)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(help=True))
    def test_help_args(self, mock_args):
        """
        test for --help
        """
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
        self.assertTrue(Database().connect())

    @mock.patch.object(psycopg2, "connect")
    def test_db_connect_fail(self, mock_connect):
        """
        test for unsuccessful connection
        """
        e = psycopg2.OperationalError()
        mock_connect.side_effect = e
        self.assertFalse(Database().connect())


if __name__ == '__main__':
    unittest.main()
