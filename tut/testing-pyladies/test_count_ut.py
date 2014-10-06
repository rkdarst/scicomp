import unittest

from count import *

class Perm(unittest.TestCase):
    def test_count(self):

        # Count of an empty iterator should return an empty dict.
        # [0] -> {}
        assert_dict_equal(count([]), {})

        # [1] -> {1: 1}

if __name__ == '__main__':
    unittest.main()
