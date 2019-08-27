from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self, char):
        # Initialize this node in the Trie
        self.char = char
        self.children = []
        self.code = 0

    def insert(self, char):
        # Add a child node in this Trie
        new_node = TrieNode()
        new_node.char = char
        self.children.append(new_node)

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        # Calls a helper function to see if the
        # children in this node has the existing character
        val = []
        for child in self.children:
            self.suffix_helper(child, child.char, val)
        # returns a list of all the suffixes
        return val
    # Uses recursion to traverse each branch of all the nodes

    def suffix_helper(self, node, suffix, lis):
        # Here the code comes in handy as it lets the search node to store this value
        if node.code == 1:
            lis.append(suffix)
        # Store it if its a leaf and is not in the list
        if len(node.children) == 0 and suffix not in lis:
            lis.append(suffix)
            return
        # Traverse each node's children
        for child in node.children:
            self.suffix_helper(child, suffix + child.char, lis)


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode('')

    def insert(self, word):
        # Add a word to the Trie
        nodes = []
        # I create each character asits own node
        for char in word:
            new_node = TrieNode(char)
            nodes.append(new_node)
        # This is marker for when to know that it was the end of a word
        nodes[-1].code = 1
        self.insert_helper(self.root, nodes)

    # This function is designed to recursively add the nodes to the tree
    def insert_helper(self, node, lis):
        # When the list is empty then I return
        if len(lis) == 0:
            return
        temp = lis.pop(0)
        # Checks if the char is already in the tree
        exists = self.node_exists(temp, node)
        # If it does not exist then I add it to the node's children
        if exists is None:
            node.children.append(temp)
            self.insert_helper(temp, lis)
            # Else I skip it and being traversing this existing node
        else:
            self.insert_helper(exists, lis)

    # This helper method is made to check if the node already exists
    def node_exists(self, node, current):
        for child in current.children:
            if node.char == child.char:
                return child
        return None

    # Finding the last occurrence of the letter
    def find(self, prefix):
        # I split the prefix into a list
        chars = list(prefix)
        # Then I call a helper method to traverse the tree
        return self.find_helper(self.root, chars)

    # If the first letter in the list is any of the children of the tree then
    # run a DFS search for the last occurrence of the prefix
    def find_helper(self, node, chars):
        last = None
        for child in node.children:
            if child.char == chars[0]:
                last = self.dfs(child, chars[1:])
        # If it's not in the root's children then return None
        return last

    # This DFS will take the characters one by one and check if it exists
    # in any of the child node. If it does then we continue the search on that
    # root. If it does not then we return None
    def dfs(self, node, chars):
        if len(chars) == 0:
            return node
        for child in node.children:
            if child.char == chars[0]:
                return self.dfs(child, chars[1:])
        return None

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');