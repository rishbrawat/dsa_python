def canConstruct(ransomNote: str, magazine: str) -> bool:
    freq_mag = {}
    for char in magazine:
        freq_mag[char] = freq_mag.get(char, 0) + 1
    freq_rn = {}
    for char in ransomNote:
        freq_rn[char] = freq_rn.get(char, 0) + 1

    # now i want to make sure that each char from mag atleast appears once, if it does not i can return false, if it appears more than once, i simply  return false again
    for char, count in freq_rn.items():
        if freq_mag.get(char, 0) < count:
            return False
    return True
   

print(canConstruct( ransomNote = "aa", magazine = "aab"))