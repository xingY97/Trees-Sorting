#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        # TODO
        if self.size == 0 :
            return True

    def contains(self, string):
        """Return True if this prefix tree contains the given string.
        """
        if string == "":
            return True
        current_node = self.root
        for s in string:
            # if character is not root's children
            if s not in current_node.children: 
                return False
            current_node = current_node.get_child(s)
        return current_node.terminal == True



    def insert(self, string):
        """Insert the given string into this prefix tree.
        """
        current_node = self.root
        unique = False
        for i in string:
            if i not in current_node.children:
                unique = True
                current_node.children[i] = PrefixTreeNode(i)
            current_node = current_node.children[i]
        current_node.terminal = True
        if unique:
            self.size += 1


    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0

        # Start with the root node
        node = self.root

        depth = 0
        while node:
            node = node.children
            depth += 1
        return node, depth


    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        string = prefix
        current_node = self.root
        preintri = False
        
        for p in prefix:
            if p in current_node.children:
                preintri = True
                current_node = current_node.children[p]
            elif p not in current_node.children:
                return completions

        self._traverse(current_node, prefix, completions)
        if completions == [] and preintri == True:
            completions.append(prefix)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # TODO
        current_node = self.root
        for char in current_node.children.keys():
            all_strings.extend(self.complete(char))
        return all_strings
    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""

        # node has no children return contorl back to the caller
        if node.num_children() == 0:
            return
        # if this node contains char that ends the word then add to complteions
        if node.terminal:
            visit.append(prefix)
        # string = prefix
        # for char in children keys
        for char in node.children.keys():
            # concatenate prefix with char
            string = prefix + char
            child_node = node.get_child(char)
            if child_node.terminal:
                visit.append(string)
            # otherwise make it a prefix and keep going
            else:
                prefix = string
            # make a recursive call until we reach the end of the trie(with no children)
            self._traverse(child_node, prefix, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()