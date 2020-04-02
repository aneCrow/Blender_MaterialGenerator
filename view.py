import bpy
from bpy.types import UILayout


def main_layout(layout: UILayout):
    layout = layout.column()
    layout.enabled = False
    layout.label(text="This Addon in WIP")
