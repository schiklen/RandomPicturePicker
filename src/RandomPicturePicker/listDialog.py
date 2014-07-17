'''
Created on Jul 16, 2014

@author: schiklen
'''
from javax.swing import JDialog, JFrame, JList, JScrollPane, JTextField, DefaultListModel, ListSelectionModel, JButton, JPanel, GroupLayout
from java.awt import Dimension
class listDialog(JDialog):
    '''
    classdocs
    '''


    def __init__(self, pP):
        '''
        Constructor
        '''
        self.list = []
        self.pP = pP
        self.setTitle("Create annotation list")
        
        #Components
        self.textField = JTextField("",16)

        self.listModel = DefaultListModel()
        self.listModel.addElement("obj")
        self.listBox = JList(self.listModel)
        self.listBox.setSelectionMode(ListSelectionModel.SINGLE_SELECTION)
        #self.listBox.addListSelectionListener(self)
        self.listBox.setVisibleRowCount(5)
        listScroller = JScrollPane(self.listBox)
        
        addButton = JButton("Add", actionPerformed = self.addToList)
        rmButton = JButton("Remove", actionPerformed = self.rmFromList)
        okButton = JButton("OK", actionPerformed = self.ok)
        
        #layout
        layout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.CENTER)
                                    .addComponent(self.textField)
                                    .addComponent(listScroller)
                                    .addGroup(layout.createSequentialGroup()
                                              .addComponent(addButton)
                                              .addComponent(rmButton)
                                              .addComponent(okButton)
                                              )
                                    )
        layout.setVerticalGroup(layout.createSequentialGroup()
                                .addComponent(self.textField)
                                .addComponent(listScroller)
                                .addGroup(layout.createParallelGroup()
                                          .addComponent(addButton)
                                          .addComponent(rmButton)
                                          .addComponent(okButton)
                                         ))
        self.pack()
        self.setVisible(True)
        
        
    def addToList(self, event):
        if self.textField.getText != "":
            self.listModel.addElement(self.textField.getText())
        self.textField.setText("")
        
    def rmFromList(self, event):
        self.listModel.remove(self.listBox.getSelectedIndex())
    
    def ok(self, event):
        print "ok"
        print list(self.listModel.toArray())
        self.pP.setAnnotationType(list(self.listModel.toArray()))
        
        self.dispose()
        
#--- main for test
#listDialog()