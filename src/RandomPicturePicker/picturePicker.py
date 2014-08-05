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
    
    def startGUI(self):
        self.gui = Gui(self)
    
    def loadPicture(self, picture):
        # try to close old imp here.
        self.currentPicture = picture
        self.currentImp = self.currentPicture.getImp()
        self.currentImp.show()
        if self.currentPicture.getAnnotation() != None:
            self.gui.setAnnotationField(picture.getAnnotation())
            
    def nextPicture(self):
        freshList = [i for i in self.pictureList if i not in self.usedList]
        
        if self.currentPicture in self.usedList:
            self.currentImp.close() # close the old picture
            
            if self.usedList.index(self.currentPicture) == len(self.usedList)-1: # if its the last picture in usedlist
                #print "Last pic in usedlist"
                if len(freshList) > 0: # if its not the last picture overall
                    self.loadPicture(random.choice(freshList))
            else:
                #print "going one fw in list"
                self.loadPicture(self.usedList[self.usedList.index(self.currentPicture)+1])
                
        elif self.currentPicture == None: # if its the first picture
            if len(freshList) > 0: # if its not the last picture
                self.loadPicture(random.choice(freshList))
        if self.currentPicture not in self.usedList:
            self.usedList.append(self.currentPicture)        

    def prevPicture(self, event):
        if len(self.usedList) >= 1:
            self.currentImp.close()
            #if self.currentPicture not in self.usedList:
            #    i = len(self.usedList)
            #else:
            #    i = self.usedList.index(self.currentPicture)
            i = self.usedList.index(self.currentPicture)
            if i > 0:
                self.loadPicture(self.usedList[i-1])

            
    def getCurrentPicture(self):
        return self.currentPicture    
    
    def exit(self):
        exit(0)

        
# main
p = picturePicker()
p.showInitDialog()

p.createPictureList()
p.startGUI()
