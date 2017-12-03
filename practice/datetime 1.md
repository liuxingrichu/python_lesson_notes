（1）计算一年的第几天

程序：

from datetime import datetime

class Demo(object):
    def cal_days(self, year, month, day):
        return (datetime(year, month, day)- datetime(year, 1, 1)).days + 1

		
测试用例：

import os
import sys
import unittest

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core.main import Demo


class PracticeTestCase(unittest.TestCase):
	def test_cal_days(self):
        self.demo = Demo()
        days = self.demo.cal_days(2000, 2 ,28)
        self.assertEquals(days, 59)

		
if __name__ == '__main__':
    unittest.main()		