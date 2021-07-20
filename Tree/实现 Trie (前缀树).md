
```py
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.children = {}
        self.isend = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pt = self
        for c in word:
            if c not in pt.children:
                pt.children[c] = Trie()
                pt.children[c].val = c
            pt = pt.children[c]
        pt.isend = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pt = self
        for c in word:
            if c not in pt.children:
                return False
            pt = pt.children[c]
        return pt.isend

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pt = self
        for c in prefix:
            if c not in pt.children:
                return False
            pt = pt.children[c]
        return True
```
