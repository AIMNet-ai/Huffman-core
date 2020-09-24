from itertools import groupby
import heapq as hq

# -1 if a<b

# 0 if a=b

# 1 if a>b


def cmp(a, b, flag):

    if(a == b):
        return False
    else:
        if(flag == "gt"):
            if(a < b):
                return False
            else:
                return True
        else:
            if(a < b):
                return True
            else:
                return False


class Node(object):
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __repr__(self):
        return "%s - %s -- %s _ %s" % (self.item, self.weight, self.left, self.right)

    # def __cmp__(self, a):
    #     return cmp(self.weight, a.weight)

    def __lt__(self, other):
        return cmp(self.weight, other.weight, flag="lt")

    def __gt__(self, other):
        return cmp(self.weight, other.weight, flag="gt")


a = Node("Maa", 10)
b = Node("papa", 20)
print(a < b)


def huffman(input):
    itemqueue = [Node(a, len(list(b))) for a, b in groupby(sorted(input))]

    hq.heapify(itemqueue)
    while len(itemqueue) > 1:
        l = hq.heappop(itemqueue)
        r = hq.heappop(itemqueue)
        n = Node(None, r.weight+l.weight)
        n.setChildren(l, r)
        hq.heappush(itemqueue, n)

    codes = {}

    def codeIt(s, node):
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            codeIt(s+"0", node.left)
            codeIt(s+"1", node.right)

    codeIt("", itemqueue[0])
    return codes, "".join([codes[a] for a in input])


input = "aababcabcd"
print(huffman(input))
# ({'a': '0', 'c': '111', 'b': '10', 'd': '110'}, '0010010111010111110')
