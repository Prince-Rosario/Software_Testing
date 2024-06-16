import unittest

from solution import Solution

class TestMinWindowSubstring(unittest.TestCase):
    def setUp(self):
        """Prepare resources for each test."""
        self.solution = Solution()

    def test_empty_string_t(self):
        """Test with t as an empty string. Expect the output to be an empty string."""
        self.assertEqual(self.solution.minWindow("anystring", ""), "")

    def test_single_character_match(self):
        """Test with s and t as single matching characters. Expect the output to be t."""
        self.assertEqual(self.solution.minWindow("a", "a"), "a")

    def test_single_character_no_match(self):
        """Test with s and t as single non-matching characters. Expect the output to be an empty string."""
        self.assertEqual(self.solution.minWindow("a", "b"), "")

    def test_example_cases(self):
        """Test the provided example cases.""" ### test parametrization by iterating over multiple input-output pairs
        cases = [
            ("ADOBECODEBANC", "ABC", "BANC"),  # Expected output: "BANC"
            ("a", "a", "a"),  # Expected output: "a"
            ("a", "aa", "")  # Expected output: ""
        ]
        for s, t, expected in cases:
            with self.subTest(s=s, t=t):
                self.assertEqual(self.solution.minWindow(s, t), expected)

    def test_no_substring_found(self):
        """Test a case where no substring of s can satisfy the condition with t."""
        self.assertEqual(self.solution.minWindow("abcdef", "xyz"), "")

    def test_large_input(self):
        """Test with large strings to check performance and boundary conditions."""
        s = "a" * 100000
        t = "aa"
        self.assertEqual(self.solution.minWindow(s, t), "aa")

    def test_t_characters_not_in_s(self):
        """Test with t containing characters not present in s."""
        self.assertEqual(self.solution.minWindow("abc", "xyz"), "")

    def test_s_and_t_same(self):
        """Test with s and t being the same."""
        self.assertEqual(self.solution.minWindow("exact", "exact"), "exact")

    def test_all_characters_in_s_needed_for_t(self):
        """Test where all characters in s are needed for t."""
        self.assertEqual(self.solution.minWindow("ab", "ab"), "ab")

    def test_s_contains_repeated_sequences_of_t(self):
        """Test with s containing repeated sequences of t."""
        self.assertEqual(self.solution.minWindow("ababcabc", "abc"), "abc")

if __name__ == "__main__":
    unittest.main()
