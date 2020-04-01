from . import util
from . import node_socketsInfo

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
items = [
    util,
    node_socketsInfo
]


def register():
    for c in items:
        c.register()


def unregister():
    for c in items:
        c.unregister()
