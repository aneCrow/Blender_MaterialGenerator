import bpy
from bpy.utils import register_class, unregister_class


# ------------------------------------------------------------------------
# operator class
# ------------------------------------------------------------------------
class PrintNode_Operator(bpy.types.Operator):
    """print node"""
    bl_idname = "node.print_self"
    bl_label = "print node"

    def execute(self, context):
        print(bpy.context.active_node)
        return {'FINISHED'}


class AddSocket_Operator(bpy.types.Operator):
    """add socket"""
    bl_idname = "node.add_socket"
    bl_label = "add socket"

    # ----------
    # props
    # ----------
    step: bpy.props.StringProperty()
    socket_type: bpy.props.StringProperty()
    steps = [
        "Inputs",
        "Outputs"
    ]

    # ----------
    # execute
    # ----------
    def execute(self, context):
        index = self.steps.index(self.step)
        node = context.active_node
        # slicing off. e.g. NodeSocketBool -> Bool
        label = self.socket_type[10:]

        if index == 0:
            node.inputs.new(self.socket_type, label)
        if index == 1:
            node.Outputs.new(self.socket_type, label)
        return {'FINISHED'}


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    PrintNode_Operator,
    AddSocket_Operator
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
