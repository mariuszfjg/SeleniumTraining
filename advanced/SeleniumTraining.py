import unittest
from selenium import webdriver


class SeleniumTraining(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_selenium_training(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
