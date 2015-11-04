#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import wx
import bitmapLoader

class CachingImageList(wx.ImageList):
    def __init__(self, width, height):
        wx.ImageList.__init__(self, width, height)
        self.map = {}

    def Add(self, *loaderArgs):
        key = "".join(loaderArgs)
        if key not in self.map:
            bitmap = bitmapLoader.getBitmap(*loaderArgs)
            if bitmap is None:
                return -1
            id = wx.ImageList.Add(self,bitmap)
            self.map[key] = id
        else:
            id = self.map[key]

        return id
