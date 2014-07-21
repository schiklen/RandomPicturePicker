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
        self.annotationType = ["Yes", "No", "Ignore"]
        self.pictureList = []
        self.usedList = []
        self.currentImp = None
        self.currentPicture = None

    # Methods for communication between initDialog and picturePicker
    def showInitDialog(self):
        initDialog(self)
    
    def setInputPathDict(self, inputPathDict):
        self.inputPathDict = inputPathDict
        
    def setOutputPath(self, outputPath):
        self.outputPath = outputPath
    
    def setAnnotationType(self, annotationType):
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
    
    def nextPicture(self):
        if self.currentPicture != None: # if its not the first picture to open.
            # TODO: check for annotation
            # if self.currentPicture.getAnnotation != None:
            self.usedList.append(self.currentPicture)
            self.currentImp.close()
        
        # update pictureList
        freshList = [i for i in self.pictureList if i not in self.usedList]        
        if len(freshList) > 0: # if self.currentPicture not in self.usedList
            self.currentPicture = random.choice(freshList)
            self.currentImp = self.currentPicture.getImp()
            self.currentImp.show()

    def prevPicture(self, event):
        if len(self.usedList) >= 1:
            self.currentImp.close()
            if self.currentPicture not in self.usedList:
                i = len(self.usedList)
            else:
                i = self.usedList.index(self.currentPicture)
            self.currentPicture = self.usedList[i-1]
            self.currentImp = self.currentPicture.getImp()
            self.currentImp.show()
            
    def exit(self):
        exit(0)

        
# main
p = picturePicker()
p.showInitDialog()

p.createPictureList()
p.startGUI()
