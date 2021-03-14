from .operators import LyricsVideoAddOn_OT
from .panel import LyricsVideoAddOn_PT_main_panel
import bpy.types
import bpy
bl_info = {
    "name": "Lyrics Video Generator",
    "author": "Kevin Isabelle",
    "description": "This plugin reads a script file with lyrics and frames.",
    "version": (1, 0),
    "blender": (2, 90, 2),
    "location": "View3D > Object > Lyrics Video Generator",
    "warning": "",
    "category": "Object"
}

classes = (LyricsVideoAddOn_OT,
           LyricsVideoAddOn_PT_main_panel)


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
