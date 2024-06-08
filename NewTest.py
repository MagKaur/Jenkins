import unittest
from selenium import webdriver

class SeleniumDemoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_example(self):
        self.assertIn("Selenium", self.driver.title)

if __name__ == "__main__":
    unittest.main()
