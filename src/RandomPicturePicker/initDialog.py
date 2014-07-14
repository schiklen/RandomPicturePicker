'''
Created on Jun 3, 2014

@author: schiklen
'''
from javax.swing import JButton, JLabel, JFrame, JDialog, GroupLayout, JTextField, JPanel, JRadioButton, ButtonGroup, BorderFactory, SwingConstants
from java.awt.Dialog import ModalityType
from os import path
from datetime import date
from ij.io import DirectoryChooser

class initDialog(JDialog): # JFrame
    
    def __init__(self, pP):
        # fields
        self.tPath = ""
        self.cPath = ""
        self.exPath = ""
        self.annotate = []
        self.picPicker = pP
    
        super(initDialog, self).__init__()
        self.initUI()


    def initUI(self):
        
        inputPanel = JPanel()
        inputPanel.setBorder(BorderFactory.createTitledBorder("Where are your control and treament images?"))
        inputLayout = GroupLayout(inputPanel)
        inputPanel.setLayout(inputLayout)
        inputLayout.setAutoCreateContainerGaps(True)
        inputLayout.setAutoCreateGaps(True)
        
        annotatePanel = JPanel()
        annotatePanel.setBorder(BorderFactory.createTitledBorder("How do you want to annotate your data?"))
        anLayout = GroupLayout(annotatePanel)
        annotatePanel.setLayout(anLayout)
        anLayout.setAutoCreateContainerGaps(True)
        anLayout.setAutoCreateGaps(True)
        
        exportPanel = JPanel()
        exportPanel.setBorder(BorderFactory.createTitledBorder("Where do you want to export your data"))
        exportLayout = GroupLayout(exportPanel)
        exportPanel.setLayout(exportLayout)
        exportLayout.setAutoCreateContainerGaps(True)
        exportLayout.setAutoCreateGaps(True)
        
        btnPanel = JPanel()
        btnLayout = GroupLayout(btnPanel)
        btnPanel.setLayout(btnLayout)
        btnLayout.setAutoCreateContainerGaps(True)
        btnLayout.setAutoCreateGaps(True)
        
        
        layout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)

        self.setModalityType(ModalityType.APPLICATION_MODAL)
        self.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE)# JFrame.EXIT_ON_CLOSE)
        # definition of elements
        # labels
        cPathLabel = JLabel("Control Path:")
        tPathLabel = JLabel("Treatment Path:")
        exPathLabel = JLabel("Save Results in:")
        
        #textfields
        self.cPathField = JTextField("", 16)
        self.tPathField = JTextField("", 16)
        self.exPathField = JTextField("", 16)
        
        #radiobuttons
        yesNoRButton = JRadioButton("Yes / No / Ignore")
        intRButton = JRadioButton("Integer")
        nRButton = JRadioButton("Number")
        listRButton = JRadioButton("From List")
        self.rBGroup = ButtonGroup()
        self.rBGroup.add(yesNoRButton)
        self.rBGroup.add(intRButton)
        self.rBGroup.add(nRButton)
        self.rBGroup.add(listRButton)
        
        
        #buttons
        cPathButton = JButton("Browse...", actionPerformed=self.browseC) # lambda on fieldvalue
        tPathButton = JButton("Browse...", actionPerformed=self.browseT) # lambda on fieldvalue
        exPathButton = JButton("Browse...", actionPerformed=self.browseE)
        OKButton = JButton("OK",actionPerformed=self.okayEvent)
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
                                    .addComponent(listRButton))
        anLayout.setVerticalGroup(anLayout.createSequentialGroup()
                                    .addComponent(yesNoRButton)
                                    .addComponent(intRButton)
                                    .addComponent(nRButton)
                                    .addComponent(listRButton))
        
        
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

        #self.setSize(200, 150)
        self.pack()
        self.setLocationRelativeTo(None)
        self.setVisible(True)

    def addDirToList(self, p):
        self.dirPathList.append(p)
        #maybe add to listmodel

    def browseT(self, event):
        self.tPathField.text = DirectoryChooser("Select Treatment Folder").getDirectory()
        
    def browseC(self, event):
        self.cPathField.text = DirectoryChooser("Select Control Folder").getDirectory()

    def browseE(self, event):
        self.exPathField.text = DirectoryChooser("Select Export Folder").getDirectory()
        self.picPicker.setOutputPath(self.exPathField.text)

            
    def cancel(self, event):
        exit(0)

    def okayEvent(self, event):
        inputDict = {self.tPathField.getText():"treatment", self.cPathField.getText():"control"} # this is for later extension
        self.picPicker.setInputPathDict(inputDict)
        
        self.picPicker.setOutputPath(self.exPathField.getText())
        print "A " + str(self.rBGroup.getSelection().getActionCommand())
        print "B " + str(self.rBGroup.getSelection())
        self.picPicker.setAnnotationType(self.rBGroup.getSelection().getActionCommand())
        
        self.dispose()