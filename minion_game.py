def minion_game_2(string):
    vowel = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    
    for i in range(1, len(string)+1):
        for j in range(0, len(string)): 
            s = (string[j:i+j])
            if len(s) == i:
                if s[0] in vowel:
                    kevin_score += 1
                else:
                    stuart_score += 1

    if kevin_score > stuart_score:
        outcome = "Kevin {}".format(kevin_score)
    elif kevin_score < stuart_score:
        outcome = "Stuart {}".format(stuart_score)
    else:
        outcome = "Draw"
        
    print ("{} = {}".format(kevin_score, stuart_score))
    print (outcome)

def minion_game(string):
    ' Optimization: add all substring start with s[i] letter. '
    vowels = 'AEIOU'
    strl = len(string)
    stuart_score, kevin_score = 0, 0

    for i in range(strl):
        if string[i] in vowels:
            kevin_score += strl-i
        else:
            stuart_score += strl-i

    if kevin_score > stuart_score:
        outcome = "Kevin {}".format(kevin_score)
    elif kevin_score < stuart_score:
        outcome = "Stuart {}".format(stuart_score)
    else:
        outcome = "Draw"
        
    print ("{} = {}".format(kevin_score, stuart_score))
    print (outcome)

if __name__ == '__main__':
    s = input()
    minion_game(s)
