# Word break problem

def wordBreak(words, word, lookup):
    n=len(word)
    if n==0:
        return True
    if lookup[n]==-1:
        lookup[n]=0
        for i in range(1,n+1):
            prefix=word[:i]
            if prefix in words and wordBreak(words,word[i:],lookup):
                lookup[n]=1
                return True
    return lookup[n]==1




words = [
    'self', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r',
    'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'
]

# input string
word = 'Wordbreakproblem'
lookup=[-1]*(len(word)+1)
if wordBreak(words, word,lookup):
    print('The string can be segmented')
else:
    print('The string can\'t be segmented')