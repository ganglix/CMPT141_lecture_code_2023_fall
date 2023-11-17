"""
S       F(S)
”       ”
’a’     ’a’      F('a') = 'a' + F('')
’ab’    ’ba’
’abc’   ’cba’    F('abc') = 'c' + F('ab')
’abcd’  ’dcba’   F('abcd') = 'd' + F('abc')

F(s) = s[-1] + F(s[0:-1])
"""

def F(s):
    if len(s) == 0:
        return s
    else:
        # recursive case: reduced, delegated: process s[0:-1]
        return s[-1] + F(s[0:-1])

print(F('ab'))