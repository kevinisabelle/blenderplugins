# Blender imports
import bpy.types


class MYFIRSTADDON_OT_test(bpy.types.Operator):
    """Operator for my first addon..."""

    bl_idname = "myfirstaddon.test"
    bl_label = "This operator does some fancy things..."
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        object = context.object

        # Your code goes here...
        print('Operator called!')

        return {'FINISHED'}
