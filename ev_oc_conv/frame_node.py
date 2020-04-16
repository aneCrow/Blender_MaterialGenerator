import bpy

class FrameNode:

    def __init__(self, node_tree, src):
        self.frame = node_tree.new("NodeFrame")
        self.copy_info(src)
        self.set_reroute(node_tree)
        self.set_location(src.location.x+ 4000, src.location.y)
        
    def copy_info(self, src):
        self.frame.label = src.label
        self.frame.color = src.color
        self.frame.use_custom_color = True
        self.frame.shrink = True
        self.frame.height = src.height
        self.frame.width = src.width
        self.textures = []
    
    def set_reroute(self, node_tree):
        self.reroute_frame1 = node_tree.new("NodeFrame")
        self.reroute_frame1.hide = True
        self.reroute_frame1.label = ""
        self.reroute_frame2 = node_tree.new("NodeFrame")
        self.reroute_frame2.hide = True
        self.reroute_frame2.label = ""
        self.reroute_frame1.shrink = True
        self.reroute_frame2.shrink = True
        self.reroute1 = node_tree.new("NodeReroute")
        self.reroute2 = node_tree.new("NodeReroute")
        self.reroute1.parent = self.reroute_frame1
        self.reroute2.parent = self.reroute_frame2
        self.reroute_frame1.parent = self.frame
        self.reroute_frame2.parent = self.frame
        self.reroute_frame2.location = self.frame.location.x+800, self.frame.location.y-200

    def set_location(self, x, y):
        self.frame.location = x,y

    def add_texture(self, node_tree, src, tar_type):
        new_texture = node_tree.new(tar_type)

        if len(self.textures) > 0:
            new_texture.parent = self.frame
            new_texture.location = self.textures[len(self.textures)-1].location.x+200, self.textures[len(self.textures)-1].location.y
        else:
            new_texture.location = self.frame.location.x+100, self.frame.location.y
            new_texture.parent = self.frame
        
        if (tar_type == "ShaderNodeOctImageTex" or tar_type == "ShaderNodeTexImage"):
            new_texture.image = src.image
        elif (tar_type == "ShaderNodeOctRGBSpectrumTex" or tar_type == "ShaderNodeRGB"):
            temp = new_texture.inputs.new("NodeSocketColor", "Color", identifier = "Color")
            print(temp.type, temp.name, temp.identifier)
            temp.default_value = src.inputs["Color"].default_value
        else:
            pass
            #print(src)
        self.textures.append(new_texture)

    def get_label(self):
        return self.frame.label