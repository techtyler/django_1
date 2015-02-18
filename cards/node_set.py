

import card_node

#do i want this to inherit from a set or something?
class node_set(object):
    
    def new:
        nodes = set()
        
    def find_or_add(_id):
        node = [n for n in nodes if n.id == _id]
        if len(node) == 0:
            node = card_node(_id)
            nodes.add(node)
        else:
            node = node[0]
        return node
    
    def remove(node, edge_node):
        node.rm_edge(edge_node)
        nodes.remove(node)
        #TODO: Make sure i dont' delete the node when i have two 4s and drop one edge
        
    def size():
        return len(nodes)
        