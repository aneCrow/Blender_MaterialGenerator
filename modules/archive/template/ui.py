import bpy
from bpy.utils import register_class, unregister_class


# ------------------------------------------------------------------------
# panel class
# ------------------------------------------------------------------------
class NODE_PT_(bpy.types.Panel):
    """..."""
    bl_idname = "NODE_PT_"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = ""
    bl_context = ""
    bl_label = ""

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header(self, context):
        ...

    def draw_header_preset(self, context):
        ...

    def draw(self, context):
        # ----------
        # props
        # ----------

        # ----------
        # layout
        # ----------
        layout = self.layout


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NODE_PT_
]


def register():
    for c in classes:
        register_class(c)


def unregister():
    for c in classes:
        unregister_class(c)


# test
if __name__ == "__main__":
    register()
