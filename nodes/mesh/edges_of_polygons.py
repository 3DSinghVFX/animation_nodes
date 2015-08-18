import bpy
from ... base_types.node import AnimationNode

class an_EdgesOfPolygons(bpy.types.Node, AnimationNode):
    bl_idname = "an_EdgesOfPolygons"
    bl_label = "Edges of Polygons"

    def create(self):
        self.inputs.new("an_PolygonIndicesListSocket", "Polygons", "polygons")
        self.outputs.new("an_EdgeIndicesListSocket", "Edges", "edges")

    def execute(self, polygons):
        edges = []
        for polygon in polygons:
            for i, index in enumerate(polygon):
                startIndex = polygon[i - 1]
                edge = (startIndex, index) if index > startIndex else (index, startIndex)
                edges.append(edge)
        return list(set(edges))
