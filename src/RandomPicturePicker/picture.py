'''
Created on Jun 6, 2014

@author: schiklen
'''
from os import path
from ij.io import Opener

class picture(object):
    '''
    classdocs
    '''

    def __init__(self, folderPath, fileName, group): # sting path folderPath, fileName, boolean shown
        '''
        Constructor
        '''
        self.directory = folderPath
        self.fileName = fileName
        self.fullPath = path.join(self.directory, self.fileName)
        self.group = group
        
        self.annotation = None
        
    def getImp(self):
        imp = Opener().openImage(self.fullPath)
        return imp
    
    def getImagePath(self):
        return self.fullPath
    
    def annotate(self, annotation):
        self.annotation = annotation
    
    