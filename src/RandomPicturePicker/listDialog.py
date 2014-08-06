'''
Random Picture Picker module
Created on Jul 16, 2014

@author: schiklen
'''
from javax.swing import JDialog, JList, JScrollPane, JTextField, DefaultListModel, ListSelectionModel, JButton, GroupLayout
from java.awt.Dialog import ModalityType
from java.awt import Dialog
class listDialog(JDialog):
    '''
    classdocs
    '''

    #Constructor
    def startUI(self):
        self.setTitle("Create annotation list")
        #Components
        self.textField = JTextField("", 16)
        self.annotationType = []
        self.setModalityType(Dialog.ModalityType.DOCUMENT_MODAL)

        self.listModel = DefaultListModel()
        self.listModel.addElement("Nucleus")
        self.listModel.addElement("Cytoplasm")
        self.listModel.addElement("Plasma Membrane")
        self.listBox = JList(self.listModel)
        self.listBox.setSelectionMode(ListSelectionModel.SINGLE_SELECTION)
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
                                         )
                                )
        
        self.pack()
        self.setLocationRelativeTo(self.getParent())
        self.setVisible(True)
        
    def addToList(self, event):
        if self.textField.getText != "":
            self.listModel.addElement(self.textField.getText())
        self.textField.setText("")
        
    def rmFromList(self, event):
        self.listModel.remove(self.listBox.getSelectedIndex())
    
    def getAnnotationType(self):
        return self.annotationType
    
    def ok(self, event):
        print "Annotation list", list(self.listModel.toArray())
        self.annotationType = list(self.listModel.toArray())
        self.getParent().getPicPicker().setAnnotationType(list(self.listModel.toArray()))
        self.dispose()

        
#--- main for test
#listDialog()