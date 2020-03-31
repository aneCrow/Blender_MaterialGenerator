import bpy


# ------------------------------------------------------------------------
# panel class
# ------------------------------------------------------------------------
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
        layout.prop(target, "bl_idname", text="Type")
        layout.prop(target, "name")

        def socketInfoLayout(sockets, layout):
            for socket in sockets:
                index = list(sockets).index(socket)
                # row 1
                row = layout.row()
                row.prop(socket, "enabled", text="# "+str(index))
                row2 = row.row()
                row2.scale_x = 1.65
                row2.prop(socket, "bl_idname", text="")
                # row 2
                row = layout.row()
                row.prop(socket, "hide")
                row2 = row.row()
                row2.scale_x = 1.65
                row2.prop(socket, "name", text="")
                row.enabled = socket.enabled

                layout.separator()

        box = layout.box()
        box.label(text="INPUTs")
        socketInfoLayout(target.inputs, box)
        box = layout.box()
        box.label(text="OUTPUTs")
        socketInfoLayout(target.outputs, box)


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NODE_PT_test_sockets_info
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
