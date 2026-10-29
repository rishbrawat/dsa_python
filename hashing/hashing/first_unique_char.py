def firstUniqChar(s: str):
    freq_s = {}
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq_s[char] == 1:
            return i
    return -1

print(firstUniqChar("lleetcode"))