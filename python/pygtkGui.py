#!/usr/bin/env python
"""Module containing the PyGtk implementation for the GUI tutorial.

COMMENTS:
=========
+ Easy widget creation; widget hierarchy based on box packing
+ Easy to use frames, with or without 'labels' (use tricks with
  SHADOW type to change 'etched' border)
+ GdkImLib missing from WIN32? Loading image files is implemented
  using GdkImLib, but couldn't find the Python WIN32 bindings. Anyone?

IDIOMS:
=======
+ Create widgets without parents and use GtkHBox() and GtkVBox()
  to 'pack' child widgets
+ Resizing policy is achieved using the 'expand' and 'fill' options
  to the 'pack' routines. 'expand' affects resize policy in box's
  direction; 'fill' affects resizing in box's other dimension
+ Size of widgets are determined top-down the widget hierarchy (most
  other GUIs use size hints from the bottom child widgets and go up)
+ Use 'show_all()' on top level widgets to display that level's hierarchy
+ 'Double-click' detected by checking the type of 'clicked' event, not by
  connecting a separate double-click event signal
+ Don't forget to connect "destroy" to your top level GtkWindow
"""

import os

from oogui import OOGui
import oogui

from gtk import *
import GDK  # for some lower-level event types, including double-click


def _getLabeledList(label='', command=None, etchedBorder=0):
    """Utility function to return a labeled frame and scrollable list"""
    frame = GtkFrame(label)
    list = ScrollableList(command)
    frame.add(list.getScrollable())
    if not etchedBorder:
        frame.set_shadow_type(SHADOW_NONE)

    return frame, list


