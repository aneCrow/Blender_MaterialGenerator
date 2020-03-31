import bpy


# ------------------------------------------------------------------------
# 1 useful funcs
# ------------------------------------------------------------------------
def parseNodeSockets(node):
    """parse material node inputs & outputs"""
    sockets_dict = {
        "inputs": [],
        "outputs": []
    }
    return sockets_dict


# test
if __name__ == "__main__":
    register()
    # parseNodeSockets=
    # parseNodeSockets(None)


# ------------------------------------------------------------------------
# 2 test class
# ------------------------------------------------------------------------
class testOperator(bpy.types.Operator):
    """test"""
    bl_idname = "util.test"
    bl_label = "test"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("test operator")

        # print("")

        return {'FINISHED'}


# ------------------------------------------------------------------------
# 3 register and unregister
# ------------------------------------------------------------------------
classes = [
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
