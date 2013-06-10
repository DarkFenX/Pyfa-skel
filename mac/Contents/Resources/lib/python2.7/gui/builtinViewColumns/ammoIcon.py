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

from gui import builtinViewColumns
from gui.viewColumn import ViewColumn
from gui import bitmapLoader
import wx
from eos.types import Module

class AmmoIcon(ViewColumn):
    name = "Ammo Icon"
    def __init__(self, fittingView, params):
        ViewColumn.__init__(self, fittingView)
        self.size = 16
        self.maxsize = self.size
        self.mask = wx.LIST_MASK_IMAGE
        self.columnText = ""

    def getText(self, mod):
        return ""

    def getImageId(self, stuff):
        if not isinstance(stuff, Module):
            return -1

        if stuff.charge is None:
            return -1
        else:
            iconFile = stuff.charge.icon.iconFile if stuff.item.icon else ""
            if iconFile:
                bitmap = bitmapLoader.getBitmap(iconFile, "pack")
                if bitmap is None:
                    return -1
                else:
                    return self.fittingView.imageList.Add(bitmap)
            else:
                return -1

AmmoIcon.register()