class PyGtkGui(OOGui):
    """Specialization of OOGui that uses the PyGtk widget set"""
    def __init__(self, argv, geometry=None, resfile=None, startdir=None):
        """Create the PyGtk and OOGui base objects"""
        self._cwdFrame     = None
        self._cwd          = None
        self._selectedRow  = -1

        # create top level window and handle window close
        topLevel = GtkWindow()
        topLevel.connect("destroy", self._exit)

        # call our parent class ctor which builds the GUI
        OOGui.__init__(self, topLevel, geometry, resfile, startdir)


    # -------------------------------------------------------------------
    # polymorphic implementations
    # -------------------------------------------------------------------

    def _buildGui(self, title):
        """Override parent's abstract 'hook' method called in ctor"""
        vbox = GtkVBox()
        # build the working directory frame
        vbox.add(self._buildCWD(), expand=FALSE)
        
        # build the paned widget that contains the lists and display
        vbox.add(self._buildPanes(), padding=oogui.BORDER)

        self._topLevel.add(vbox)
        self._topLevel.set_title(title)

        
    def _loadResources(self, resfile=None):
        """Load the resources (options) for all the 'named' widgets"""
        # FIXME
        #if resfile:
        #    self._topLevel.option_readfile(resfile)
        return 1

    def _setFilename(self, filename):
        """Sets the filename entry field when a file is selected; called
        by base class's _fileSelected() method
        """
        self._filename.set_text(filename)
        

    def _startGui(self, geometry=None):
        """Runs the application in the main event loop"""
        # set the top level window placement and size if specified
        posx = 0
        posy = 0
        width = oogui.DISPLAY_WIDTH
        height = oogui.APP_HEIGHT
        if geometry:
            # FIXME ... parse geometry
            print 'fix geometry setting!'
        # self._topLevel.set_position(pos)
        self._topLevel.set_default_size(width, height)

        # start up the main event loop
        self._topLevel.show_all()
        mainloop()


    def _getCurrentDirectory(self):
        """Returns the name of the current working directory"""
        return self._cwd

        
    def _getSelectedDirectory(self):
        """Returns currently 'selected' directory name"""
        return self._dirList.get_text(self._selectedRow, 0)
    

    def _getSelectedFile(self):
        """Returns currently 'selected' file name"""
        if self._selectedFile:
            return self._selectedFile
        return self._fileList.get_text(self._selectedRow, 0)
    

    def _getTopLevel(self):
        """Special access method used by base to ensure top level is created"""
        return self._topLevel

        
    def _displayBinary(self, filename):
        """Displays binary files in the way it thinks it should."""
        self._display.binary(filename)


    def _displayHTML(self, filename):
        """Implemented behavior for displaying HTML files"""
        self._display.html(filename)


    def _displayImage(self, filename):
        """Implemented behavior for displaying image files"""
        self._display.image(filename)


    def _displayText(self, filename):
        """Implemented behavior for displaying text (other) files"""
        self._display.text(filename)


    # -------------------------------------------------------------------
    # private class methods 
    # -------------------------------------------------------------------

    def _buildCWD(self):
        """Private method to construct the working directory frame"""
        # the GtkFrame has an optional label, so use it for current working dir
        self._cwdFrame = GtkFrame(label=os.getcwd())
        self._cwdFrame.set_border_width(oogui.BORDER)

        # add a button to allow the user to 'GoTo' a specified directory
        gotoButton = GtkButton("GoTo")
        gotoButton.connect("clicked", self._setDirectory)
        
        self._gotoEntry = GtkEntry()
        self._gotoEntry.connect("activate", self._setDirectory)

        hbox = GtkHBox()
        hbox.pack_start(gotoButton, expand=FALSE, fill=FALSE, padding=oogui.BORDER)
        hbox.pack_end(self._gotoEntry, padding=oogui.BORDER)

        self._cwdFrame.add(hbox)

        return self._cwdFrame


    def _buildPanes(self):
        """Build a PanedWidget with panes for lists and display views"""
        panedW = GtkVPaned()

        # place the lists in the 'list' pane
        panedW.pack1(self._buildLists())

        # place the display in the 'disp' pane
        self._display = DisplayFrame()
        panedW.pack2(self._display)

        panedW.set_position(oogui.SASH_POSITION)

        return panedW
        

    def _buildLists(self):
        """Create the frame that contains list of files and text entry"""
        # create the directories and files list frames
        dirFrame, self._dirList   = _getLabeledList(oogui.DIRS_LABEL,
                                                    self._listSelected)
        fileFrame, self._fileList = _getLabeledList(oogui.FILES_LABEL,
                                                    self._listSelected)
        
        # construct the lists side by side
        listsBox = GtkHBox()
        listsBox.pack_start(dirFrame, padding=oogui.BORDER)
        listsBox.pack_end( fileFrame, padding=oogui.BORDER)

        # create a variable to use for filename entry
        self._filename = GtkEntry()
        self._filename.connect("activate", self._setFile)
        filenameFrame = GtkFrame(oogui.FILENAME_LABEL)
        filenameFrame.add(self._filename)
        filenameFrame.set_shadow_type(SHADOW_NONE)
        filenameFrame.set_border_width(oogui.BORDER)

        # put the lists and filename entry frames together        
        vbox = GtkVBox()
        vbox.pack_start(listsBox)
        vbox.pack_end(filenameFrame, expand=FALSE)

        return vbox

    def _setCWD(self, cwd):
        """Updates the GUI by setting the current working directory to 'cwd'"""
        if not cwd or not os.path.isdir(cwd):
            return
        self._cwdFrame.set_label(cwd)
        self._cwd = cwd
        self._setEntries()


    def _setDirectory(self, *unused):
        """Event callback for GoTo button and text entry to set the
        current working directory.
        """
        self._setCWD(self._gotoEntry.get_text())


    def _setFile(self, *unused):
        """Event callback for filename text entry to specify full pathname
        of file to display.
        """
        self._selectedFile = self._filename.get_text()
        self._fileSelected()
        self._selectedFile = None


    def _setEntries(self):
        """Sets the names of files and directories in the lists for the
        'current selected directory'
        """
        cwd = self._cwd
        if not cwd:
            cwd = os.getcwd()
            self._cwd = cwd

        self._gotoEntry.set_text(cwd)

        # populate the list boxes with their respective entries
        self._dirList.clear()
        self._fileList.clear()
        dirs, files = self._getEntries(cwd)
        # build list of items and append to list boxes
        [self._dirList.append([d]) for d in dirs]
        [self._fileList.append([f]) for f in files]


    def _listSelected(self, clist, row, unused, event):
        """Idiom for list selection is to check the event callback values
        to detect double-click. Use this common method, determine which
        list was selected, and if double-clicked, call appropriate action
        """
        # only handle double-clicks on the list
        if event.type != GDK._2BUTTON_PRESS:
            return
        
        self._selectedRow = row
        if clist == self._fileList:
            self._fileSelected()
        elif clist == self._dirList:
            self._directorySelected()


    def _exit(self, *unused):
        """Clean up application window upon exit"""
        self._topLevel.hide()
        self._topLevel.destroy()
        mainquit()


