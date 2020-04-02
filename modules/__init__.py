from . import node_editor
from . import tree_manager


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
items = [
    node_editor,
    tree_manager
]


def register():
    for i in items:
        i.register()


def unregister():
    for i in items:
        i.unregister()
