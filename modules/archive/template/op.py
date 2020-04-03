import bpy
from bpy.utils import register_class, unregister_class


# ------------------------------------------------------------------------
# operator class
# ------------------------------------------------------------------------
class _Operator(bpy.types.Operator):
    """"""
    bl_idname = "."
    bl_label = ""

    # ----------
    # props
    # ----------

    # ----------
    # execute
    # ----------
    def execute(self, context):

        return {'FINISHED'}


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    _Operator
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
