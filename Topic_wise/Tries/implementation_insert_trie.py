
class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = [None] * 26  # Array for 'a' to 'z'
        self.isend = False  # End of word flag

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
            current_node.isend = True  # Mark the end of the word

# Example usage
words = ["big", "brigadier", "bison"]
root = TrieNode(None)
solution = Solution()
solution.insert_word(words, root)

