from .operators import MYFIRSTADDON_OT_test
from .panel import MYFIRSTADDON_PT_main_panel
import bpy.types
import bpy
bl_info = {
    "name": "My First Addon",
    "author": "Nn Nn",
    "description": "This is my first addon...",
    "version": (1, 0),
    "blender": (2, 90, 2),
    "location": "View3D > Object > My First Addon",
    "warning": "",
    "category": "Object"
}

# Blender imports

# Import Panel

# Import Operators

classes = (MYFIRSTADDON_OT_test,
           MYFIRSTADDON_PT_main_panel)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
