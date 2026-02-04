import unittest
from io import StringIO
from unittest.mock import patch

from aurora.main import main

class Test_main(unittest.TestCase):
    def test_main_contains_packages_require_attention(self):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()
            output = fake_out.getvalue()

        self.assertIn("packages require attention.", output)

if __name__ == "__main__":
    unittest.main()       