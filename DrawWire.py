import bpy

bl_info = {
    "name": "Show Wire",
    "category": "Object > Special > Show Wire",
}


# Toggle displaying wire
# It's inside of the special menu in object mode
# previously it was q but I changed it
# The structure is not difficult at all
class ShowWire(bpy.types.Operator):
    """Show Wire"""                     # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.showwire"       # unique identifier for buttons and menu items to reference.
    bl_label = "Show Wire"              # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}   # enable undo for the operator.

    # You need this class method sentence for class methods
    @classmethod
    # what's cls?
    # anyway, with this, you can disable the menu
    def poll(cls, context):
        return bool(bpy.context.selected_objects)

    def execute(self, context):  # execute() is called by blender when running the operator.
        if bpy.context.object.show_wire == False:
            bpy.context.object.show_wire = True
            bpy.context.object.show_all_edges = True
        else:
            bpy.context.object.show_wire = False
            bpy.context.object.show_all_edges = False

        return {'FINISHED'}  # this lets blender know the operator finished successfully.


# for menu to draw
# You can change this to Lambda
def menu_draw(self, context):
    self.layout.operator("object.showwire")


# registering class and menu
def register():
    bpy.utils.register_class(ShowWire)
    bpy.types.VIEW3D_MT_object_specials.append(menu_draw)


# Unregistering class and menu
def unregister():
    bpy.utils.unregister_class(ShowWire)
    bpy.types.VIEW3D_MT_object_specials.remove(menu_draw)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
