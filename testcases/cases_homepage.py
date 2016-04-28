# -*- coding: UTF-8 -*-
import unittest

import time
import logging
from commom.common import Elements
from commom.utility import Utilty
from page_elements import element_page_home

class HomePageCases(unittest.Testcase):
    def setUp(self):
        pass

    def testDown(self):
        self.driver.quit()
        self.driver.close()
    def test_in_hotel(self):
        pass



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(HomePageCases("test_in_hotel"))
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))




