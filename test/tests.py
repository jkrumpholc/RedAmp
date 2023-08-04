import unittest
import src.main as main


class RedAmpTest(unittest.TestCase):

    def test_empty_args(self):
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 1)

    @patch('argparse._sys.argv', ['--help'])
    def test_help_args(self):
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
