import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MinWindowE2ETest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000")

    def test_empty_string_t(self):
        self._submit_form("anystring", "")
        self._verify_result("")

    def test_single_character_match(self):
        self._submit_form("a", "a")
        self._verify_result("a")

    def test_single_character_no_match(self):
        self._submit_form("a", "b")
        self._verify_result("")

    def test_no_substring_found(self):
        self._submit_form("abcdef", "xyz")
        self._verify_result("")

    def test_large_input(self):
        self._submit_form("a" * 100000, "aa")
        self._verify_result("aa")

    def test_t_characters_not_in_s(self):
        self._submit_form("abc", "xyz")
        self._verify_result("")

    def test_s_and_t_same(self):
        self._submit_form("exact", "exact")
        self._verify_result("exact")

    def test_all_characters_in_s_needed_for_t(self):
        self._submit_form("ab", "ab")
        self._verify_result("ab")

    def test_s_contains_repeated_sequences_of_t(self):
        self._submit_form("ababcabc", "abc")
        self._verify_result("abc")

    def _submit_form(self, s, t):
        driver = self.driver
        s_input = driver.find_element(By.NAME, "s")
        t_input = driver.find_element(By.NAME, "t")
        s_input.clear()
        t_input.clear()
        s_input.send_keys(s)
        t_input.send_keys(t)
        t_input.send_keys(Keys.RETURN)

    def _verify_result(self, expected_result):
        result = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertIn(f"Result: {expected_result}", result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()