# Software_Testing

## Testing

The tests for the solution are located in test_solution.py. The TestMinWindowSubstring class contains several test cases to verify the correctness of the solution under various conditions, including:

- Testing with t as an empty string.
- Testing with s and t as single matching or non-matching characters.
- Testing with provided example cases, including cases where no substring is found, cases with large inputs to check performance, and cases where t contains characters not present in s.
- Testing with s and t being the same, and cases where all characters in s are needed for t.
- Testing with s containing repeated sequences of t.

## Solution credits

[neet code](https://github.com/neetcode-gh/leetcode/blob/main/python/0076-minimum-window-substring.py)

The time complexity of used solution is **O(S+T)**, where **S** is the length of string **s** and **T** is the length of string **t**.
