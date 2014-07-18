'''
Created on Jun 8, 2014

@author: schiklen
'''
from javax.swing import JButton, JLabel, JFrame, GroupLayout, JTextField, JPanel, JRadioButton, JProgressBar, ButtonGroup, BorderFactory, SwingConstants
from java.awt import GridLayout, Dialog # abstract window toolkit
from os import path
from datetime import date


class Gui(JFrame):
    '''
    classdocs
    '''


    def __init__(self, pP):
        '''
        Constructor
        '''
        self.pP = pP
        
        self.setTitle("Random Picture Picker")

        #annotation Panel
        annoPanel = JPanel()
        annoPanel.setBorder(BorderFactory.createTitledBorder("Annotations"))
        annoPLayout = GroupLayout(annoPanel)
        annoPanel.setLayout(annoPLayout)
        annoPLayout.setAutoCreateContainerGaps(True)
        annoPLayout.setAutoCreateGaps(True)        

        # dynamic creation of annotation panel
        # yesNoIgnore, int, number, list
        if self.pP.getAnnotationType() == "int":
            self.annoField = JTextField("", 4)
            annoPLayout.setHorizontalGroup(annoPLayout.createParallelGroup().addComponent(self.annoField))
            annoPLayout.setVerticalGroup(annoPLayout.createSequentialGroup().addComponent(self.annoField))
        elif self.pP.getAnnotationType() == "number":
            self.annoField = JTextField("", 16)
            annoPLayout.setHorizontalGroup(annoPLayout.createParallelGroup().addComponent(self.annoField))
            annoPLayout.setVerticalGroup(annoPLayout.createSequentialGroup().addComponent(self.annoField))
        elif self.pP.getAnnotationType() == "yesNoIgnore" or "list":
            choices = pP.getAnnotationType()
            print "choices", choices
            choiceBtns = []
            self.annoField = ButtonGroup()
            for c in choices:
                Btn = JRadioButton(c)
                self.annoField.add(Btn)
                choiceBtns.append(Btn)
          
            h = annoPLayout.createParallelGroup()
            for b in choiceBtns:
                h.addComponent(b)
            annoPLayout.setHorizontalGroup(h)
            
            v = annoPLayout.createSequentialGroup()
            for b in choiceBtns:
                v.addComponent(b)
            annoPLayout.setVerticalGroup(v)


        # Control Panel
        ctrlPanel = JPanel()
        ctrlPLayout = GroupLayout(ctrlPanel, autoCreateContainerGaps=True, autoCreateGaps=True)
        ctrlPanel.setLayout(ctrlPLayout)
        
        nextImgButton = JButton("Next >", actionPerformed=self.pP.nextPicture)
        prevImgButton = JButton("< Prev", actionPerformed=self.pP.prevPicture)
        quitButton = JButton("Quit", actionPerformed=self.exit)

        ctrlPLayout.setHorizontalGroup(ctrlPLayout.createParallelGroup(GroupLayout.Alignment.CENTER)
                                       .addGroup(ctrlPLayout.createSequentialGroup()
                                                 .addComponent(prevImgButton)
                                                 .addComponent(nextImgButton))
                                       .addComponent(quitButton))
        ctrlPLayout.setVerticalGroup(ctrlPLayout.createSequentialGroup()
                                     .addGroup(ctrlPLayout.createParallelGroup()
                                               .addComponent(prevImgButton)
                                               .addComponent(nextImgButton))
                                     .addComponent(quitButton))
        ctrlPLayout.linkSize(SwingConstants.HORIZONTAL, quitButton)

        
        statusPanel = JPanel()   # contains status information: progress bar
        self.progressBar = JProgressBar()
        self.progressBar.setStringPainted(True)
        self.progressBar.setValue(0)
        statusPanel.add(self.progressBar)
        
        #MainLayout
        mainLayout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(mainLayout)
        
        mainLayout.setHorizontalGroup(mainLayout.createParallelGroup(GroupLayout.Alignment.CENTER)
                                    .addComponent(annoPanel)
                                    .addComponent(ctrlPanel)
                                    .addComponent(statusPanel)
                                    )
        mainLayout.setVerticalGroup(mainLayout.createSequentialGroup()
                                    .addComponent(annoPanel)
                                    .addComponent(ctrlPanel)
                                    .addComponent(statusPanel)
                                    )
        mainLayout.linkSize(SwingConstants.HORIZONTAL, annoPanel, ctrlPanel, statusPanel)
         
      
        self.pack()
        self.setVisible(True)
        
    #def getAnnotation(self):
    #    return 
    
    def exit(self, event):
        self.pP.exit()
        self.dispose()

# Main for test purposes
#
