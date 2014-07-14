'''
Created on Jun 4, 2014

@author: schiklen
'''
from InitDialog import initDialog

#module random picture picker


# an ImageJ/Fiji plugin that lets you annotate bildly
# different sets of images, e. g. treated / untreated
# @author: Christoph Schiklenk, christoph.schiklenk@embl.de

# --- imports ---

# --- custom imports ---
from sys import path
from java.lang.System import getProperty


import os
import pickle
import random
from javax.swing import JFrame, JPanel, JButton, JList, JProgressBar, JTextField, BorderFactory
from java.awt import LayoutManager, GridLayout

#globals
IMAGETYPES = [".tif", ".tiff", ".jpeg", ".jpg", ".png", ".dv", ".lsm"]

def isImage(s):
    if os.path.splitext(s)[1] in IMAGETYPES:
        return True
    else:
        return False
    
#classes

class gui:
    "Work graphical user interface for Random Picture Picker"
    def __init__(self):
        self.imgList = imgList()
        self.imp = None
        self.outpath = os.path.join(DirectoryChooser("Please chose save directory").getDirectory(), "results.csv")
        
        self.frame = JFrame("Random Picture Picker", size=(300, 200))
        mainPane = JPanel(GridLayout(3,1))
        self.frame.add(mainPane)

        annotationPane = JPanel()  # contains all annotation stuff
        mainPane.add(annotationPane)

        self.annotationField = JTextField(15)
        annotationPane.add(self.annotationField) #

        controlsPane = JPanel(GridLayout(4,1, 4, 4))  # contains buttons 'next', 'previous', 'quit'
        mainPane.add(controlsPane)
        addFolderButton = JButton("Add Folder...", actionPerformed=self.addFolder)
        controlsPane.add(addFolderButton)
        nextImgButton = JButton("Next Image >", actionPerformed=self.showNextImage)
        controlsPane.add(nextImgButton)
        prevImgButton = JButton("< Prev Image", actionPerformed=self.showPrevImage)
        controlsPane.add(prevImgButton)        
        prevImgButton = JButton("Quit script", actionPerformed=self.exit)
        controlsPane.add(prevImgButton)
        
        statusPane = JPanel()   # contains status information: progress bar
        mainPane.add(statusPane)
        
        self.progressBar = JProgressBar()
        self.progressBar.setStringPainted(True)
        self.progressBar.setValue(0)
        statusPane.add(self.progressBar)
        
        self.frame.pack
        self.frame.setVisible(True)

    def addFolder(self, event):
        "Adding all images in one folder to the list of unprocessed pictures"
        d = DirectoryChooser("Please chose directory 1").getDirectory()
        self.imgList.addFolder(d)
        self.progressBar.setMaximum(len(self.imgList.getAll()))
        self.progressBar.setValue(len(self.imgList.getProcessed()))

    def showNextImage(self, event):
        # open new random picture
        i = self.imgList.getRandomImg()
        if i != None:
            self.showImg(i)
        else:
            IJ.log("All images looked at")
        a = self.annotationField.getText()
        self.out = open(self.outpath, 'a')
        self.out.write(i + "," + a + "\n")
        self.close()

    def showPrevImage(self, event):
        self.showImg(self.imgList.getPrevImg())

    def showImg(self, imagePath):
        if os.path.exists(imagePath):
            # close old imp, if open
            try:
                self.imp.close()
            except AttributeError:
                pass
            self.imp = ImagePlus(imagePath)
            self.imp.setTitle("- - -")
            self.imp.show()
            self.progressBar.setValue(len(self.imgList.getProcessed()))
        else:
           print "Image file not found"

    def exit(self, event):
        try:
            self.imp.close()
        finally:
            WindowManager.removeWindow(self.frame)
            self.frame.dispose()
            self.out.close()


class imgList:
    "A class to manage imges shown and images still to show"
    def __init__(self):
       self.fresh = []
       self.used = []

    def addFolder(self, dirPath):
        # add all imgFiles in this folder but exclude duplicates
        self.fresh = self.fresh + [e for e in folder(dirPath).getImageList() if e not in (self.fresh + self.used)]
        print len(self.fresh)

    def getRandomImg(self):
        if len(self.fresh) > 0:
            r = random.choice(self.fresh)
            self.fresh.remove(r)
            self.used.append(r)
            return r
        else:
            return None

    def getPrevImg(self):
        p = self.used.pop()
        self.fresh.append(p)
        return p

    def getAll(self):
        return self.fresh + self.used

    def getProcessed(self):
        return self.used

    def getUnprocessed(self):
        return self.fresh


class folder:
    def __init__(self, dirPath):
        self.dirPath = dirPath
        print self.dirPath
        self.fileList = os.listdir(dirPath)
        self.imageList = [os.path.join(self.dirPath, f) for f in self.fileList if isImage(f) == True]

    def getFileList(self):
        return self.fileList

    def getImageList(self):
        return self.imageList

#- main -

#TODO: pre-interface: What options (e. g. plasma membrane / nucleus/ no signal)? default yes/no, numbers,...

#TODO: sort pictures
