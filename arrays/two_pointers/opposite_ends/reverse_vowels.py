def reverseVowels(s: str) -> str:
    left = 0
    right = len(s)-1

    vowels =set('aeiou')
    chars = list(s)

    while left < right:
        if chars[left].lower() not in vowels:
            left += 1
            continue
        if chars[right].lower() not in vowels:
            right -= 1
            continue
        
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return ''.join(chars)


print(reverseVowels(s="IceCreAm"))