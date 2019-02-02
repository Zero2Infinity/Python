def string_validators(s):
    'The any(0 method returns True if any element of an iteration is True'
    result = [False] * 5
    for i in range(0, len(s)):
       if not result[1] and s[i].isalpha():
            result[1] = True
       if not result[2] and s[i].isdigit():
            result[2] = True
       if not result[3] and s[i].islower():
            result[3] = True
       if not result[4] and s[i].isupper():
            result[4] = True

    result[0] = result[1] or result[2] 
    return result

 
if __name__ == '__main__':
    s = input().strip()
    #result = string_validators(s)
    #print ('\n'.join([str(s) for s in result]))
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))
