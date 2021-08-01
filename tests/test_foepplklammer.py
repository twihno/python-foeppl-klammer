"""unittests for foepplklammer"""

import unittest

import numpy as np
import foepplklammer as fp
from foepplklammer.foepplklammerstandard import foeppl, foeppl_inkl_null


class TestFoeppl(unittest.TestCase):
    """Test class for foepplklammer"""

    def test_foepplklammer_np(self):
        """tests the numpy functions"""

        numbers = np.array([-1, 2, 4, 5, 100])
        error_numbers = np.array([-1, 0, 1, 2])

        self.assertEqual(
            str(fp.foeppl_np(numbers, 0, 2)), str(
                np.array([0, 4, 16, 25, 10000]))
        )

        self.assertEqual(
            str(fp.foeppl_np(numbers, 1, 2)), str(
                np.array([0, 1, 9, 16, 9801]))
        )

        self.assertEqual(
            str(fp.foeppl_np(numbers, 0, 0)), str(
                np.array([0, 1, 1, 1, 1]))
        )

        with self.assertRaises(ValueError):
            fp.foeppl_np(error_numbers, 0, 2)

        self.assertEqual(
            str(fp.foeppl_np_inkl_null(error_numbers, 0, 2)),
            str(np.array([0, 0, 1, 4]))
        )

        self.assertEqual(
            str(fp.foeppl_np_inkl_null(error_numbers, 0, 0)),
            str(np.array([0, 0, 1, 1]))
        )

    def test_foepplklammer_standard(self):
        """tests the standard functions"""

        self.assertEqual(foeppl(-1, 0, 1), 0)
        self.assertEqual(foeppl(1, 0, 1), 1)
        self.assertEqual(foeppl(2, 0, 1), 2)
        self.assertEqual(foeppl(2, 0, 2), 4)

        self.assertEqual(foeppl(-1, 0, 0), 0)
        self.assertEqual(foeppl(1, 0, 0), 1)
        self.assertEqual(foeppl(2, 0, 0), 1)

        with self.assertRaises(ValueError):
            foeppl(0, 0, 1)

        self.assertEqual(foeppl_inkl_null(-1, 0, 1), 0)
        self.assertEqual(foeppl_inkl_null(0, 0, 1), 0)
        self.assertEqual(foeppl_inkl_null(1, 0, 1), 1)
        self.assertEqual(foeppl_inkl_null(2, 0, 1), 2)
        self.assertEqual(foeppl_inkl_null(2, 0, 2), 4)

        self.assertEqual(foeppl_inkl_null(-1, 0, 0), 0)
        self.assertEqual(foeppl_inkl_null(0, 0, 0), 0)
        self.assertEqual(foeppl_inkl_null(1, 0, 0), 1)
        self.assertEqual(foeppl_inkl_null(2, 0, 0), 1)


if __name__ == "__main__":
    unittest.main()
