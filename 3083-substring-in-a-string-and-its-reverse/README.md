# 3083. Existence of a Substring in a String and Its Reverse

## Problem Description

Given a string s, find any substring of length 2 which is also present in the reverse of s.

Return true if such a substring exists, and false otherwise.
---

## Example

### Example 1

**Input:**  
s = "leetcode"
**Output:**  
true

**Explanation:**  
Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

---

### Example 2

**Input:**  
s = "abcba"
**Output:**  
true

**Explanation:**  
All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".

---

### Example 3

**Input:**  
s = "abcd"
**Output:**  
false

**Explanation:**  
There is no substring of length 2 in s, which is also present in the reverse of s.

---

## Constraints

- 1 <= s.length <= 100
- s consists only of lowercase English letters.

---

## Approach

1. Iterate through the string to generate all substrings of length 2
2. Reverse the original string once for comparison
3. Check if each length-2 substring exists in the reversed string
4. Return True if a match is found, otherwise return False

---

## Code Implementation (Python)

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s)-1):
            if (s[i]+s[i+1]) in s[::-1]:
                return True
        return False
```

----

## Acceptance

![Acceptance](https://github.com/muhdshahan/Daily-DSA/blob/main/3083-substring-in-a-string-and-its-reverse/acceptance.png)