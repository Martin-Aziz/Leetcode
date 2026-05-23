import os

problems = [
    {
        "num": 3,
        "title": "Longest Substring Without Repeating Characters",
        "pattern": "Sliding Window / Hash Set",
        "difficulty": "Medium",
        "statement": """Given a string s, find the length of the longest substring without repeating characters.

**Example 1:**
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

**Example 2:**
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

**Example 3:**
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.""",
        "explanation": """### Approach: Sliding Window with Hash Set

1. Use two pointers: left and right to define a window
2. Use a set to track characters in current window
3. Expand right pointer, adding characters to set
4. If duplicate found, shrink from left until no duplicate
5. Track maximum window size""",
        "walkthrough": """Example: s = "abcabcbb"

```
Step 1: left=0, right=0, char='a'
  set = {a}, max_len = 1

Step 2: left=0, right=1, char='b'
  set = {a,b}, max_len = 2

Step 3: left=0, right=2, char='c'
  set = {a,b,c}, max_len = 3

Step 4: left=0, right=3, char='a' (duplicate!)
  Remove from left: remove 'a', left=1
  set = {b,c}, add 'a': set = {b,c,a}, max_len = 3

Continue... Maximum = 3""",
        "python_code": """def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Test cases
print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3""",
        "java_code": """class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < s.length(); right++) {
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }
            charSet.add(s.charAt(right));
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}""",
        "js_code": """function lengthOfLongestSubstring(s) {
    const charSet = new Set();
    let left = 0;
    let maxLen = 0;
    
    for (let right = 0; right < s.length; right++) {
        while (charSet.has(s[right])) {
            charSet.delete(s[left]);
            left++;
        }
        charSet.add(s[right]);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
}

console.log(lengthOfLongestSubstring("abcabcbb")); // 3
console.log(lengthOfLongestSubstring("bbbbb"));    // 1
console.log(lengthOfLongestSubstring("pwwkew"));   // 3"""
    },
    {
        "num": 4,
        "title": "Median of Two Sorted Arrays",
        "pattern": "Binary Search / Divide and Conquer",
        "difficulty": "Hard",
        "statement": """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

**Example 1:**
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

**Example 2:**
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.""",
        "explanation": """### Approach: Binary Search on Smaller Array

Key insight: We need to partition both arrays such that:
1. Left half has same elements as right half (or one more)
2. All elements in left <= all elements in right

1. Ensure nums1 is the smaller array
2. Binary search on nums1 to find partition
3. Calculate corresponding partition in nums2
4. Check if partition is valid (left1 <= right2 and left2 <= right1)
5. If valid, calculate median based on odd/even total length""",
        "walkthrough": """Example: nums1 = [1,3], nums2 = [2]

```
Total length = 3, need 2 elements on left
Partition nums1 at index 1: [1] | [3]
Partition nums2 at index 1: [2] | []

left1 = 1, right1 = 3
left2 = 2, right2 = infinity

Check: left1(1) <= right2(inf) ✓
       left2(2) <= right1(3) ✓

Median = max(left1, left2) = max(1,2) = 2""",
        "python_code": """def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is smaller
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    
    return 0.0

# Test cases
print(findMedianSortedArrays([1,3], [2]))      # 2.0
print(findMedianSortedArrays([1,2], [3,4]))    # 2.5""",
        "java_code": """class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length, n = nums2.length;
        int left = 0, right = m;
        
        while (left <= right) {
            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;
            
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((m + n) % 2 == 0) {
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                } else {
                    return Math.max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                right = partition1 - 1;
            } else {
                left = partition1 + 1;
            }
        }
        
        return 0.0;
    }
}""",
        "js_code": """function findMedianSortedArrays(nums1, nums2) {
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    
    const m = nums1.length, n = nums2.length;
    let left = 0, right = m;
    
    while (left <= right) {
        const partition1 = Math.floor((left + right) / 2);
        const partition2 = Math.floor((m + n + 1) / 2) - partition1;
        
        const maxLeft1 = partition1 === 0 ? -Infinity : nums1[partition1 - 1];
        const minRight1 = partition1 === m ? Infinity : nums1[partition1];
        const maxLeft2 = partition2 === 0 ? -Infinity : nums2[partition2 - 1];
        const minRight2 = partition2 === n ? Infinity : nums2[partition2];
        
        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            if ((m + n) % 2 === 0) {
                return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
            } else {
                return Math.max(maxLeft1, maxLeft2);
            }
        } else if (maxLeft1 > minRight2) {
            right = partition1 - 1;
        } else {
            left = partition1 + 1;
        }
    }
    
    return 0.0;
}

console.log(findMedianSortedArrays([1,3], [2]));    // 2.0
console.log(findMedianSortedArrays([1,2], [3,4]));  // 2.5"""
    },
    {
        "num": 5,
        "title": "Longest Palindromic Substring",
        "pattern": "Expand Around Center / Dynamic Programming",
        "difficulty": "Medium",
        "statement": """Given a string s, return the longest palindromic substring in s.

**Example 1:**
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

**Example 2:**
Input: s = "cbbd"
Output: "bb"

**Constraints:**
- 1 <= s.length <= 1000
- s consist of only digits and English letters.""",
        "explanation": """### Approach: Expand Around Center

A palindrome mirrors around its center. There are 2n-1 centers:
- n single character centers (for odd-length palindromes)
- n-1 between-character centers (for even-length palindromes)

1. For each possible center, expand outward
2. Keep track of the longest palindrome found
3. Return the longest substring""",
        "walkthrough": """Example: s = "babad"

```
Center at index 0 ('b'): "b" (len=1)
Center at index 1 ('a'): "bab" (len=3) ✓
Center at index 2 ('b'): "aba" (len=3) ✓
Center at index 3 ('a'): "a" (len=1)
Center at index 4 ('d'): "d" (len=1)

Even centers:
Between 0-1: "b" (no match)
Between 1-2: "" (no match)
...

Longest: "bab" or "aba" (both length 3)""",
        "python_code": """def longestPalindrome(s):
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    if not s:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        len1 = expandAroundCenter(i, i)      # Odd length
        len2 = expandAroundCenter(i, i + 1)  # Even length
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

# Test cases
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"
print(longestPalindrome("a"))      # "a\"""",
        "java_code": """class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int maxLen = Math.max(len1, len2);
            
            if (maxLen > end - start) {
                start = i - (maxLen - 1) / 2;
                end = i + maxLen / 2;
            }
        }
        
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}""",
        "js_code": """function longestPalindrome(s) {
    function expandAroundCenter(left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }
    
    if (!s) return "";
    
    let start = 0, end = 0;
    
    for (let i = 0; i < s.length; i++) {
        const len1 = expandAroundCenter(i, i);
        const len2 = expandAroundCenter(i, i + 1);
        const maxLen = Math.max(len1, len2);
        
        if (maxLen > end - start) {
            start = i - Math.floor((maxLen - 1) / 2);
            end = i + Math.floor(maxLen / 2);
        }
    }
    
    return s.substring(start, end + 1);
}

console.log(longestPalindrome("babad")); // "bab" or "aba"
console.log(longestPalindrome("cbbd"));  // "bb"
console.log(longestPalindrome("a"));     // "a\""""
    }
]

