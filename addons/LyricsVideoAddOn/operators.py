# Blender imports
import bpy.types
from .bll.lyricsprocessor import LyricsScriptReader
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
import os


class OpenFilebrowser_OT(Operator, ImportHelper):
    """Select the lyrics file"""
    bl_idname = "lyricsvideoaddon.open_filebrowser"
    bl_label = "Select file"

    def execute(self, context):
        """Do something with the selected file(s)."""

        filename, extension = os.path.splitext(self.filepath)

        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)

        return {'FINISHED'}


class LyricsVideoAddOn_OT(bpy.types.Operator):
    """Updates the lyric animation"""

    bl_idname = "lyricsvideoaddon.process"
    bl_label = "Processes the lyrics for each frames according to the script."
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        object = context.object
        reader = LyricsScriptReader()
        reader.process_lyrics("1000|lyrics text goes here")

        print('Operator called!')

        return {'FINISHED'}
