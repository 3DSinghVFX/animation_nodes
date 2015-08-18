import bpy
from ... base_types.node import AnimationNode

class PolygonInfo(bpy.types.Node, AnimationNode):
    bl_idname = "an_PolygonInfo"
    bl_label = "Polygon Info"

    def create(self):
        self.inputs.new("an_PolygonSocket", "Polygon", "polygon")
        self.outputs.new("an_VectorSocket", "Center", "center")
        self.outputs.new("an_VectorSocket", "Normal", "normal")
        self.outputs.new("an_VectorSocket", "Material Index", "materialIndex")
        self.outputs.new("an_FloatSocket", "Area", "area")
        self.outputs.new("an_VertexListSocket", "Vertices", "vertices")

    def execute(self, polygon):
        return polygon.center, polygon.normal, polygon.materialIndex, polygon.area, polygon.vertices
