# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "testAddon",
    "author" : "hollow",
    "description" : "TestAddon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class TestOperation(bpy.types.Operator):
    bl_idname = "object.move_x"
    bl_label = "Move X by One"
    bl_options = {'REGISTER', 'UNDO'}

    def converter(self, src, tar_type, nodes, links):
        print("converting *", src.type, "* to *", tar_type, "*")
        new_node = nodes.new(tar_type)
        new_node.location = src.location.x, src.location.y
        
        if src.type == "OCT_IMAGE_TEX":
            new_node.image = src.image
        
        for o in src.outputs[0].links:
            to_socket = o.to_socket

            if src.outputs[0].is_linked:
                links.new(new_node.outputs[0], to_socket)

    def execute(self, context):
        print("IM HERE")
        materials = list(bpy.data.materials)
        for m in materials:
            nodes = m.node_tree.nodes
            links = m.node_tree.links
            
            i = 1
            for n in nodes:
                if n.type == "OCT_IMAGE_TEX":
                    self.converter(n, "ShaderNodeTexImage", nodes, links)
                #if n.type == "OCT_UNIVERSAL_MAT":
                    #universal = n
                #print("\n", i, " ", n.bl_idname,": ",n.type)
                #print("    ",n.inputs,",",n.color)
                #i+=1
                #types.add(n.type)
            #print(types)
            #for i in list(universal.inputs):
                #print(i)
        print("DONE")
        return {'FINISHED'}
            #for l in links:
                #print(l.from_node)
                
        

def register():
    print("Hello World")
    bpy.utils.register_class(TestOperation)

def unregister():
    print("Goodby World")
    bpy.utils.unregister_class(TestOperation)

if __name__ == '__main__':
    register()