def isPalindrome(word):
    copy = word[::-1]
    if(copy == word): return True
    else: return False
    
x = 'madam'
print(isPalindrome(x))