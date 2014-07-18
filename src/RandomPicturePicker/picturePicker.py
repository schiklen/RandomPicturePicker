'''
Created on Jun 9, 2014

@author: schiklen
'''
from initDialog import initDialog
from os import listdir, path
import random
from picture import picture
from rppGui import Gui
#from ij import ImagePlus

IMAGE_FORMATS = [".tiff", ".tif", ".jpg", ".lsm"]

class picturePicker(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.inputPathDict = None
        self.outputPath = None
        self.annotationType = None
        self.pictureList = []
        self.usedList = []
        self.currentImp = None

    # Methods for communication between initDialog and picturePicker
    def showInitDialog(self):
        initDialog(self)
    
    def setInputPathDict(self, inputPathDict):
        self.inputPathDict = inputPathDict
        
    def setOutputPath(self, outputPath):
        self.outputPath = outputPath
    
    def setAnnotationType(self, annotationType):
        print "set anno type to", annotationType
        self.annotationType = annotationType
        
    def getAnnotationType(self):
        return self.annotationType
    
    # Methods for processing
    def createPictureList(self):
        for folder in self.inputPathDict.keys():
            for fileName in listdir(folder):
                if path.splitext(fileName)[1] in IMAGE_FORMATS:
                    self.pictureList.append(picture(folder, fileName, self.inputPathDict[folder]))
        print self.pictureList
    
    def startGUI(self):
        # startGUI
        gFr = Gui(self)
        #self.createPictureList()
            
            #This statement ONLY after successful annotation!
            #self.pictureList.remove(pic)
    
    def nextPicture(self, event):
        if self.currentImp != None:
            self.currentImp.close()
        
        if len(self.pictureList) > 0:
            rImage = random.choice(self.pictureList)
            print rImage.getImagePath()
            self.currentImp = rImage.getImp()
            self.currentImp.show()
            
    def prevPicture(self, event):
        print "previous pic"
            
    def exit(self):
        exit(0)

        
# main
p = picturePicker()
p.showInitDialog()

p.createPictureList()
p.startGUI()
