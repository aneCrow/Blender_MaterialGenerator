import bpy

from . import frame_node

class TreeStruct:

    def __init__(self, node_tree):
        self.node_tree = node_tree
        self.build_tree()
        self.build_conv_dict()
        self.uncovered_node_type = set()

    def build_tree(self):
        self.frame_dict = dict()
        frames = [n for n in self.node_tree if n.type == "FRAME"]
        for f in frames:
            if f.parent == None:
                    temp = frame_node.FrameNode(self.node_tree, f)
                    self.frame_dict[temp.get_label()] = temp
    
    def copy_node(self, src):
        if src.parent != None and src.bl_idname != "NodeFrame" and src.bl_idname != "NodeReroute":
            
            if (src.parent.label in self.frame_dict):
                tar_type = self.convert_name(src.bl_idname)
                if tar_type != None:
                    self.frame_dict[src.parent.label].add_texture(self.node_tree, src, tar_type)
            else:
                print("cannot find target frame: ", src.parent.label)

            if src.bl_idname not in self.oc and src.bl_idname not in self.ev:
                self.uncovered_node_type.add(src.bl_idname)
                print(self.uncovered_node_type)

    def get_node_list(self):
        return [n for n in self.node_tree]

    def build_conv_dict(self):
        self.oc = {
            "ShaderNodeOctImageTex": "ShaderNodeTexImage",
            "ShaderNodeOctRGBSpectrumTex": "ShaderNodeRGB",
            "ShaderNodeOctUniversalMat": "ShaderNodeBsdfPrincipled",
            "ShaderNodeOutputMaterial": "ShaderNodeOutputMaterial",
        }

        self.ev = {
            "ShaderNodeTexImage": "ShaderNodeOctImageTex",
            "ShaderNodeRGB": "ShaderNodeOctRGBSpectrumTex",
            "ShaderNodeBsdfPrincipled": "ShaderNodeOctUniversalMat",
            "ShaderNodeOutputMaterial": "ShaderNodeOutputMaterial",
        }

    def convert_name(self, src_name):
        if src_name in self.oc:
            return self.oc[src_name]
        elif src_name in self.ev:
            return self.ev[src_name]

        #print("Cannot convert the given node type: ", src_name)
        return None

