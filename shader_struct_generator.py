import bpy
import random


def linkInGroupNodes(shader_node, outout_node, input_node, root, num):
    if shader_node is None:
        return None
    sockets_names = ["Transmission",
                     "Alberto",
                     "Metallic",
                     "Specular",
                     "Roughness",
                     "Normal",
                     "Displacement"
                     ]
    map_sockets = [None,
                   [15, 0, 4, 5, 7, 19],
                   [0, 1, 2, 3, [4, 13], 29, 30]
                   ]
    root.links.new(outout_node.inputs[0], shader_node.outputs[0])
    for item in map_sockets[num]:
        index = map_sockets[num].index(item)
        if isinstance(item, int):
            root.links.new(shader_node.inputs[item], input_node.outputs[index])

        if isinstance(item, list):
            root.links.new(
                shader_node.inputs[item[0]], input_node.outputs[index])
            root.links.new(
                shader_node.inputs[item[1]], input_node.outputs[index])

        # if isinstance(item, str):
        #     root.inputs.new("NodeSocketString", item)


def createNodes(num, targetType):
    target = bpy.context.selected_objects[0]
    active_material_tree = target.active_material.node_tree
    offset = 1500 * num
    # create shader output
    shader_output = active_material_tree.nodes.new("ShaderNodeOutputMaterial")
    shader_output.location.x = offset + 200
    if targetType != "":
        shader_output.target = targetType
    # create shader group
    shader_group = active_material_tree.nodes.new("ShaderNodeGroup")
    shader_group.location.x = offset
    shader_group.node_tree = bpy.data.node_groups.new(
        "NodeGroup", "ShaderNodeTree")
    # create in group nodes
    group_tree = shader_group.node_tree
    group_labels = ["", "Eevee Shader", "Octane Shader"]
    if group_labels[num] != "":
        group_tree.name = group_labels[num]
    ingourp_output = group_tree.nodes.new("NodeGroupOutput")
    ingourp_output.location = (400, 0)
    ingourp_input = group_tree.nodes.new("NodeGroupInput")
    ingourp_input.location = (-400, -200)
    ingourp_shader = None
    if num == 1:
        ingourp_shader = group_tree.nodes.new("ShaderNodeBsdfPrincipled")
    elif num == 2:
        ingourp_shader = group_tree.nodes.new("ShaderNodeOctUniversalMat")
    # link in group nodes
    linkInGroupNodes(ingourp_shader, ingourp_output, ingourp_input,
                     group_tree, num)
    # link shader output
    if len(shader_group.outputs) != 0:
        active_material_tree.links.new(shader_output.inputs[0],
                                       shader_group.outputs[0])
    # other
    return None


def buildMaterialRenderModule(num=0):
    EngineTypes = ["", "BLENDER_EEVEE", "octane"]

    if EngineTypes[num] != "":
        bpy.context.scene.render.engine = EngineTypes[num]

    TargetTypes = ["", "EEVEE", "octane"]
    createNodes(num, TargetTypes[num])


# editorPanel button "Empty Struct"
class buildModuleEmptyStruct(bpy.types.Operator):
    """click to build an Empty Struct shader module"""
    bl_idname = "yt_shader.empty_struct"
    bl_label = "EmptyStruct"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule()
        return {'FINISHED'}


# editorPanel button "Eevee"
class buildModuleEevee(bpy.types.Operator):
    """click to build an Eevee shader module"""
    bl_idname = "yt_shader.eevee"
    bl_label = "Eevee"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule(1)
        return {'FINISHED'}


# editorPanel button "Octane"
class buildModuleOctane(bpy.types.Operator):
    """click to build an Octane shader module"""
    bl_idname = "yt_shader.octane"
    bl_label = "Octane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        buildMaterialRenderModule(2)
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
