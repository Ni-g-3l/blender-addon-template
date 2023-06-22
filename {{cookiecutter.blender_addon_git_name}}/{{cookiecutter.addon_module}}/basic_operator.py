from typing import Set
import bpy
from bpy.types import Context

class HelloWorldOperator(bpy.types.Operator):

    bl_idname = "object.say_hello"
    bl_label = "Say Hello"

    def execute(self, context: Context) -> Set[str] | Set[int]:
        self.report({'INFO'}, "Hello from cookiecutter")
        return {"FINISHED"}

def add_to_object_menu(self, context):
    self.layout.operator(
        HelloWorldOperator.bl_idname, text=HelloWorldOperator.bl_label
    )

def register():
    bpy.types.VIEW3D_MT_object.append(add_to_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(add_to_object_menu)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(add_to_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(add_to_object_menu)
