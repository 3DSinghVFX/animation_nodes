import bpy
from bpy.props import *
from ... base_types.node import AnimationNode

class CreatePolygonIndices(bpy.types.Node, AnimationNode):
    bl_idname = "an_CreatePolygonIndices"
    bl_label = "Create Polygon Indices"
    isDetermined = True

    errorMessage = StringProperty()

    def create(self):
        self.inputs.new("an_IntegerListSocket", "Indices", "indices")
        self.outputs.new("an_PolygonIndicesSocket", "Polygon Indices", "polygonIndices")

    def draw(self, layout):
        if self.errorMessage != "":
            layout.label(self.errorMessage, icon = "ERROR")

    def execute(self, indices):
        if len(indices) >= 3:
            self.errorMessage = ""
            return tuple(indices)
        else:
            self.errorMessage = "3 or more indices needed"
            return (0, 1, 2)
