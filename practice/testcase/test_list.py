#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import unittest
from core.main import reverse3
from core.main import make_ends


class PracticeTestCase(unittest.TestCase):
    def testReverse3(self):
        self.assertEquals(reverse3([7, 0, 0]), [0, 0, 7])

    def testMakeEnds(self):
        self.assertEquals(make_ends([7]), [7, 7])