for prob in problems:
    content = f'''# Problem {prob["num"]}: {prob["title"]}

## Problem Statement
{prob["statement"]}

---

## Pattern Recognition
**Pattern:** {prob["pattern"]}
**Difficulty:** {prob["difficulty"]}

---

## Step-by-Step Explanation

{prob["explanation"]}

---

## Visual Walkthrough

{prob["walkthrough"]}

---

## Code Solutions

### Python Solution
```python
{prob["python_code"]}
```

### Java Solution
```java
{prob["java_code"]}
```

### JavaScript Solution
```javascript
{prob["js_code"]}
```

---

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Optimal | See solution | See solution |

---

## Common Mistakes

❌ **Mistake 1:** Not handling edge cases (empty string, single character)
✅ **Fix:** Add base case checks at the beginning

❌ **Mistake 2:** Off-by-one errors in indices
✅ **Fix:** Carefully track left/right boundaries

---

## Variations & Related Problems

1. **Palindrome Number** - Check if number is palindrome
2. **Palindromic Substrings** - Count all palindromic substrings
3. **Longest Palindromic Subsequence** - DP variation
4. **Valid Palindrome** - With alphanumeric constraint
5. **Shortest Palindrome** - Add characters to make palindrome

---

## Interview Tips

💡 **What interviewers look for:**
1. Can you identify the palindrome pattern?
2. Do you consider both odd and even length cases?
3. Can you optimize from brute force?

💡 **Follow-up questions:**
- "Can you solve it in O(n)?" → Manacher's algorithm
- "What about counting all palindromes?" → DP approach
- "How would you handle very long strings?" → Consider space optimization

---

## Reflection Questions

1. Why do we need to check both odd and even length palindromes?
2. What's the time complexity of the brute force approach?
3. How does the expand around center approach improve efficiency?

---

## Practice Exercises

1. Implement the DP solution for this problem
2. Modify to count all palindromic substrings
3. Solve the variant where you can delete k characters
'''
    
    filename = f'/workspace/files/{prob["num"]:03d}.{prob["title"].replace(" ", "-")}.md'
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print("\nBatch 1 complete!")
