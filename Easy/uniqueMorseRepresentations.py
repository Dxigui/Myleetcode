# -*- coding: utf-8 -*-

def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    pwdbook = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    wordbook = 'abcdefghijklmnopqrstuvwxyz'
    L = []
    for word in words:
        pwd = ''
        for i in word:
            wordindex = pwdbook[wordbook.find(i)]
            pwd += wordindex
        L.append(pwd)
        print(L)
    return len(set(L))

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
