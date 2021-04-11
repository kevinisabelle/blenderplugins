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
        context.scene.lyricsprops.lyricsfile = self.filepath
        return {'FINISHED'}


class SelectMainWav_OT(Operator, ImportHelper):
    """Select the lyrics file"""
    bl_idname = "lyricsvideoaddon.select_mainmusicfile"
    bl_label = "File"

    def execute(self, context):
        context.scene.lyricsprops.mainmusicfile = self.filepath
        return {'FINISHED'}


class LyricsVideoAddOn_InsertWaves(bpy.types.Operator):
    """Updates the waves curves"""
    bl_idname = "lyricsvideoaddon.insertwaves"
    bl_label = "Insert Waves Curves"
    bl_options = {'REGISTER'}

    def execute(self, context):
        if (not hasattr(bpy.context.scene.sequence_editor.sequences_all, "mainmusicfile")):

            # bpy.ops.sequencer.sound_strip_add(
            # filepath="K:\\Google Drive\\KIsabel\\Content\\Released\\Music\\2021-01-Soltera\\Soltera_72.wav",
            # directory="K:\\Google Drive\\KIsabel\\Content\\Released\\Music\\2021-01-Soltera\\",
            # files=[{"name":"Soltera_72.wav", "name":"Soltera_72.wav"}], frame_start=1, channel=1)

            dirname = os.path.dirname(context.scene.lyricsprops.mainmusicfile)
            mainmusicfile = context.scene.lyricsprops.mainmusicfile
            context.area.ui_type = 'SEQUENCE_EDITOR'

            bpy.ops.sequencer.sound_strip_add(filepath=mainmusicfile, directory=dirname,
                                              files=[{"name": "mainmusicfile", "name": "mainmusicfile"}], frame_start=1, channel=1)

            context.area.ui_type = 'VIEW_3D'

            return {'FINISHED'}


class LyricsVideoAddOn_OT(bpy.types.Operator):
    """Updates the lyric animation"""

    bl_idname = "lyricsvideoaddon.process"
    bl_label = "Processes the lyrics for each frames according to the script."
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        object = context.object
        lyricsprops = scene.lyricsprops

        print('Processing: ' + lyricsprops.lyricsfile)

        reader.process_lyrics(lyricsprops.lyricsfile)

        print('Processed lyrics')

        return {'FINISHED'}
