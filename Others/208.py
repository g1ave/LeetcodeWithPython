import collections


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if not cur:
                return False
        if not cur.is_word:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if not cur:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert trie.startsWith("app")
