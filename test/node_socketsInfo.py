import bpy


# ------------------------------------------------------------------------
# panel props func
# ------------------------------------------------------------------------
def getStrProp():
    materials = bpy.data.materials
    if len(materials) == 0:
        return None
    query_nodes = [
        x for x in materials[0].node_tree.nodes if x.name == "String Prop"
    ]
    if len(query_nodes) == 0:
        return None
    store_node = query_nodes[0]
    if len(store_node.outputs) == 0:
        store_node.outputs.new("NodeSocketString", "String Prop")
    elif len(store_node.outputs) == 1:
        return store_node.outputs["String Prop"]
    else:
        return None


# ------------------------------------------------------------------------
# panel layout func
# ------------------------------------------------------------------------
def getSocketInfo(sockets, layout):
    if len(sockets) == 0:
        layout.enabled = False
        layout.label(text="- nothing")
    for socket in sockets:
        index = list(sockets).index(socket)
        # row 1
        row = layout.row()
        row.prop(socket, "enabled", text="# "+str(index))
        row2 = row.row()
        row2.scale_x = 1.5
        row2.prop(socket, "bl_idname", text="")
        # row 2
        row = layout.row()
        row.prop(socket, "hide")
        row2 = row.row()
        row2.scale_x = 1.5
        row2.prop(socket, "name", text="")
        row.enabled = socket.enabled

        layout.separator()


def getButtonAddSocket(operator, prop_type, layout):
    row = layout.row()
    # TODO: add function
    row.operator(operator, text="+")
    row2 = row.row()
    row2.scale_x = 1.65
    row2.prop(prop_type, "default_value", text="Type")


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
        # set a data store node
        prop_type = getStrProp()

        # ----------
        # layout
        # ----------
        layout = self.layout
        if target is None:
            return None
        # layout.operator("util.test", text="test")
        layout.prop(target, "bl_idname", text="Type")
        layout.prop(target, "name")

        # input sockets
        box = layout.box()
        box.label(text="INPUTs")
        # list
        getSocketInfo(target.inputs, box)
        # add button
        if prop_type is not None:
            getButtonAddSocket("util.test", prop_type, box)

        # output sockets
        box = layout.box()
        box.label(text="OUTPUTs")
        # list
        getSocketInfo(target.outputs, box)
        # add button
        if prop_type is not None:
            getButtonAddSocket("util.test", prop_type, box)


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
