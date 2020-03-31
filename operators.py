# this code forked from github aditiapratama/cycles-octane-converter
# https://github.com/aditiapratama/cycles-octane-converter

import bpy


def diffuse_convert():
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        diff_nodes = [n for n in nodes if n.type == 'BSDF_DIFFUSE']
        print(diff_nodes)
        for n in diff_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y
            n_color = n.inputs[0].default_value

            shader_oct_diff = nodes.new('ShaderNodeOctDiffuseMat')
            shader_oct_diff.location = n_loc_x, n_loc_y
            shader_oct_diff.inputs[0].default_value = n_color

            n_inputs = n.inputs[0]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_diff.inputs[0],
                    from_socket
                )

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_diff.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def mixmat_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        mix_nodes = [n for n in nodes if n.type == 'MIX_SHADER']
        print(mix_nodes)
        for n in mix_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y

            shader_oct_mix = nodes.new('ShaderNodeOctMixMat')
            shader_oct_mix.location = n_loc_x, n_loc_y

            n_inputs = n.inputs[1]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket_1 = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_mix.inputs[1],
                    from_socket_1
                )
            n_inputs = n.inputs[2]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket_2 = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_mix.inputs[2],
                    from_socket_2
                )

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_mix.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def image_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        img_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
        print(img_nodes)
        for n in img_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y
            n_image = n.image

            shader_oct_img = nodes.new('ShaderNodeOctImageTex')
            shader_oct_img.location = n_loc_x, n_loc_y
            shader_oct_img.image = n_image

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_img.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def floatimg_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        floatimg_nodes = [n for n in nodes if n.type == 'TEX_IMAGE'
                          and n.color_space == 'NONE']
        print(floatimg_nodes)
        for n in floatimg_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y
            n_image = n.image

            shader_oct_floatimg = nodes.new('ShaderNodeOctFloatImageTex')
            shader_oct_floatimg.location = n_loc_x, n_loc_y
            shader_oct_floatimg.image = n_image

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_floatimg.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def glossy_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        glossy_nodes = [n for n in nodes if n.type == 'BSDF_GLOSSY']
        print(glossy_nodes)
        for n in glossy_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y
            n_color = n.inputs[0].default_value

            shader_oct_glossy = nodes.new('ShaderNodeOctGlossyMat')
            shader_oct_glossy.location = n_loc_x, n_loc_y
            shader_oct_glossy.inputs[0].default_value = n_color

            n_inputs = n.inputs[0]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_glossy.inputs[0],
                    from_socket
                )

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_glossy.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def principled_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        principled_nodes = [n for n in nodes if n.type == 'BSDF_PRINCIPLED']
        print(principled_nodes)
        for n in principled_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y
            n_color = n.inputs[0].default_value
            n_specular = n.inputs['Specular'].default_value
            n_roughness = n.inputs['Roughness'].default_value
            n_ior = n.inputs['IOR'].default_value

            shader_oct_glossy = nodes.new('ShaderNodeOctGlossyMat')
            shader_oct_glossy.location = n_loc_x, n_loc_y
            shader_oct_glossy.inputs[0].default_value = n_color
            shader_oct_glossy.inputs['Specular'].default_value = n_specular
            shader_oct_glossy.inputs['Roughness'].default_value = n_roughness
            shader_oct_glossy.inputs['Index'].default_value = n_ior

            diff_input = n.inputs['Base Color']
            i_links = [i for i in diff_input.links]
            for i in i_links:
                from_socket_diff = i.from_socket

            if diff_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Diffuse'],
                    from_socket_diff
                )

            spec_input = n.inputs['Specular']
            i_links = [i for i in spec_input.links]
            for i in i_links:
                from_socket_spec = i.from_socket

            if spec_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Specular'],
                    from_socket_spec
                )

            rough_input = n.inputs['Roughness']
            i_links = [i for i in rough_input.links]
            for i in i_links:
                from_socket_rough = i.from_socket

            if rough_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Roughness'],
                    from_socket_rough
                )

            normal_input = n.inputs['Normal']
            i_links = [i for i in normal_input.links]
            for i in i_links:
                from_socket_normal = i.from_socket

            if normal_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Normal'],
                    from_socket_normal
                )

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_glossy.outputs[0],
                    to_socket
                )
            nodes.remove(n)


def glass_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        glossy_nodes = [n for n in nodes if n.type == 'BSDF_GLASS']
        print(glossy_nodes)
        for n in glossy_nodes:
            n_loc_x = n.location.x
            n_loc_y = n.location.y - 225
            n_color = n.inputs[0].default_value

            shader_oct_glass = nodes.new('ShaderNodeOctSpecularMat')
            shader_oct_glass.location = n_loc_x, n_loc_y
            shader_oct_glass.inputs[1].default_value = n_color

            n_outputs = n.outputs[0]
            o_links = [o for o in n_outputs.links]
            for o in o_links:
                to_socket = o.to_socket

            if n_outputs.is_linked:
                links.new(
                    shader_oct_glass.outputs[0],
                    to_socket
                )
            nodes.remove(n)


# panel engine button execute class
class convertMaterial(bpy.types.Operator):
    """click to convert material"""
    bl_idname = "material.convert"
    bl_label = "Convert Material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("test")
        return {'FINISHED'}


def register():
    from bpy.utils import register_class

    register_class(convertMaterial)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(convertMaterial)


if __name__ == "__main__":
    # register()
    diffuse_convert()
