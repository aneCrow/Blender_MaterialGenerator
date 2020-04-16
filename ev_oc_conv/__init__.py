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
    "name" : "EV_OC_CONV",
    "author" : "hollow",
    "description" : "Convert OC/EV nodes to EV/OC",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . import frame_node
from . import tree_struct

class TestOperation(bpy.types.Operator):
    bl_idname = "object.conv_oc"
    bl_label = "Convert OC/EV nodes to EV/OC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):       
        materials = list(bpy.data.materials)
        for m in materials:
            nodes = m.node_tree.nodes
            links = m.node_tree.links

            tree = tree_struct.TreeStruct(nodes)

            for n in tree.get_node_list():
                tree.copy_node(n)
            for l in links:
                print("From: ", l.from_node, l.from_socket, l.from_socket.identifier, l.from_socket.name)
                print("To: ", l.to_node, l.to_socket, l.to_socket.identifier, l.to_socket.name)

        print("DONE")
        return {'FINISHED'}
                
        

def register():
    print("Hello World")
    bpy.utils.register_class(TestOperation)

def unregister():
    print("Goodby World")
    bpy.utils.unregister_class(TestOperation)

if __name__ == '__main__':
    register()