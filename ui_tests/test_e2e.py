import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MinWindowE2ETest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_min_window(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        s = driver.find_element_by_name("s")
        t = driver.find_element_by_name("t")
        
        # Example test case
        s.send_keys("ADOBECODEBANC")
        t.send_keys("ABC")
        t.send_keys(Keys.RETURN)
        
        result = driver.find_element_by_tag_name("p").text
        self.assertIn("Result: BANC", result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()