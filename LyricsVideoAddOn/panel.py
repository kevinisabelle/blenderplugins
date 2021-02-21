# Blender imports
import bpy.types


class MYFIRSTADDON_PT_main_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "My First Addon"
    bl_context = "objectmode"
    bl_category = "My First Addon"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("myfirstaddon.test", text="My operator")
