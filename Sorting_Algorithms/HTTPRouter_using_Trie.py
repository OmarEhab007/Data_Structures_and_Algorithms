"""HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would
find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers
such as regular expressions or simple string matching,
but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about",
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
In a dynamic web server,
the content will often come from a block of code called a handler.
    """
"""
First we need to implement a slightly different Trie than
the one we used for autocomplete.
Instead of simple words the Trie will contain a part of the http path
at each node, building from the root node /

In addition to a path though,
we need to know which function will handle the http request.
طIn a real router we would probably pass an instance of a class like Python's
SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar
to how we did the autocomplete Trie, but this would result
in a Trie with a very large number of nodes and lengthy
traversals if we have a lot of pages on our site.
A more sensible way to split things would be on the
parts of the path that are separated by slashes ("/").
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
"""
"""
Next we need to implement the actual Router.
The router will initialize itself with a RouteTrie
for holding routes and associated handlers.
It should also support adding a handler by path and looking up a handler
by path. All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts,
so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router
which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes!
A request for '/about' or '/about/' are probably looking for the same page.
Requests for '' or '/' are probably looking for the root handler.
Handle these edge cases in your Router.
"""

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

    def find(self, path_part):
        # check if path_part is in this TrieNode
        if path_part in self.children:
            return True
        return False

    def __str__(self):
        # A description of this RouteTrieNode
        trie_children = self.children
        count_children = len(trie_children)
        desc = ""
        for key, value in trie_children.items():
            if count_children > 1 or count_children == 0:
                desc += str(key) + "=>" + str(value) + "\n"
            else:
                desc += str(key) + "=>" + str(value)

        return desc

# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node (root_handeler)
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path_part in path_parts:
            # Add a child node in this RouteTrie (insert: set handler to None)
            current_node.insert(path_part)
            # Advance to the next node
            current_node = current_node.children[path_part]
        # Assign the handler to the leaf node of this path (last part of the path)
        current_node.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        if path_parts is None:
            return None

        # Return the handler of the root if the composition of the path is only '/'
        if len(path_parts) == 0:
            return self.root.handler

        # traverse the RouteTrie and check the path_parts matching
        # A complete match returns the leaf node's handler of this path.
        for path_part in path_parts:
            # mismatching URL
            if not current_node.find(path_part):
                return None
            # Advance to the next node
            current_node = current_node.children[path_part]

        # reached the path's end
        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, url_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self._split_path(url_path)

        if path_parts != None:
            self.root_trie.insert(path_parts, handler)

    def lookup(self, url_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        # e.g. '' or '/' return the root handler
        path_parts = self._split_path(url_path)
        url_handler = self.root_trie.find(path_parts)
        if url_handler is None:
            return self.not_found_handler
        return url_handler

    # private helper method
    def _split_path(self, url_path):
        # you need to split the path of a URL into parts for
        # both the add_handler and lookup functions.

        # a valid url should be a string
        if url_path is None or type(url_path) != str:
            return None

        # Handling edge cases:
        # Requests for '/' or '' are probably looking for the root handler.
        # the root has no parts (empty list).
        if url_path == '/' or url_path == '':
            return []

        path_parts = url_path.split(sep='/')

        # a path part cannot be an empty string
        return [path_part for path_part in path_parts if path_part != '']

###########################################################################

# Here are some test cases and expected outputs you can use to test your implementation


def test_function(test_case):
    url_handler = test_case[0].lookup(test_case[1])
    solution = test_case[2]
    if url_handler == solution:
        return "Pass"
    else:
        return "Fail"


# create the router and add a route
router = Router("root handler", "not found handler")
print('\nCreate:\t router = Router("root handler", "not found handler")\n')

# Test Not valid input cases:
print('---- \t Testing Not valid inputs \t -----')
solution = "not found handler"

url = None
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup({}): {} \t{}'.format(url, solution, test))

url = 3
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup({}):    {} \t{}'.format(str(url), solution, test))

url = " "
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(str(url), solution, test))

# Testing Edge cases:
print('\n---- \t Testing Edge cases \t -----')
solution = "root handler"

url = "/"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(str(url), solution, test))

url = ""
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(str(url), solution, test))


# Add route
router.add_handler("/home/about", "about handler")  # add a route

print('\nRoute:\t router.add_handler("/home/about", "about handler")')


# some lookups with the expected output
print('\n---- \t Testing lookups search miss \t -----')
solution = "not found handler"

url = "/home"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): \t {} \t{}'.format(url, solution, test))

url = "home"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  \t {} \t{}'.format(url, solution, test))

url = "/home/about/me"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(url, solution, test))

print('\n---- \t Testing lookups search hit \t -----')
solution = "about handler"

url = "/home/about"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(url, solution, test))

url = "/home/about/"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(url, solution, test))

# Add route
router.add_handler("/home/about/me", "about me handler")
print('\nRoute:\t router.add_handler("/home/about/me", "about me handler")\n')

solution = "about me handler"
url = "/home/about/me"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(url, solution, test))
