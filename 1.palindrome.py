import re

# re 모듈 이용
def isPalindrome(s : str) -> bool :
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    print(s)
    
    if s != s[::-1] or s =='' :
        print('false')
    else :
        print('true')

# re 모듈 없이
def isPalindrome(s:str) -> bool :
    strs = []
    for i in s :
        if i.isalnum() :
            strs.append(i.lower())


    if strs == strs[::-1] and strs != [] :
        return print('true')
    else :
        return print('false')

isPalindrome('sqwqs')