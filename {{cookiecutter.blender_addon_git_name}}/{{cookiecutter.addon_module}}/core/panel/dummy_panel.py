import bpy

from {{cookiecutter.addon_module}}.core.operator.dummy_operator import DummyOperator

class DummyPanel(bpy.types.Panel):

    bl_idname = "SCENE_PT_Dummy_pannel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dummy"
    bl_label = "Dummy Panel"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(DummyOperator.bl_idname)