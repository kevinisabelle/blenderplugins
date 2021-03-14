# Blender imports
import bpy.types


class LyricsVideoAddOn_PT_main_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Lyrics Video"
    bl_context = "objectmode"
    bl_category = "K Isabel"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        layout.label(text="File selections")

        row.operator("lyricsvideoaddon.process", text="Refresh")
        row.operator("test.open_filebrowser", text="Open Panel")