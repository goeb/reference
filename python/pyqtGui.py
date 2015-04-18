"""Module containing the PyQt implementation for the GUI tutorial

COMMENTS:
=========
+ More complex widget creation; create a layout for parent widget,
  adding child widgets, but only if parent widget doesn't already have
  a layout (e.g., QHGroupBox)
+ 'Type-safe' signals/slots architecture not really taken advantage
  of in Python (maybe a new feature for pychecker? :)
+ Would be nice if QString's automagically converted to Python strings
+ Nice rich text widget, QTextView
+ Rich set of widgets overall: see QMainWindow for getting started
  (not used in the tutorial)
+ Easy image display (for simple image formats) using QPixmap and QLabel

IDIOMS:
=======
+ Create widgets with a parent and a label; add them to QHBoxLayout
  and QVBoxLayout via addWidget()
+ Resizing policy is achieved using the 'expand' flag on addWidget()
  PLUS the parent widget's sizing policy (either override sizePolicy() OR
  call 'setSizePolicy(QSizePolicy()) on parent widget directly)
+ QHBox and QVBox are widgets that auto-manage their children as they
  are created; use QHBoxLayout and QVBoxLayout as layout managers for parent
  widgets when more discrete layout manageement is required
+ Use 'show()' on top level widgets to display that level's hierarchy
"""

import os

import qt
SIGNAL = qt.SIGNAL
Qt     = qt.Qt

import oogui
OOGui  = oogui.OOGui


_ANCHOR = qt.QSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Expanding)

def _getLabeledFrame(w, label="", etchedBorder=0):
    """Utility function to create a labeled frame"""
    box = qt.QHGroupBox(w, label)
    box.setSizePolicy(_ANCHOR)
    box.setTitle(label)
    if not etchedBorder:
        box.setFrameShadow(qt.QFrame.Plain)
        box.setLineWidth(0)
        
    return box


def _getLabeledList(w, label="", commandSlot=None):
    """Utility function to create an expanding listbox in labeled frame"""
    # use the other utility function to create the labeled frame
    frame   = _getLabeledFrame(w, label)
    listbox = qt.QListBox(frame, label)

    # allow the listbox to expand in both directions
    listbox.setSizePolicy(_ANCHOR)
    
    # connect the "double-click" signal (event) to commandSlot
    if commandSlot:
        w.connect(listbox, SIGNAL("selected(int)"), commandSlot)
    
    return frame, listbox


