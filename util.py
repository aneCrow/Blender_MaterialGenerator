import bpy


def getSelectedObject():
    return bpy.context.active_object


def parseNodeSockets(node):
    """parse material node inputs & outputs"""
    sockets_dict = {
        "inputs": [],
        "outputs": []
    }
    return sockets_dict


def panel_node(layout):
    box = layout.box()
    box.operator("test.test",
                 text="test")
    text = getSelectedObject().name
    box.label(text=text)


# test
class testOperator(bpy.types.Operator):
    """test"""
    bl_idname = "test.test"
    bl_label = "test"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("test operator")

        # print(len(getSelectedObject()))

        return {'FINISHED'}


def register():
    from bpy.utils import register_class

    register_class(testOperator)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(testOperator)


# test
if __name__ == "__main__":
    register()
    # parseNodeSockets=
    # parseNodeSockets(None)
