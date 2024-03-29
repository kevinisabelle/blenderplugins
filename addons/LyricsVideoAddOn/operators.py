# Blender imports
import os
import bpy.types
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.app.handlers import persistent

from .bll.lyricsprocessor import LyricsScriptReader

reader = LyricsScriptReader()
reader.process_lyrics()


@persistent
def LyricsFrameHandler(scene):
    textline = reader.getTextLine(reader.detect_index(scene.frame_current))
    print("Frame Change", textline)


class SelectLyricsFile_OT(Operator, ImportHelper):
    """Select the lyrics file"""
    bl_idname = "lyricsvideoaddon.select_lyricsfile"
    bl_label = ""

    def execute(self, context):
        context.window_manager.lyricsprops.lyricsfile = self.filepath
        return {'FINISHED'}


class SelectMainWav_OT(Operator, ImportHelper):
    """Select the lyrics file"""
    bl_idname = "lyricsvideoaddon.select_mainmusicfile"
    bl_label = "File"

    def execute(self, context):
        context.window_manager.lyricsprops.mainmusicfile = self.filepath
        return {'FINISHED'}


class LyricsVideoAddOn_InsertWaves(bpy.types.Operator):
    """Updates the waves curves"""
    bl_idname = "lyricsvideoaddon.insertwaves"
    bl_label = "Insert Waves"
    bl_options = {'REGISTER'}

    def execute(self, context):
        if (not hasattr(bpy.context.scene.sequence_editor.sequences_all, "mainmusicfile")):

            bpy.ops.sequencer.sound_strip_add(filepath=context.window_manager.lyricsprops.mainmusicfile, directory=context.window_manager.lyricsprops.mainmusicfile,
                                              files=[{"name": "mainmusicfile", "name": "mainmusicfile"}], relative_path=True, frame_start=1, channel=1)


class LyricsVideoAddOn_OT(bpy.types.Operator):
    """Updates the lyric animation"""

    bl_idname = "lyricsvideoaddon.process"
    bl_label = "Processes the lyrics for each frames according to the script."
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        object = context.object
        lyricsprops = bpy.types.WindowManager.lyricsprops

        print('Processing: ' + lyricsprops.lyricsfile)

        reader.process_lyrics(
            lyricsprops.lyricsfile)

        print('Processed lyrics')

        return {'FINISHED'}
