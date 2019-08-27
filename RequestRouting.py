# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, char):
        # Initialize this node in the Trie
        self.char = char
        self.children = []
        self.code = 0
        # placeholder
        self.handler = None

    def insert(self, char):
        # Add a child node in this Trie
        new_node = RouteTrieNode()
        new_node.char = char
        self.children.append(new_node)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self, home_page):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('')

    def insert(self, word):
        # Add a word to the Trie
        word = word.split('/')
        if word[0] == '':
            word.pop(0)
        nodes = []
        # I create each character as its own node
        for char in word:
            new_node = RouteTrieNode(char)
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

    def find(self, prefix):
        # I split the prefix into a list
        chars = prefix.split('/')
        if chars[0] == '':
            chars.pop(0)
        if chars[-1] == '':
            chars.pop(len(chars) - 1)

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


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, dire):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie('')
        self.trie.root.handler = dire
        pass

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # I insert the path into the tree so it can be parsed
        self.trie.insert(path)
        # then find the node and set the nodes handler value
        find_node = self.trie.find(path)
        find_node.handler = handler
        # find_node.handler = handler
        return find_node

    def lookup(self, path):
        if path == '/':
            return self.trie.root.handler
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # I use my find method to traverse the tree to find the associated letter
        find_node = self.trie.find(path)
        if find_node is None:
            return 'not found handler'
        if find_node.handler is None:
            return 'not found handler'
        return find_node.handler

# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")# add a route
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement