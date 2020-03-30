import bpy


renderEngineTypesDict = {
    "octane": "Octane",
    "BLENDER_EEVEE": "Eevee"
}


# panel engine button execute class
class toggleRenderEngine(bpy.types.Operator):
    """click to toggle render engine"""
    bl_idname = "render.change_engine"
    bl_label = "change_engine"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        render = bpy.context.scene.render
        # toggle engine with Octane or Eevee
        if render.engine == "octane":
            render.engine = "BLENDER_EEVEE"
        elif render.engine == "BLENDER_EEVEE":
            render.engine = "octane"
        # skip if other engine
        return {'FINISHED'}


# panel render enter class
class renderUtil(bpy.types.Panel):
    """panel of material utils"""
    bl_idname = "OBJECT_PT_renderUtil"
    bl_label = "Conver Material - YUNTAI"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    # def draw_header(self, context):
    #     layout = self.layout

    #     layout.label(text=render_engine)

    def draw(self, context):
        layout = self.layout

        # control render engine
        # TODO: change function to spicific render output item
        render_engine = bpy.context.scene.render.engine
        if renderEngineTypesDict.__contains__(render_engine):
            render_engine = renderEngineTypesDict[render_engine]
        else:
            render_engine = "Other"
        row_engine = layout.row()
        row_engine.label(text="Engine:")
        row_engine.operator("render.change_engine", text=render_engine)

        layout.separator()

        # object panel
        selected_objs = bpy.context.selected_objects
        if len(selected_objs) == 0:
            # nothing selected
            layout.label(text="Selected an object first.")
        else:
            # object name
            row_engine.alignment = "CENTER"
            layout.label(text=selected_objs[0].name)
            row_engine.alignment = "EXPAND"

            # object material info
            nodes_material = selected_objs[0].active_material.node_tree.nodes
            nodes_outputs = [
                # filter output material nodes
                x for x in nodes_material if x.type == "OUTPUT_MATERIAL"
            ]
            for node in nodes_outputs:
                box = layout.box()
                active_info = ""
                if False:
                    # TODO: check current use node
                    active_info = " Active"
                # index
                box.label(text="# " +
                          str(nodes_outputs.index(node)) +
                          ":" +
                          active_info
                          )
                layout.separator()
                box.label(text=node.name)
                box.label(text="output target: " + node.target)
                box.operator("material.convert")


def register():
    from bpy.utils import register_class

    register_class(toggleRenderEngine)
    register_class(renderUtil)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(toggleRenderEngine)
    unregister_class(renderUtil)


# test
if __name__ == "__main__":
    register()
