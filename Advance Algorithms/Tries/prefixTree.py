class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.word=False
    
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
        
    def insert(self, word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
                curr=curr.children[c] #incorrect identation was the cause of this error
        curr.word=True
    
    def search(self, word):
        curr =self.root
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.word
    
    def startsWith(self, prefix):
        curr=self.root
        count=0
        for c in prefix:
            if c not in curr.children:
                return False
            count+=1
            curr=curr.children[c]
        print(count)
        return True
        
    
    
trie=Trie()
trie.insert('search')
trie.insert('sea')
trie.startsWith('se')