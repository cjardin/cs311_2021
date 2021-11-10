import random
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node:
    def __init__(self):
        self.children = []
        self.node_name = ''.join([random.choice(string.ascii_letters) for i in range(3)])

     def make_children(self, current_layer_number, node_per_layer_map):
        if current_layer_number >= len(node_per_layer_map):
            return

        for i in range( node_per_layer_map[current_layer_number] ):
            self.children.append( Node() )


        # add to professor's code to make first_born
        #first_born = self.children[0]
        # end of addition

        self.children[0].make_children( current_layer_number + 1, node_per_layer_map)

        for i in range(1, leng(self.children) ):
            self.children[i].children = self.children[0].children[:]
        

# takinig off what we did in class to put down at bottom            
#new_node = Node()
#new_node.children(0, NODE_COUNT_PER_LAYER)



# where we ended in class
# my trial of next part

    def adjust_child_weights(self):
        if len(self.children) = 0:
            return

        self.children_connection_weights = []
        
        for i in range( len(self.children) ):
            self.children_connection_weights.append( random.uniform(0, 1) )

            self.children[i].adjust_child_weights()


    def print_children(self, current_layer_number):
        indent = '    ' * layer

        if len(self.children) = 0:
            print(f"{indent}{self.node_name}")
            return

        print(f"{indent}{self.node_name} is connected to ")

        for i in range( len(self.children) ):
            self.children[i].print_children(current_layer_number + 1)

            if i < len( self.children_connection_weights ):
                print(f"{indent}with weight {self.children_connection_weights[i]} ")


new_node = []
master_node = Node()
self.children[0] = Node()
self.children[0].make_children(0, NODE_COUNT_PER_LAYER)
master_node.children.append( self.children[0] )

for i in range( 0, len(NODE_COUNT_PER_LAYER) ):
    new_node = Node()
    new_node.children = self.children[0].children[:]
    master_node.children.append new_node)
    
master_node.print_children(0)
print("!! Set Weights !!")

master_node.adjust_child_weights()
master_node.print_children(0)

