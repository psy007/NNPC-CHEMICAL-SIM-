#!/usr/bin/env python
"""PyCrustApp is a python shell and namespace browser application."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: PyCrustApp.py,v 1.2 2002/08/31 05:10:24 raul Exp $"
__revision__ = "$Revision: 1.2 $"[11:-2]

from wxPython.wx import *
from PyCrust.crust import CrustFrame


class App(wxApp):
    """PyCrust standalone application."""
    
    def OnInit(self):
        wxInitAllImageHandlers()
        locals = {'__app__': 'PyCrust Standalone Application'}
        self.crustFrame = CrustFrame(locals=locals)
        self.crustFrame.SetSize((750, 525))
        self.crustFrame.Show(true)
        self.SetTopWindow(self.crustFrame)
        # Add the application object to the sys module's namespace.
        # This allows a shell user to do:
        # >>> import sys
        # >>> sys.application.whatever
        import sys
        sys.application = self
        return true


def main():
    application = App(0)
    application.MainLoop()

if __name__ == '__main__':
    main()

 
