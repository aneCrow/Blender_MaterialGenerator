import bpy
from bpy.utils import register_class, unregister_class


# ------------------------------------------------------------------------
# panel props
# ------------------------------------------------------------------------
class Static:
    socket_types = ["NodeSocketBool",
                    "NodeSocketColor",
                    "NodeSocketFloat",
                    "NodeSocketFloatAngle",
                    "NodeSocketFloatFactor",
                    "NodeSocketFloatPercentage",
                    "NodeSocketFloatTime",
                    "NodeSocketFloatUnsigned",
                    "NodeSocketInt",
                    "NodeSocketIntFactor",
                    "NodeSocketIntPercentage",
                    "NodeSocketIntUnsigned",
                    "NodeSocketShader",
                    "NodeSocketString",
                    "NodeSocketVector",
                    "NodeSocketVectorAcceleration",
                    "NodeSocketVectorDirection",
                    "NodeSocketVectorEuler",
                    "NodeSocketVectorTranslation",
                    "NodeSocketVectorVelocity",
                    "NodeSocketVectorXYZ",
                    "NodeSocketVirtual"]
    enum_items = [(str(index), socket, "")
                  for index, socket in enumerate(socket_types)]


class NodeEditor_Props(bpy.types.PropertyGroup):
    addButton_socketTypeS: bpy.props.StringProperty()
    addButton_socketTypeE: bpy.props.EnumProperty(name="Socket Types",
                                                  items=Static.enum_items,
                                                  default="0",)


# ------------------------------------------------------------------------
# panel class
# ------------------------------------------------------------------------
def mapSocketsLayout(sockets: bpy.types.NodeInputs,
                     layout: bpy.types.UILayout,
                     label: str):
    # ----------
    # props
    # ----------
    has_sockets = len(sockets) != 0
    add_socket_operator = "node.add_socket"
    props = bpy.context.scene.NodeEditor_Props
    prop_name = "addButton_socketTypeE"
    socket_type = Static.socket_types[int(props.addButton_socketTypeE)]

    # ----------
    # layout
    # ----------
    layout.label(text=label+":")

    if not has_sockets:
        column = layout.column()
        column.enabled = False
        column.label(text="Not socket here.")
    else:
        for index, item in enumerate(sockets):
            # row 1
            row = layout.row()
            row.prop(item, "enabled", text="# "+str(index))
            row2 = row.row()
            row2.scale_x = 1.5
            row2.prop(item, "bl_idname", text="")
            # row 2
            row = layout.row()
            row.prop(item, "hide")
            row2 = row.row()
            row2.scale_x = 1.5
            row2.prop(item, "name", text="")
            row.enabled = item.enabled
            # separator
            layout.separator()
    row = layout.row()
    op = row.operator(add_socket_operator)
    op.step = label
    op.socket_type = socket_type
    row.prop(props, prop_name, text="")


class NODE_PT_EDITOT(bpy.types.Panel):
    """Node Editor"""
    bl_idname = "NODE_PT_EDITOT"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Item"
    bl_context = ""
    bl_label = "Node Editor"

    def draw(self, context):
        # ----------
        # props
        # ----------
        target = bpy.context.active_node
        if target is None:
            return None
        inputs = target.inputs
        outputs = target.outputs

        # ----------
        # layout
        # ----------
        layout = self.layout

        layout.operator("node.print_self", text="test")
        layout.prop(target, "parent")
        layout.prop(target, "bl_idname", text="Type")

        layout.prop(target, "name")
        layout.prop(target, "label")

        layout.prop(target, "hide")
        layout.prop(target, "show_options")
        layout.prop(target, "show_preview")

        layout.prop(target, "use_custom_color")
        if target.use_custom_color:
            layout.prop(target, "color")

        mapSocketsLayout(inputs,
                         layout.box(),
                         "Inputs")
        mapSocketsLayout(outputs,
                         layout.box(),
                         "Outputs")
        # TODO: add links and options map layout


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NodeEditor_Props,
    NODE_PT_EDITOT
]


def register():
    for c in classes:
        register_class(c)
    bpy.types.Scene.NodeEditor_Props = bpy.props.PointerProperty(
        type=NodeEditor_Props)


def unregister():
    for c in classes:
        unregister_class(c)
    del(bpy.types.Scene.NodeEditor_Props)


# test
if __name__ == "__main__":
    register()
