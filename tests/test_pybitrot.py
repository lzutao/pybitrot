# #!/usr/bin/env python
import os
import sys
import unittest
#
import pybitrot


class TestPybitrot(unittest.TestCase):

    def test_rol(self):
        test_cases = [
            #   x,    k, size, solution
            # when k is multiple of four
            [0xfa,        0x0,  0x8,  0xfa],
            [0xfa,        0x4,  0x8,  0xaf],
            [0xfa,        0x8,  0x8,  0xfa],
            [0xfa,       -0x4,  0x8,  0xaf],
            [0xfa,       -0x8,  0x8,  0xfa],
            # else
            [0xfa,        0x1,  0x8,  0xf5],
            [0xfa,        0x2,  0x8,  0xeb],
            [0xfa,        0x3,  0x8,  0xd7],
            # Multi-byte
            [0x11223344,  0x8, 0x32,  0x22334411],
            [0x11223344, 0x16, 0x32,  0x33441122],
        ]

        for (x, k, size, solution) in test_cases:
            rs = pybitrot.__rol(x, size, k)
            self.assertEqual(rs, solution)


    def test_ror(self):
        test_cases = [
            #   x,    k, size, solution
            # when k is multiple of four
            [0xfa,        0x0,  0x8,  0xfa],
            [0xfa,        0x4,  0x8,  0xaf],
            [0xfa,        0x8,  0x8,  0xfa],
            [0xfa,       -0x4,  0x8,  0xaf],
            [0xfa,       -0x8,  0x8,  0xfa],
            # else
            [0xfa,        0x1,  0x8,  0x7d],
            [0xfa,        0x2,  0x8,  0x3e],
            [0xfa,        0x3,  0x8,  0x1f],
            # Multi-byte
            [0x11223344,  0x8, 0x32,  0x44112233],
            [0x11223344, 0x16, 0x32,  0x33441122],
        ]

        for (x, k, size, solution) in test_cases:
            rs = pybitrot.__ror(x, size, k)
            self.assertEqual(rs, solution)


if __name__ == '__main__':
    unittest.main()
