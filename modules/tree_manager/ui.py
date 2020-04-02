import bpy
from bpy.utils import register_class, unregister_class


class testOperator(bpy.types.Operator):
    """test"""
    bl_idname = "node.test"
    bl_label = "test"
    bl_options = {'REGISTER', 'UNDO'}

    test: bpy.props.BoolProperty()

    def execute(self, context):
        print(self.test)
        # message = ("Popup Values: % d"  %
        #            (self.test)
        #            )
        # self.report({'INFO'}, message)
        # print(context.active_node.keys())
        # print(list(context.space_data.edit_tree.nodes))
        # node = bpy.context.material.node_tree.nodes[0]
        # # node["test"] = bpy.props.BoolProperty(
        # #     update=lambda self, context: common_update(
        # #         self, context, 'my_bool_one')
        # # )
        # node["test"] = {"test": False}
        # bpy.ops.node.add_node(type="NodeFrame")

        return {'FINISHED'}

    # def invoke(self, context, event):
    #     wm = context.window_manager
    #     return wm.invoke_props_dialog(self)


class TestProps(bpy.types.PropertyGroup):

    test: bpy.props.StringProperty(default="testtest")


# ------------------------------------------------------------------------
# panel class
# ------------------------------------------------------------------------
class NODE_PT_TREE_MANAGER(bpy.types.Panel):
    """Manager the material trees"""
    bl_idname = "NODE_PT_TREE_MANAGER"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Tree"
    bl_context = ""
    bl_label = "Tree Manager"

    def draw(self, context):
        # ----------
        # props
        # ----------
        material = context.material

        if material is None:
            return None

        nodes = material.node_tree.nodes
        output_nodes = [
            x for x in nodes if x.bl_idname == "ShaderNodeOutputMaterial"
        ]
        has_output_nodes = len(output_nodes) != 0

        # ----------
        # layout
        # ----------
        layout = self.layout
        layout.operator("node.test", text="test").test = True
        if not has_output_nodes:
            return None

        for index, value in enumerate(output_nodes):
            layout.label(text="#" + str(index))
            root = layout.box()
            root.prop(value, "name")
            root.prop(value, "target")


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
classes = [
    NODE_PT_TREE_MANAGER,
    testOperator,
    TestProps
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
