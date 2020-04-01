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

import bpy
from . import modules

# ------------------------------------------------------------------------
# addon head info
# ------------------------------------------------------------------------
bl_info = {
    "name": "Shader Generator (Octane & Eevee)",
    "author": "aneCrow",
    "description": "Build Octane/Eevee shader node tree automatic.",
    "blender": (2, 81, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "WIP",
    "category": "Material"
}


# ------------------------------------------------------------------------
# UI root
# ------------------------------------------------------------------------
class root:
    def register():
        bpy.utils.register_class(NODE_PT_root)

    def unregister():
        bpy.utils.unregister_class(NODE_PT_root)


class NODE_PT_root(bpy.types.Panel):
    """Panel Of Generator"""
    bl_idname = "NODE_PT_root"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Generator'
    bl_context = 'root'
    bl_label = "Generator"

    def draw(self, context):
        from .modules.view import main_layout
        main_layout(self.layout)


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
items = [
    root,
    modules
]


def register():
    for c in items:
        c.register()


def unregister():
    for c in items:
        c.unregister()
