import unittest
from unittest import mock
import argparse
import psycopg2
from src.Database import Database, Credentials
import src.main as main
from src.Data_processing import parse_links, parse_data


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

    def test_file_nonexistent(self):
        """
        test for nonexistent file
        """
        with self.assertRaises(SystemExit) as cm:
            parse_links("", "")
        self.assertEqual(cm.exception.code, 1)

    def test_file_non_file(self):
        """
        test for dir instead of file
        """
        with self.assertRaises(SystemExit) as cm:
            parse_links("../src/", "")
        self.assertEqual(cm.exception.code, 1)

    def test_file_empty_file(self):
        """
        test for empty file
        """
        with open("../empty.txt", "w") as file:
            pass
        self.assertEqual(parse_links("../empty.txt", ""), 0)

    def test_parse_empty_data(self):
        """
        test for parsing empty data
        """
        self.assertEqual(parse_data("", "", ""), (0, 0))

    def test_parse_data(self):
        """
        test for correct parsing data
        """
        db = Database()
        db.connect()
        self.assertEqual(parse_data("https://www.templatent.com/apc/2fa69440-4d27-4a93-b54d-4af36b27a54b/186dc87a-7c05-446c-8919-bd97a59dd550/13f11222-6f81-49c3-92ab-17b40ef8c79a/login?id=c2lHREdJSVNxaHp4UmhZczY1RGoyKzRUUmZnOElTZG10Tk9VUm1wZ3E3aHBqUEJMZ3JRcktYVUl5d0Z1cEc4UityeFdTVWtTNVVCWERGSjhCYkZBY1BqdkQweklzc2pNaExXbmdvZDRrMnVZeHBQNWpDbk9aSU9yS2hSbzdoVlgrejg5d0dXSWpsaVVTeC9vcHYwcFJGSVBOK20yNlV6enkwejlVR2IrblFKRGlKSGs2ZFdaR214NVJoZnBLWTVWOVd4WE5hdDVmNVdGbHVBR2VRQjBHOC9RSnMrZjRtUldjNndudmYzMDZYeW40allhRDhwRE81MG01L01UdjBHVUI0cGlaajNvaThzY2RHOWRKRGRoK3hVQjNiekM5YXZiYllTMjB5YkxGYnVReFVIanNEbGVZRklKN3lFK3BpS0kxczRxOWRzSEdVYjZjaW5tVnlRQVdvZDZDQzZlV2NQbjZVVmdsWDRNa2FZb2xSenZ0akI4eGtPeE1aNzVGR2hB",
                                    'openphish.com', db), (0, 1))

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

    def test_db_commit(self):
        """
        test for database commit
        """
        db = Database()
        db.connect()
        self.assertTrue(db.db_commit())

    def test_db_sources(self):
        """
        test for saving IOC sources
        """
        db = Database()
        db.connect()
        self.assertTrue(db.set_sources(0, 0, ""))


if __name__ == '__main__':
    unittest.main()
