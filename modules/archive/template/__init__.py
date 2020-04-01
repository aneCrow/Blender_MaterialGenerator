from . import ui
from . import op

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
items = [
    ui,
    op
]


def register():
    for c in items:
        c.register()


def unregister():
    for c in items:
        c.unregister()
