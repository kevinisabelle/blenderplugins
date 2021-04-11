# Blender imports
import bpy.types
from .operators import reader
from bpy.props import FloatProperty, StringProperty


class LyricsVideoAddOn_PT_main_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Lyrics Video"
    bl_context = "objectmode"
    bl_category = "K Isabel"

    def draw(self, context):
        layout = self.layout

        layout.label(text="File selections")
        layout.separator()

        row = layout.row()
        row.prop(context.scene.lyricsprops, "lyricsfile", icon="FILE_TEXT")

        layout.separator()

        row = layout.row()
        row.prop(context.scene.lyricsprops,
                 "mainmusicfile", text="Main Music wav", icon="FILE_SOUND")

        row = layout.row()
        row.prop(context.scene.lyricsprops, "wavkick",
                 text="Kick wav", icon="FILE_SOUND")

        row = layout.row()
        row.prop(context.scene.lyricsprops, "wavbass",
                 text="Bass wav", icon="FILE_SOUND")

        row = layout.row()
        row.prop(context.scene.lyricsprops, "wavinstru1",
                 text="Instru 1 wav", icon="FILE_SOUND")

        row = layout.row()
        row.prop(context.scene.lyricsprops, "wavinstru2",
                 text="Instru 2 wav", icon="FILE_SOUND")

        row = layout.row()
        row.prop(context.scene.lyricsprops, "wavvocals",
                 text="Vocals wav", icon="FILE_SOUND")

        layout.separator()
        row = layout.row()
        row.operator("lyricsvideoaddon.process", text="Refresh Lyrics")

        row = layout.row()
        row.operator("lyricsvideoaddon.insertwaves", text="Refresh wave files")
