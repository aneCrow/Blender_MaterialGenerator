import bpy

renderEngineTypesDict = {
    "octane": "Octane",
    "BLENDER_EEVEE": "Eevee"
}

# panel render enter class


class editorPanel(bpy.types.Panel):
    """panel of shader node tree generator"""
    bl_idname = "OBJECT_PT_YUNTAI_shader_generator"
    bl_label = "Shader Generator"
    bl_region_type = "WINDOW"
    bl_space_type = "PROPERTIES"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header_preset(self, context):
        layout = self.layout.row(align=True)
        layout.enabled = False
        layout.label(text="|    YUNTAI    |")

    def draw(self, context):
        layout = self.layout

        selected_objs = bpy.context.selected_objects
        if len(selected_objs) == 0:
            # nothing selected
            layout.label(text="Selected an object first.")
            return None

        # object name
        # TODO: build the selection object list
        layout.label(text=selected_objs[0].name)

        layout.separator()

        layout.label(text="build shader module")
        row = layout.row(align=True)
        row.operator("yt_shader.empty_struct",
                     text="Empty Struct")
        row.operator("yt_shader.octane",
                     text="Octane")
        row.operator("yt_shader.eevee",
                     text="Eevee")

        layout.separator()

        box = layout.box()


def register():
    from bpy.utils import register_class

    register_class(editorPanel)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(editorPanel)


# test
if __name__ == "__main__":
    register()
