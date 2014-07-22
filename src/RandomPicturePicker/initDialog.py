'''
Created on Jun 3, 2014

@author: schiklen
'''
from javax.swing import JButton, JLabel, JFrame, JDialog, GroupLayout, JTextField, JPanel, JRadioButton, ButtonGroup, JList, DefaultListModel,  BorderFactory, SwingConstants
from java.awt.Dialog import ModalityType
from os import path
from datetime import date
from ij.io import DirectoryChooser
from listDialog import listDialog

class initDialog(JDialog): # JFrame
    
    def __init__(self, pP):
        # fields
        self.tPath = ""
        self.cPath = ""
        self.exPath = ""
        self.picPicker = pP
        self.annotationType = self.picPicker.getAnnotationType()
    
        super(initDialog, self).__init__()
        
        self.initUI()


    def initUI(self):
        
        inputPanel = JPanel()
        inputPanel.setBorder(BorderFactory.createTitledBorder("Where are your control and treament images?"))
        inputLayout = GroupLayout(inputPanel, autoCreateContainerGaps=True, autoCreateGaps=True)
        inputPanel.setLayout(inputLayout)
        
        annotatePanel = JPanel()
        annotatePanel.setBorder(BorderFactory.createTitledBorder("How do you want to annotate your data?"))
        anLayout = GroupLayout(annotatePanel, autoCreateContainerGaps=True, autoCreateGaps=True)
        annotatePanel.setLayout(anLayout)
        
        exportPanel = JPanel()
        exportPanel.setBorder(BorderFactory.createTitledBorder("Where do you want to export your data"))
        exportLayout = GroupLayout(exportPanel, autoCreateContainerGaps=True, autoCreateGaps=True)
        exportPanel.setLayout(exportLayout)
        
        btnPanel = JPanel()
        btnLayout = GroupLayout(btnPanel, autoCreateContainerGaps=True, autoCreateGaps=True)
        btnPanel.setLayout(btnLayout)
        
        layout = GroupLayout(self.getContentPane(), autoCreateContainerGaps=True, autoCreateGaps=True)
        self.getContentPane().setLayout(layout)

        self.setModalityType(ModalityType.APPLICATION_MODAL)
        self.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE)# JFrame.EXIT_ON_CLOSE)
        # definition of elements
        # labels
        cPathLabel = JLabel("Control Path:")
        tPathLabel = JLabel("Treatment Path:")
        exPathLabel = JLabel("Save Results in:")
        
        #textfields
        self.cPathField = JTextField("/Users/schiklen/DotData/131118_dummy/131118_2926/cutout/", 16)
        self.tPathField = JTextField("/Users/schiklen/DotData/131118_dummy/131118_2926/cutout/", 16)
        self.exPathField = JTextField("/Users/schiklen/DotData/131118_dummy/131118_2926/cutout/", 16)
        
        #Radiobuttons
        yesNoRButton = JRadioButton("Yes / No / Ignore", selected=True, actionCommand="yesNoIgnore", actionPerformed=self.setAnnotationTypeDialog)
        intRButton = JRadioButton("Integer", actionCommand="int", actionPerformed=self.setAnnotationTypeDialog)
        nRButton = JRadioButton("Number", actionCommand="float", actionPerformed=self.setAnnotationTypeDialog)
        listRButton = JRadioButton("From List...", actionCommand="list", actionPerformed=self.openListDialog)

        self.rBGroup = ButtonGroup()
        self.rBGroup.add(yesNoRButton)
        self.rBGroup.add(intRButton)
        self.rBGroup.add(nRButton)
        self.rBGroup.add(listRButton)
        
        #self.customListButton = JButton("Custom List...", actionPerformed=self.makeCustomList, enabled=0)
        
        #buttons
        cPathButton = JButton("Browse...", actionPerformed=self.browseC) # lambda on fieldvalue
        tPathButton = JButton("Browse...", actionPerformed=self.browseT) # lambda on fieldvalue
        exPathButton = JButton("Browse...", actionPerformed=self.browseE)
        OKButton = JButton("OK", actionPerformed=self.okayEvent)
        CancelButton = JButton("Cancel", actionPerformed=self.cancel)
        
        '''General ContentPane Layout'''
        layout.setHorizontalGroup(layout.createParallelGroup()
                                  .addComponent(inputPanel)
                                  .addComponent(annotatePanel)
                                  .addComponent(exportPanel)
                                  .addComponent(btnPanel)
                                  )
        layout.linkSize(SwingConstants.HORIZONTAL, inputPanel, annotatePanel, exportPanel, btnPanel)
        layout.setVerticalGroup(layout.createSequentialGroup()
                                .addComponent(inputPanel)
                                .addComponent(annotatePanel)
                                .addComponent(exportPanel)
                                .addComponent(btnPanel)
                                )
        
        ''' Input panel Layout '''
        inputLayout.setHorizontalGroup(inputLayout.createSequentialGroup()
                                       .addGroup(inputLayout.createParallelGroup(GroupLayout.Alignment.TRAILING)
                                                 .addComponent(cPathLabel)
                                                 .addComponent(tPathLabel))
                                       .addGroup(inputLayout.createParallelGroup(GroupLayout.Alignment.TRAILING)
                                                 .addComponent(self.cPathField)
                                                 .addComponent(self.tPathField))
                                       .addGroup(inputLayout.createParallelGroup()
                                                 .addComponent(cPathButton)
                                                 .addComponent(tPathButton))
                                       )
        
        inputLayout.setVerticalGroup(inputLayout.createSequentialGroup()
                                       .addGroup(inputLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                                 .addComponent(cPathLabel)
                                                 .addComponent(self.cPathField)
                                                 .addComponent(cPathButton))
                                       .addGroup(inputLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                                 .addComponent(tPathLabel)
                                                 .addComponent(self.tPathField)
                                                 .addComponent(tPathButton))
                                     )
        
        '''Annotate panel layout'''
        anLayout.setHorizontalGroup(anLayout.createParallelGroup()
                                    .addComponent(yesNoRButton)
                                    .addComponent(intRButton)
                                    .addComponent(nRButton)
                                    .addComponent(listRButton)
                                    #.addComponent(self.customListButton)
                                    )
        anLayout.setVerticalGroup(anLayout.createSequentialGroup()
                                    .addComponent(yesNoRButton)
                                    .addComponent(intRButton)
                                    .addComponent(nRButton)
                                    .addComponent(listRButton)
                                    #.addComponent(self.customListButton)
                                    )
        
        
        '''Export panel layout'''
        exportLayout.setHorizontalGroup(exportLayout.createSequentialGroup()
                                        .addComponent(exPathLabel)
                                        .addComponent(self.exPathField)
                                        .addComponent(exPathButton))
        exportLayout.setVerticalGroup(exportLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                        .addComponent(exPathLabel)
                                        .addComponent(self.exPathField)
                                        .addComponent(exPathButton))
        
        
        '''Buttons Panel Layout'''
        btnLayout.setHorizontalGroup(btnLayout.createSequentialGroup()
                                     .addComponent(CancelButton)
                                     .addComponent(OKButton)
                                     )
        btnLayout.setVerticalGroup(btnLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                   .addComponent(CancelButton)
                                   .addComponent(OKButton)
                                   )

        self.setTitle("Random Picture Picker")

        self.pack()
        self.setLocationRelativeTo(None)
        self.setVisible(True)

    def addDirToList(self, p):
        self.dirPathList.append(p)

    def browseT(self, event):
        self.tPathField.text = DirectoryChooser("Select Treatment Folder").getDirectory()
        
    def browseC(self, event):
        self.cPathField.text = DirectoryChooser("Select Control Folder").getDirectory()

    def browseE(self, event):
        self.exPathField.text = DirectoryChooser("Select Export Folder").getDirectory()
        self.picPicker.setOutputPath(self.exPathField.text)

    def makeCustomList(self):
        ld = listDialog(self)
        ld.startUI()
        
    def cancel(self, event):
        exit(0)

    def okayEvent(self, event):
        inputDict = {self.tPathField.getText():"treatment", self.cPathField.getText():"control"} # this is for later extension
        self.picPicker.setInputPathDict(inputDict)
        self.picPicker.setOutputPath(self.exPathField.getText())
        
        self.dispose()
        
    def getPicPicker(self):
        return self.picPicker

    def setAnnotationTypeDialog(self, event):
        annotype = self.rBGroup.getSelection().getActionCommand()
        if annotype == "int" or "float":
            self.picPicker.setAnnotationType(["text"])
        if annotype == "yesNoIgnore":
            self.picPicker.setAnnotationType(["Yes", "No", "Ignore"])
    
    def openListDialog(self,event):
        self.makeCustomList()
        #self.customListButton.setEnabled(True)