# -----------------------------------------------------------------------
# Specialized scrolled frame that displays text and image files
# -----------------------------------------------------------------------

# Could not find the WIN32 Python bindings for GdkImLib ... anyone?
_imageLoadOk = 1
try:
    import GdkImlib
except ImportError:
    _imageLoadOk = 0
    
class DisplayFrame(GtkFrame):
    """Specialized scrolled frame that displays text and image files"""
    def __init__(self):
        """Create the display frame that will display the selected file"""
        GtkFrame.__init__(self)
        self._sw = None   # rebuilt each time show() is called
        self.set_label('Ready')
        self.set_border_width = oogui.BORDER

    def binary(self, filename):
        """Resets/Clears the scrolled text and displays unavailable format"""
        self._show(None)


    def html(self, filename):
        """Displays the file with HTML fonts/formatting"""
        #FIXME: use GtkHtml????
        self.text(filename)


    def image(self, filename):
        """Displays the image contained in filename"""
        self._show(filename)
        if not _imageLoadOk:
            self.text(filename,
                      'Unable to load image file with GdkImLib in WIN32')
            return
        image = GdkImlib.Image(filename=filename)
        image.render()
        self._sw.add_with_viewport(image.make_pixmap())
        self._sw.show_all()


    def text(self, filename, altText=None):
        """Displays the text of the selected file"""
        self._show(filename)
        if altText:
            fileText = altText
        else:
            fileText, isBinary = oogui._getText(filename)
            if isBinary:
                self.binary(filename)
                return
        textWin = GtkText()
        textWin.set_editable(FALSE)
        textWin.insert(None, None, None, fileText)
        self._sw.add(textWin)
        self._sw.show_all()


    def _show(self, filename=None):
        """Manages the general scrolled window container and file label"""
        if self._sw:
            self.remove(self._sw)

        if not filename:
            filename = oogui.DISPLAY_UNAVAIL
        labelText = oogui.DISPLAY_LABEL + filename
        self.set_label(labelText)

        self._sw = GtkScrolledWindow()
        self.add(self._sw)


# -----------------------------------------------------------------------
# "Decorated" GtkCList that scrolls automatically
# -----------------------------------------------------------------------

# NOTE: GtkList is superceded by GtkCList, so use it instead.
class ScrollableList(GtkCList):
    def __init__(self, callback=None):
        """Creates a scrollable listbox with default resizing behavior"""
        GtkCList.__init__(self)
        self._sw = GtkScrolledWindow()
        self._sw.set_policy(POLICY_AUTOMATIC, POLICY_AUTOMATIC)
        # set_usize is deprecated in the doc, but the recommended
        # replacement methods: set_size_request(width, height) and
        # set_default_size(width, height) aren't available for the
        # GtkScrolledWindow ??
        self._sw.set_usize(oogui.DISPLAY_WIDTH/2, oogui.DISPLAY_HEIGHT/4)
        self._sw.add(self)
        
        if callback:
            self.setCommand(callback)

    def getScrollable(self):
        """List is composed within the scrolled window, and the container
        is what will be managed within the widget hierarchy.
        """
        return self._sw

    def setCommand(self, callback):
        """Connect the list to the specified callback function"""
        self.connect("select-row", callback)
    

