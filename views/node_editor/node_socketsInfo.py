import bpy


# panel render enter class
class NODE_PT_test_sockets_info(bpy.types.Panel):
    """panel of node sockets info"""
    bl_idname = "NODE_PT_test_sockets_info"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Test'
    bl_context = 'sockets'
    bl_label = "Sockets Info"

    def draw(self, context):
        # ----------
        # props
        # ----------
        target = bpy.context.active_node

        # ----------
        # layout
        # ----------
        layout = self.layout
        if target is None:
            return None
        # layout.operator("view.test", text="test")
        layout.prop(target, "name")
        layout.prop(target, "bl_idname")
        box = layout.box()
        box.label(text="inputs")
        box.label(text="putputs")


# test operator
class testOperator(bpy.types.Operator):
    """test"""
    bl_idname = "view.test"
    bl_label = "test"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("test operator")

        test = bpy.context.material.name
        print(test)

        return {'FINISHED'}


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NODE_PT_test_sockets_info,
    testOperator
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
