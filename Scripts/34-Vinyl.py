# MenuTitle: 34. Vinyl
# -*- coding: utf-8 -*-
__doc__ = """
34. Vinyl
"""

import GlyphsApp
from NaNGFGraphikshared import *
from NaNGFAngularizzle import *
from NaNGFSpacePartition import *

from NaNFilter import NaNFilter


class Vinyl(NaNFilter):

    params = {
        "S": {"offset": 10, "it": 5, "depthmin": 20, "depthmax": 65},
        "M": {"offset": 10, "it": 5, "depthmin": 25, "depthmax": 75},
        "L": {"offset": 10, "it": 5, "depthmin": 30, "depthmax": 85}
    }
    glyph_stroke_width = 16
    shadow_stroke_width = 6
    angle = -160 #random.randrange(0, 360)

    def setup(self):
        pass

    def processLayer(self, thislayer, params):

        offset, it, depthmin, depthmax = params["offset"], params["it"], params["depthmin"], params["depthmax"]

        thislayer.removeOverlap()
        pathlist = doAngularizzle(thislayer.paths, 10)
        outlinedata = getGlyphCoords(pathlist)
        bounds = AllPathBounds(thislayer)

        offsetpaths = self.saveOffsetPaths(
            thislayer, offset, offset, removeOverlap=True
        )
        pathlist2 = doAngularizzle(offsetpaths, 4)
        outlinedata2 = getGlyphCoords(pathlist2)

        ClearPaths(thislayer)

        shadowpaths = []
        for n in range(0, it):
            depth = random.randrange(depthmin, depthmax)
            angle = random.randrange(0, 360)
            shadowpaths.extend( DoShadow(thislayer, outlinedata, angle, depth, "paths") )
            AddAllPathsToLayer(shadowpaths, thislayer)
        
        thislayer.removeOverlap()

        roundpaths = RoundPaths(thislayer.paths, "nodes")
        blobs = []
        for p in roundpaths: blobs.append ( convertToFitpath(p, True) )

        ClearPaths(thislayer)

        AddAllPathsToLayer(blobs, thislayer)
       
        thislayer.removeOverlap()


Vinyl()
