import bpy


# ------------------------------------------------------------------------
# panel class
# ------------------------------------------------------------------------
class NODE_PT_test(bpy.types.Panel):
    """test"""
    bl_idname = "NODE_PT_test"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Test"
    bl_context = "test"
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
    NODE_PT_test
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
