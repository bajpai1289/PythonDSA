def uniqueMorseRepresentations(words: str):
    morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d={}
    for i in range(97, 123):
        d[chr(i)]=morse[i-97]
    for k in range(len(words)):
        newStr=''
        for j in range(len(words[k])):
            newStr+=d[words[k][j]]
        words[k]=newStr
    return len(set(words))

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))

