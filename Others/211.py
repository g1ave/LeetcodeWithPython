import collections


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        return self.match(0, word, self.root)

    def match(self, index: int, word: str, node: TrieNode):
        if not node:
            return False

        if index == len(word):
            return node.is_word

        if word[index] != '.':
            return self.match(index + 1, word, node.children.get(word[index]))
        else:
            for child in node.children.values():
                if self.match(index + 1, word, child):
                    return True
        return False


if __name__ == '__main__':
    word_dictionary = WordDictionary()
    word_dictionary.addWord("apple")
    word_dictionary.addWord("aliyun")
    word_dictionary.addWord("bear")
    assert word_dictionary.search("a....")
    assert word_dictionary.search("..ar")