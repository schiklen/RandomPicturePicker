'''
Created on Jun 9, 2014

@author: schiklen
'''
from initDialog import initDialog
from os import listdir
import random
from picture import picture
from rppGui import Gui

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
    
    # Methods for procesing
    def createPictureList(self):
        for folder in self.inputPathDict.keys():
            for fileName in listdir(folder):
                self.pictureList.append(picture(folder, fileName, self.inputPathDict[folder]))
        print self.pictureList
    
    def startGUI(self):
        # startGUI
        gFr = Gui(self)
        #self.createPictureList()
            
            #This statement ONLY after successful annotation!
            #self.pictureList.remove(pic)
    
    def nextPicture(self, event):
        if len(self.pictureList) > 0:
            rImage = random.choice(self.pictureList)
            self.imp = rImage.getImp()
            
    def prevPicture(self, event):
        print "previous pic"
            
    def exit(self):
        exit(0)

        
# main
p = picturePicker()
p.showInitDialog()

p.createPictureList()
print p.getAnnotationType()
p.startGUI()
