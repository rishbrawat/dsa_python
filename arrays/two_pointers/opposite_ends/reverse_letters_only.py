def reverseOnlyLetters(s: str) -> str:
        left = 0
        right = len(s)-1

        chars = list(s)

        while left < right:
            if not chars[left].isalpha():
                left += 1
                continue
            if not  chars[right].isalpha():
                right -= 1
                continue

            else:
                chars[left], chars[right] = chars[right],chars[left]

            left += 1
            right -= 1
        
        return ''.join(chars)


print(reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))