class PyQtGui(qt.QApplication, OOGui):
    """Specialization of OOGui that uses the PyQt widget set"""
    def __init__(self, argv, geometry=None, resfile=None, startdir=None):
        """Create the PyQt QApplication and OOGui base objects"""
        self._cwdFrame     = None

        # create top level window and handle window close
        qt.QApplication.__init__(self, argv)
        topLevel = qt.QFrame()
        self.setMainWidget(topLevel)

        # call our parent class ctor which builds the GUI
        OOGui.__init__(self, topLevel, geometry, resfile, startdir)


    def sizePolicy(self):
        """Override default sizing policy and let both dimensions expand"""
        return _ANCHOR
        

    # -------------------------------------------------------------------
    # polymorphic implementations
    # -------------------------------------------------------------------

    def _buildGui(self, title):
        """Override parent's abstract 'hook' method called in ctor"""
        # set our top level sizing policy to expand in both directions
        self._topLevel.setSizePolicy(_ANCHOR)

        # create the main layout manager and tell toplevel to use it
        vbox = qt.QVBoxLayout(self._topLevel)
        vbox.setMargin(oogui.BORDER)   # border width
        vbox.setSpacing(oogui.BORDER)  # spacing between children

        # build the working directory frame
        vbox.addWidget(self._buildCWD(), 0)
        
        # build the paned widget that contains the lists and display
        vbox.addWidget(self._buildPanes(), 1)

        # set the title of main GUI window
        vbox.activate()
        self._topLevel.setCaption(title)

        
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
        self._filename.setText(filename)
        

    def _startGui(self, geometry=None):
        """Runs the application in the main event loop"""
        # set the top level window placement and size if specified
        if geometry:
            # FIXME ... parse geometry
            print 'fix geometry setting!'

        # start up the main event loop
        self._topLevel.show()
        self.exec_loop()


    def _getSelectedDirectory(self):
        """Returns currently selected directory name"""
        return str(self._dirList.text(self._dirList.currentItem()))
    

    def _getSelectedFile(self):
        """Returns currently selected file name"""
        if self._selectedFile:
            return self._selectedFile
        return str(self._fileList.text(self._fileList.currentItem()))
    

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
        # use group box label to display current working dir
        self._cwdFrame = _getLabeledFrame(self._topLevel, "", 1)

        # add a button to allow the user to 'GoTo' a specified directory
        gotoButton = qt.QPushButton(self._cwdFrame, "goto")
        gotoButton.setText("GoTo")
        self.connect(gotoButton, SIGNAL("clicked()"), self._setDirectory)
        
        self._gotoEntry = qt.QLineEdit(self._cwdFrame, "gotoEntry")
        self.connect(self._gotoEntry, SIGNAL("returnPressed()"),
                     self._setDirectory)

        return self._cwdFrame


    def _buildPanes(self):
        """Build a PanedWidget with panes for lists and display views"""
        panedW = qt.QSplitter(Qt.Vertical, self._topLevel, "panedW")
        panedW.setSizePolicy(_ANCHOR)
        panedW.setOpaqueResize(1) # repaint often when resizing
        
        # build and manage the lists pane
        self._buildLists(panedW)

        # build and manage the display pane
        self._display = DisplayFrame(panedW)

        # set sash position
        self._display.setMinimumSize(oogui.DISPLAY_WIDTH, oogui.SASH_MIN)

        return panedW
        

    def _buildLists(self, w):
        """Create the frame that contains list of files and text entry"""
        listsFrame = qt.QFrame(w, "listsFrame")
        listsFrame.setSizePolicy(_ANCHOR)

        # create the directories and files list frames
        dirFrame, self._dirList = _getLabeledList(listsFrame,
                                                 oogui.DIRS_LABEL,
                                                 self._directorySelected)
        fileFrame, self._fileList = _getLabeledList(listsFrame,
                                                   oogui.FILES_LABEL,
                                                   self._fileSelected)
        
        # construct the lists side by side
        listsBox = qt.QHBoxLayout()
        listsBox.setSpacing(oogui.BORDER)
        listsBox.addWidget(dirFrame, 1)
        listsBox.addWidget(fileFrame, 1)

        # create a variable to use for filename entry
        filenameFrame = _getLabeledFrame(listsFrame, oogui.FILENAME_LABEL)
        self._filename = qt.QLineEdit(filenameFrame, 'filenameEntry')
        self.connect(self._filename, SIGNAL("returnPressed()"), self._setFile)

        # put the lists and filename entry frames together
        vbox = qt.QVBoxLayout(listsFrame)
        vbox.setSpacing(oogui.BORDER)
        vbox.addLayout(listsBox, 1)
        vbox.addWidget(filenameFrame, 0)

        return listsFrame


    def _getCurrentDirectory(self):
        """Returns the full pathname of the current working directory"""
        return str(self._cwdFrame.title())
    
    def _setCWD(self, cwd):
        """Updates the GUI by setting the current working directory to cwd"""
        if not cwd or not os.path.isdir(cwd):
            return
        self._cwdFrame.setTitle(cwd)
        self._setEntries()


    def _setDirectory(self, *unused):
        """Slot for signal 'returnPressed' for entry text and for signal
        'clicked' for GoTo button so user can enter full pathname to
        specify a new working directory.
        """
        self._setCWD(str(self._gotoEntry.text()))


    def _setFile(self, *unused):
        """Slot for signal 'returnPressed' for entry text so user can enter
        full pathname for a file to be displayed.
        """
        self._selectedFile = str(self._filename.text())
        self._fileSelected()
        self._selectedFile = None


    def _setEntries(self):
        """Sets the names of files and directories in the lists for the
        'current selected directory'
        """
        cwd = self._getCurrentDirectory()
        if not cwd:
            cwd = os.getcwd()
            self._cwdFrame.setTitle(cwd)

        self._gotoEntry.setText(cwd)

        # populate the list boxes with their respective entries
        self._dirList.clear()
        self._fileList.clear()
        dirs, files = self._getEntries(cwd)
        self._dirList.insertStrList(dirs)
        self._fileList.insertStrList(files)


# -----------------------------------------------------------------------
# Specialized scrolled frame that displays text and image files
# -----------------------------------------------------------------------
class DisplayFrame(qt.QVGroupBox):
    """Specialized scrolled frame that displays text and image files"""
    def __init__(self, w):
        """Creates the labeled frame that will contain the displayed file"""
        qt.QVGroupBox.__init__(self, 'displayFrame', w)
        self._sw = None   # manages new scrolled child each time
        self.setTitle('Ready')


    def sizePolicy(self):
        """Override default sizing policy and let both dimensions expand"""
        return _ANCHOR


    def binary(self, unused):
        """Resets/Clears the scrolled text and displays unavailable format"""
        self._init(None)


    def html(self, filename):
        """Displays the file with HTML fonts/formatting"""
        self.text(filename)


    def image(self, filename):
        """Displays the image contained in filename"""
        self._init(filename)
        self._sw = qt.QScrollView(self, "scrollView")
        label = qt.QLabel(self)
        label.setPixmap(qt.QPixmap(filename))
        self._sw.addChild(label)
        self._sw.show()


    def text(self, filename):
        """Displays the text of the specified file"""
        self._init(filename)
        fileText, isBinary = oogui._getText(filename)
        if isBinary:
            self.binary(filename)
            return
        self._sw = qt.QTextView(self, 'textView')
        self._sw.setText(fileText)
        self._sw.show()


    def _init(self, filename=None):
        """Manages the contained scrolled widget for every file display"""
        if self._sw:
            self.removeChild(self._sw)
            self._sw = None
            
        if not filename:
            filename = oogui.DISPLAY_UNAVAIL
        labelText = oogui.DISPLAY_LABEL + filename
        self.setTitle(labelText)
