from . import test

# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
modules = [
    test
]


def register():
    for c in modules:
        c.register()


def unregister():
    for c in modules:
        c.unregister()
