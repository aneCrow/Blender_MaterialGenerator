import bpy

class FrameNode:

    def __init__(self, node_tree, img = None ,label = "default frame"):
        self.frame = node_tree.new("NodeFrame")
        self.img = img
        self.reroute = None
        frame.bl_label = label
        
    def copy_image(self, node_tree, src, tar_type):
        """
        copy the src image texture node and create a new texture node of tar_type
        attach the new node to node_tree
        """ 
        self.img = node_tree.new(tar_type)
        self.img.image = src.image

    def new_reroute(self, node_tree):
        print("Create a new reroute")
        self.reroute = node_tree.new("NodeReroute")

    def set_location(self, x, y):
        self.frame.location = x,y
        if (self.img != None):
            self.img.location = x,y
        if (self.reroute != None)
            self.reroute.location = x,y