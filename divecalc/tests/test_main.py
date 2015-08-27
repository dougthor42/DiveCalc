# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:23:40 2015

@author: dthor
"""

# Standard Library
import sys
import unittest
import os.path as osp

# Third-Party
from docopt import docopt

# Package / Application
try:
    from .. import main
except (SystemError, ImportError):
    if __name__ == "__main__":
        # Allow module to be run as script
        print("Running module as script")
        sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
        import main
    else:
        raise

class TestTableDepth(unittest.TestCase):
    known_values = ((0, 10),
                    (23, 25),
                    (15, 15),
                    (15.1, 20),
                    (39.996, 40),
                    (103, 110),
                    (130, 130),
                    )

    def test_known_values(self):
        """Check known good values"""
        for depth, expected in self.known_values:
            self.assertEqual(main.table_depth(depth), expected)

    def test_negative_depth(self):
        """Negative values raise ValueError"""
        invalid_depths = (-1, -100, -156323, -0.0023658)
        for depth in invalid_depths:
            with self.assertRaises(ValueError):
                main.table_depth(depth)

    def test_large_depth(self):
        """Depths below 130ft raise DeathError"""
        invalid_depths = (130.1, 131, 1550)
        for depth in invalid_depths:
            fail_msg = "Failed on: `{}`".format(depth)
            with self.assertRaises(main.DeathError, msg=fail_msg):
                main.table_depth(depth)

    def test_wrong_type(self):
        """Only ints and floats are allowed"""
        invalid_types = ("string", {"dict": 0}, (1, 2), [3, 4], True)
        for item in invalid_types:
            fail_msg = "Failed on: `{} {}`".format(item, type(item))
            with self.assertRaises(TypeError, msg=fail_msg):
                main.table_depth(item)


if __name__ == "__main__":
    """
    Main entry point
    """
    docopt(__doc__, version="0.0.1")    # TODO: pull VERSION from __init__
    unittest.main(verbosity=1)
