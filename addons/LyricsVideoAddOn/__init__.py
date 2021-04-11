from .operators import LyricsVideoAddOn_OT, SelectLyricsFile_OT, SelectMainWav_OT, LyricsVideoAddOn_InsertWaves, LyricsFrameHandler
from .panel import LyricsVideoAddOn_PT_main_panel
import bpy.types
from bpy.props import IntProperty, StringProperty
import bpy
bl_info = {
    "name": "Lyrics Video Generator",
    "author": "Kevin Isabelle",
    "description": "This plugin reads a script file with lyrics and frames.",
    "version": (1, 0),
    "blender": (2, 90, 2),
    "location": "View 3D > Properties Panel",
    "support": "COMMUNITY",
    "category": "Mesh"
}


class LyricsProperties(bpy.types.PropertyGroup):
    lyricsfile: StringProperty(
        name="lyricsfile", description="Text file with the lyrics script")
    mainmusicfile: StringProperty(
        name="mainmusicfile", description="Wave file with the music")
    wavkick: StringProperty(
        name="wavkick", description="Wave file with the kick only")
    wavbass: StringProperty(
        name="wavbass", description="Wave file with the kick only")
    wavinstru1: StringProperty(
        name="wavinstru1", description="Wave file with the kick only")
    wavinstru2: StringProperty(
        name="wavinstru2", description="Wave file with the kick only")
    wavvocals: StringProperty(
        name="wavvocals", description="Wave file with the kick only")


classes = (LyricsVideoAddOn_OT,
           LyricsVideoAddOn_PT_main_panel,
           SelectLyricsFile_OT,
           SelectMainWav_OT,
           LyricsVideoAddOn_InsertWaves,
           LyricsProperties)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.lyricsprops = bpy.props.PointerProperty(
        type=LyricsProperties)

    bpy.app.handlers.frame_change_pre.append(LyricsFrameHandler)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.lyricsprops
    bpy.app.handlers.frame_change_pre.remove(LyricsFrameHandler)


if __name__ == "__main__":
    register()
