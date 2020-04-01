import bpy


# ------------------------------------------------------------------------
# UI root
# ------------------------------------------------------------------------
class NODE_PT_root(bpy.types.Panel):
    """Panel Of Generator"""
    bl_idname = "NODE_PT_root"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Generator'
    bl_context = 'root'
    bl_label = "Shader Generator"

    def draw(self, context):
        ...


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NODE_PT_root
]


def register():
    from bpy.utils import register_class

    for c in classes:
        register_class(c)


def unregister():
    from bpy.utils import unregister_class

    for c in classes:
        unregister_class(c)


# test
if __name__ == "__main__":
    register()
