import re
import unittest
from python.dummy_logger import main


class TestDummyLogger(unittest.TestCase):
    def test_dummy_logger(self):
        output = main()
        print(output)
        self.assertIsNotNone(
            re.search("[A-Z,a-z]{3} [A-Z,a-z]{3} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}: [A-Z, a-z].*", output),
            "Output doesn't match expected pattern"
        )


if __name__ == "__main__":
    unittest.main(module=None)