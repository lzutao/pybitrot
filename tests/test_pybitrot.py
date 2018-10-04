# #!/usr/bin/env python
import os
import sys
#
import pytest
#
from pybitrot import pybitrot


class TestPybitrot(object):
    def test_rol(self):
        test_cases = [
            #   x,    k, size, solution
            # when k is multiple of four
            [0xfa,        0,  8,  0xfa],
            [0xfa,        4,  8,  0xaf],
            [0xfa,        8,  8,  0xfa],
            [0xfa,       -4,  8,  0xaf],
            [0xfa,       -8,  8,  0xfa],
            # else
            [0xfa,        1,  8,  0xf5],
            [0xfa,        2,  8,  0xeb],
            [0xfa,        3,  8,  0xd7],
            # Multi-byte
            [0x11223344,  8, 32,  0x22334411],
            [0x11223344, 16, 32,  0x33441122],
        ]

        for (x, k, size, solution) in test_cases:
            rs = pybitrot.rol(x, size, k)
            assert(rs == solution)


    def test_ror(self):
        test_cases = [
            #   x,    k, size, solution
            # when k is multiple of four
            [0xfa,        0,  8,  0xfa],
            [0xfa,        4,  8,  0xaf],
            [0xfa,        8,  8,  0xfa],
            [0xfa,       -4,  8,  0xaf],
            [0xfa,       -8,  8,  0xfa],
            # else
            [0xfa,        1,  8,  0x7d],
            [0xfa,        2,  8,  0xbe],
            [0xfa,        3,  8,  0x5f],
            # Multi-byte
            [0x11223344,  8, 32,  0x44112233],
            [0x11223344, 16, 32,  0x33441122],
        ]

        for (x, k, size, solution) in test_cases:
            rs = pybitrot.ror(x, size, k)
            assert(rs == solution)

