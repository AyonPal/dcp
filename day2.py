class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print(self):
        iterator = self.head
        while(iterator):
            print(iterator.get_data())
            iterator = iterator.get_next()

    """
    Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

    For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
    """

    def removeZeroSum(self):
        iterator = self.head
        sum = 0
        umap = {}
        umap[sum] = Node(None)
        while(iterator):
            sum += iterator.get_data()
            # if sum already there add node to map
            if sum not in umap.keys():
                umap[sum] = iterator
            elif sum == 0:
                self.head = iterator.get_next()
            # else remove items after the previous detected sum and link to current items next
            else:
                umap[sum].set_next(iterator.get_next())
            iterator = iterator.get_next()


if (__name__ == "__main__"):
    ll = LinkedList()
    INPUTS = [1,2,3,-3,-2]
    for i in INPUTS[::-1]:
        ll.insert(i)
    ll.removeZeroSum()
    ll.print()
