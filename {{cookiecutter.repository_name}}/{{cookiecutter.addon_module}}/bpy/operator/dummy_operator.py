import bpy

class DummyOperator(bpy.types.Operator):

    bl_idname = "object.dummy_operator"
    bl_label = "Dummy Operator"

    def execute(self, context):
        self.report({"INFO"}, "Hello from Dummy Operator")
        return {"FINISHED"}