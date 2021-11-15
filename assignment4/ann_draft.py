import random
import string
import networkx as nx

NODE_COUNT_PER_LAYER = [4,3,2]

#trial
G = nx.MultiDiGraph()
#

class Node:
    def __init__(self):
        self.children = []
        self.node_name = ''
        
        for i in range(3):
            self.node_name += self.node_name.join([random.choice(string.ascii_letters)])
            
        self.children_connection_weights = []

    def make_children(self, current_layer_number, node_per_layer_map):
        # >=
        if current_layer_number == len(node_per_layer_map):
            return

        for i in range(node_per_layer_map[current_layer_number]):
            self.children.append( Node())

        # add to professor's code to make first_born
        first_born = self.children[0]
        # end of addition

        first_born.make_children(current_layer_number + 1, node_per_layer_map)
    

        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]

    def adjust_child_weights(self):
        
        if len(self.children) == 0:
            return

        self.children_connection_weights = []

        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0, 1))
            G.add_node(self.children[i].adjust_child_weights())

    def print_children(self, layer):
        indent = '    ' *  layer

        if len(self.children) == 0:
            print(f"{indent}{self.node_name}")
            return

        print(f"{indent}{self.node_name} is connected to ")


        for i in range(len(self.children)):
            self.children[i].print_children(layer + 1)
            
            if i < len(self.children_connection_weights):
                print(f"{indent}with weight {self.children_connection_weights[i]} ")

    
       #def add_edges(self, edge):
        
     #   for i in range(len(self.edges)):
       #     G.add_edges_from(edges[i].add_edges(edge + 1))
      #      edges[i] = ([(self.children[i].print_children(layer), self.children[i].print_children(layer + 1))])

                

nodes = []
master_node = Node()
first_born = Node()
first_born.make_children(0, NODE_COUNT_PER_LAYER)
master_node.children.append(first_born)

for i in range(0, len(NODE_COUNT_PER_LAYER)):
    new_node = Node()
    #G.add_noode(new_node)
    new_node.children = first_born.children[:]
    master_node.children.append(new_node)
    #G.add_node(new_node)

master_node.print_children(0)
print("SET WEIGHTS:")

#G.add_nodes_from(master_node.print_children(0))
master_node.adjust_child_weights()
#G.add_weighted_edges_from(master_node.print_children(0))
master_node.print_children(0)

nx.draw_networkx(G)


