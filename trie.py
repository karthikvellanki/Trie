class TrieNode(object):    
    def __init__(self, char):
        self.char = char
        self.children = set()
        self.end_of_word = False
        self.counter = 1
    

def add_word(root, word):

    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if child.char == char:

                child.counter += 1

                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.add(new_node)

            node = new_node

    node.word_finished = True


def prefix_search(root, prefix):

    node = root

    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
`
        for child in node.children:
            if child.char == char:

                char_not_found = False

                node = child
                break

        if char_not_found:
            return False, 0

    return True, node.counter


# root = TrieNode('')
# add_word(root, "marathon")
# add_word(root, 'marat')

# print(prefix_search(root, 'mar'))
# print(prefix_search(root, 'ma'))
