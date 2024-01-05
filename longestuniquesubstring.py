def longestUniqueSubstring(s):
    i = 0
    j = 0
    longest_substring = 0
    while j < len(s):
        if s[j] in s[i:j]:
            i += 1
        else:
            longest_substring = max(longest_substring, j - i + 1)
            j += 1
    return longest_substring