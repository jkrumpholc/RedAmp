import unittest
import src.main as main


class RedAmpTest(unittest.TestCase):

    def test_empty_args(self):
        with self.assertRaises(SystemExit) as cm:
            main.arg_parsing()
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
