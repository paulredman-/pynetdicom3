"""Run all the test files in test directory."""

import os
import sys
import unittest

test_dir = os.path.dirname(__file__)

class TestLoader(object):
    def load_tests(self, *args):
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.discover(test_dir))

        return suite

if __name__ == "__main__":
    # Get the testss
    suite = TestLoader().load_tests()

    # Run the tests
    verbosity = 1
    args = sys.argv
    if len(args) > 1 and (args[1] == "-v" or args[1] == "--verbose"):
        verbosity = 2

    runner = unittest.TextTestRunner(verbosity=verbosity)

    test_dir = os.path.join(test_dir, 'dicom_files')
    result = runner.run(suite)

    sys.exit(len(result.failures) + len(result.errors))