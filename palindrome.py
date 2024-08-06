def palindrome(word):
    lst=list(word)
    if lst==lst[::-1]:
        return True
    else:
        return False
print(palindrome("bob"))