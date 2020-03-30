import bpy
import random


def buildMaterialRenderModule(Type="ALL"):
    # get nodes
    target_nodes = bpy.context.selected_objects[0].active_material.node_tree.nodes

    # build module node
    nodeGroup = target_nodes.new('ShaderNodeGroup')
    nodeGroup.location = (random.randrange(-1000, 1000, 50),
                          0)
    nodeTree = bpy.data.node_groups.new("NodeGroup", "ShaderNodeTree")
    nodeGroup.node_tree = nodeTree
    # define module inputs
    sockets_name = ["Transmission",
                    "Alberto",
                    "Metallic",
                    "Specular",
                    "Roughness",
                    "Normal",
                    "Displacement"
                    ]
    for name in sockets_name:
        nodeTree.inputs.new('NodeSocketFloat', name)
    # define module nodes
    module_nodes = nodeTree.nodes
    # define input
    module_input = module_nodes.new("NodeGroupInput")
    module_input.location = (-400, -200)
    # define output
    module_output = module_nodes.new("ShaderNodeOutputMaterial")
    module_output.location = (400, 0)
    module_output.target = Type
    # define shader
    if Type == "EEVEE":
        bpy.context.scene.render.engine = "BLENDER_EEVEE"
        nodeTree.name = "Eevee Render"
        module_shader = module_nodes.new("ShaderNodeBsdfPrincipled")
        # link output
        nodeTree.links.new(module_output.inputs["Surface"],
                           module_shader.outputs["BSDF"])

        link_ins = module_shader.inputs
        link_outs = module_input.outputs
        # link input
        nodeTree.links.new(link_ins["Transmission"],
                           link_outs["Transmission"])
        nodeTree.links.new(link_ins["Base Color"],
                           link_outs["Alberto"])
        nodeTree.links.new(link_ins["Metallic"],
                           link_outs["Metallic"])
        # nodeTree.links.new(link_ins["Specular"], link_outs["Specular"])
        nodeTree.links.new(link_ins["Roughness"],
                           link_outs["Roughness"])
        nodeTree.links.new(link_ins["Normal"],
                           link_outs["Normal"])
        # nodeTree.links.new(link_ins["Displacement"],
        #                    link_outs["Displacement"])
    elif Type == "octane":
        bpy.context.scene.render.engine = "octane"
        nodeTree.name = "Octane Render"
        module_shader = module_nodes.new("ShaderNodeOctUniversalMat")
        # link output
        nodeTree.links.new(module_output.inputs["Surface"],
                           module_shader.outputs["OutMat"])

        link_ins = module_shader.inputs
        link_outs = module_input.outputs
        # link input
        nodeTree.links.new(link_ins["Transmission"],
                           link_outs["Transmission"])
        nodeTree.links.new(link_ins["Albedo color"],
                           link_outs["Alberto"])
        nodeTree.links.new(link_ins["Metallic"],
                           link_outs["Metallic"])
        nodeTree.links.new(link_ins["Specular"],
                           link_outs["Specular"])
        nodeTree.links.new(link_ins["Roughness"],
                           link_outs["Roughness"])
        nodeTree.links.new(link_ins["Normal"],
                           link_outs["Normal"])
        nodeTree.links.new(link_ins["Displacement"],
                           link_outs["Displacement"])


# editorPanel button "Empty Struct"
class buildModuleEmptyStruct(bpy.types.Operator):
    """click to build an Empty Struct shader module"""
    bl_idname = "yt_shader.empty_struct"
    bl_label = "EmptyStruct"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule()
        return {'FINISHED'}


# editorPanel button "Octane"
class buildModuleOctane(bpy.types.Operator):
    """click to build an Octane shader module"""
    bl_idname = "yt_shader.octane"
    bl_label = "Octane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule("octane")
        return {'FINISHED'}


# editorPanel button "Eevee"
class buildModuleEevee(bpy.types.Operator):
    """click to build an Eevee shader module"""
    bl_idname = "yt_shader.eevee"
    bl_label = "Eevee"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule("EEVEE")
        return {'FINISHED'}


def register():
    from bpy.utils import register_class

    register_class(buildModuleEmptyStruct)
    register_class(buildModuleOctane)
    register_class(buildModuleEevee)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(buildModuleEmptyStruct)
    unregister_class(buildModuleOctane)
    unregister_class(buildModuleEevee)


# test
if __name__ == "__main__":
    buildMaterialRenderModule()
    buildMaterialRenderModule("EEVEE")
    buildMaterialRenderModule("octane")
    register()
