import re

def is_my_palindrome(line: str) -> bool:  # empty end one character are polyn =)
    line = line.lower()
    for i in range(len(line)//2):
        if line[i] != line[len(line)-1 - i]:
            return False
    return True


def is_palindrome(word):
    forward = ''.join(re.findall(r'[a-z]+', word.lower()))
    backwards = forward[::-1]
    return forward == backwards


l = input()
print(is_palindrome(l))
