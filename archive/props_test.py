import bpy


class QueryProps(bpy.types.PropertyGroup):

    query: bpy.props.StringProperty(default="testtest")


class SelectByQuery(bpy.types.Operator):

    bl_idname = "object.select_by_query"
    bl_label = "Selection of object by query"

    def execute(self, context):
        try:
            bpy.data.objects[self.query].select_set(True)
            return {'FINISHED'}
        # except:
        #     print('Could not select object')
        #     return {'CANCELLED'}


class PanelThree(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_SelectionQuery"
    bl_label = "Selection Query"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        props = bpy.context.scene.QueryProps
        layout = self.layout

        col = layout.column(align=True)
        rowsub = col.row(align=True)

        rowsub.label(text="SELECT *")

        rowsub = col.row(align=True)
        col2 = layout.column()
        rowsub2 = col2.row()
        rowsub2.operator("object.select_by_query", text="Query")
        rowsub.prop(props, "query", text="")


classes = (
    QueryProps,
    SelectByQuery,
    PanelThree
)


def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # Register QueryProps
    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProps)


def unregister():

    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    # $ delete QueryProps on unregister
    del(bpy.types.Scene.QueryProps)


if __name__ == "__main__":
    register()
