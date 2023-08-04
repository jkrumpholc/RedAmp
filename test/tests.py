import unittest
from unittest import mock
import argparse
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

if __name__ == '__main__':
    unittest.main()
