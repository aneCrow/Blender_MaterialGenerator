from . import util
from . import node_socketsInfo

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
modules = [
    util,
    node_socketsInfo
]


def register():
    for c in modules:
        c.register()


def unregister():
    for c in modules:
        c.unregister()
