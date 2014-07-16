'''
Created on Jul 16, 2014

@author: schiklen
'''
from javax.swing import JDialog, JFrame, JList, JScrollPane, JTextField, DefaultListModel, ListSelectionModel, JButton, JPanel, GroupLayout

class listDialog(JDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list = []
        
        #Components
        self.textField = JTextField("",16)

        self.listModel = DefaultListModel()
        self.listModel.addElement("obj")
        self.listBox = JList(self.listModel)
        self.listBox.setSelectionMode(ListSelectionModel.SINGLE_SELECTION)
        #self.listBox.addListSelectionListener(self)
        self.listBox.setVisibleRowCount(5)
        listScrollPane = JScrollPane(self.listBox)
        
        addButton = JButton("Add", actionPerformed = self.addToList)
        rmButton = JButton("Remove", actionPerformed = self.rmFromList)
        okButton = JButton("OK", actionPerformed = self.ok)
        
        #layout
        layout = GroupLayout(self.getContentPane())
        self.getContentPane().setLayout(layout)
        
        layout.setHorizontalGroup(layout.createParallelGroup(GroupLayout.Alignment.CENTER)
                                    .addComponent(self.textField)
                                    .addComponent(self.listBox)
                                    .addGroup(layout.createSequentialGroup()
                                              .addComponent(addButton)
                                              .addComponent(rmButton)
                                              .addComponent(okButton)
                                              )
                                    )
        layout.setVerticalGroup(layout.createSequentialGroup()
                                .addComponent(self.textField)
                                .addComponent(self.listBox)
                                .addGroup(layout.createParallelGroup()
                                          .addComponent(addButton)
                                          .addComponent(rmButton)
                                          .addComponent(okButton)
                                         ))
        self.pack()
        self.setVisible(True)
        
        
    def addToList(self, event):
        print "add"
        
    def rmFromList(self, event):
        print "Remove"
        #self.listModel.removeElement()
    
    def ok(self, event):
        print "ok"
        
        self.dispose()
        
#--- main for test
listDialog()