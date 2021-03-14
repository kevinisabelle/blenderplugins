# Blender imports
import bpy.types
from .bll.lyricsprocessor import LyricsScriptReader


class LyricsVideoAddOn_OT(bpy.types.Operator):
    """Operator for my first addon..."""

    bl_idname = "lyricsvideoaddon"
    bl_label = "Processes the lyrics for each frames according to the script."
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        object = context.object
        reader = LyricsScriptReader()
        reader.process_lyrics("1000|lyrics text goes here")

        # Your code goes here...
        print('Operator called!')

        return {'FINISHED'}
