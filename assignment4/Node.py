import random
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node:
    def __init__(self):
        self.children = []
        self.weight = []
        self.node_name = ''
        random_letters = []

        for i in range(3):
            random_letters.append(random.choice(string.ascii_letters))
            
        self.node_name = ''.join(random_letters)
        ''.join([random.choice(string.ascii_letters) for i in range(3)])

    def make_children(self, layer, node_per_layer_map):
        if layer >= len(node_per_layer_map):
            return

        for i in range(node_per_layer_map[layer]):
            self.children.append(Node())

        first_node = self.children[0]
        first_node.make_children(layer + 1, node_per_layer_map)
    
        for i in range(1, len(self.children)):
            self.children[i].children = first_node.children[:] 

    def adjust_child_weights(self, layer, node_per_layer_map):
        #if len(self.children) == 0:
         #   return

        if layer >= len(node_per_layer_map):
            return

        self.weight = [0.0] * len(self.children)
        for i in range(len(self.children)):
            #self.weight[i].append(random.uniform(0, 1))
            self.weight[i] = random.uniform(0,1)
            self.children[i].adjust_child_weights(layer + 1, node_per_layer_map)
        return

    def print_children(self, layer, node_per_layer_map):
        indent = '    ' *  layer

        if layer >= len(node_per_layer_map):
            print(f"{indent} {self.node_name}")
            return

        #if len(self.children) == 0:
         #   print(f"{indent}{self.node_name}")
          #  return

        print(f"{indent} {self.node_name} is connected to:")

        for i in range(len(self.children)):
            try:
                print(f"{indent} Weight of {self.weight[i]}")
            except:
                pass
            self.children[i].print_children(layer + 1, node_per_layer_map)
        return
            

nodes = []
master_node = Node()
#first_node = Node()
#first_node.make_children(0, NODE_COUNT_PER_LAYER)

master_node.make_children(0, NODE_COUNT_PER_LAYER)
master_node.print_children(0, NODE_COUNT_PER_LAYER)
print("SET WEIGHTS:")
master_node.adjust_child_weights(0, NODE_COUNT_PER_LAYER)
master_node.print_children(0, NODE_COUNT_PER_LAYER)

