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
    for i in items:
        i.register()


def unregister():
    for i in items:
        i.unregister()
