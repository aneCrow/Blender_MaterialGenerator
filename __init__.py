# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import main_panel
from . import test

# ------------------------------------------------------------------------
# addon head info
# ------------------------------------------------------------------------
bl_info = {
    "name": "Shader Generator (Octane & Eevee)",
    "author": "aneCrow",
    "description": "Build Octane/Eevee shader node tree automatic.",
    "blender": (2, 81, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "WIP",
    "category": "Material"
}


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------
modules = [
    main_panel,
    test
]


def register():
    for c in modules:
        c.register()


def unregister():
    for c in modules:
        c.unregister()
