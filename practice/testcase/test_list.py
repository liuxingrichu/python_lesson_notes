#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import unittest
from core.main import reverse3
from core.main import make_ends
from core.main import sum13
from core.main import has22


class PracticeTestCase(unittest.TestCase):
    def testReverse3(self):
        self.assertEquals(reverse3([7, 0, 0]), [0, 0, 7])

    def testMakeEnds(self):
        self.assertEquals(make_ends([7]), [7, 7])

    def testSum13_01(self):
        self.assertEquals(sum13([13, 1, 13]), 0)

    def testSum13_02(self):
        self.assertEquals(sum13([1, 2, 13, 2, 1, 13]), 4)

    def testHas22_01(self):
        self.assertEquals(has22([2, 3, 2, 2]), True)

    def testHas22_02(self):
        self.assertEquals(has22([]), False)
