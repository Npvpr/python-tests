def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.split()[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))