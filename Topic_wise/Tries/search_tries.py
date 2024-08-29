class TrieNode:
    def __init__(self,data):
        self.data = data
        self.children = [None] * 26
        self.isend = False

class Solution:
    def insert_word(self, words, root):
        for word in words:
            current_node = root
            for char in word:
                index = ord(char) - ord('a')  # Convert char to index (0-25)
                if not current_node.children[index]:
                    # If the corresponding child does not exist, create a new TrieNode
                    current_node.children[index] = TrieNode(char)
                current_node = current_node.children[index]
            current_node.isend = True
    def searchword(self, word, root):
        current_node = root
        for char in word:
            index = ord(char) - ord('a')
            if not current_node.children[index]:
                return False  # If the character is not found, the word doesn't exist
            current_node = current_node.children[index]
        return current_node.isend  # Return True if it's the end of a valid word

# Example usage
words = ["big", "brigadier", "bison"]
root = TrieNode(None)
solution = Solution()
solution.insert_word(words, root)

# Now, use the searchword method to check if words exist in the Trie
print(solution.searchword(root=root, word="big"))       # True
print(solution.searchword(root=root, word="brigadier")) # True
print(solution.searchword(root=root, word="bison"))     # True
print(solution.searchword(root=root, word="bis"))       # False
print(solution.searchword(root=root, word="brig"))      # False
