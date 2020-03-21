from javax.swing import *
from java.awt import *
from java.text import *
import sys

mouseLoc = []

class mainWindow(JFrame):
  def __init__(self):
    super(mainWindow, self).__init__()
    self.initComponents()
    
  def initComponents(self):
    self.bgPanel = JPanel(mousePressed = self.bgPanelMousePressed,
                          mouseDragged = self.bgPanelMouseDragged)
    self.exitButton = JLabel(mouseClicked = self.exitButtonMouseClicked)
    self.fnameField = JTextField(focusGained = self.fnameFieldFocusGained)
    self.lnameField = JTextField(focusGained = self.lnameFieldFocusGained)
    self.emailsField = JTextField(focusGained = self.emailsFieldFocusGained)
    self.numsField = JTextField(focusGained = self.numsFieldFocusGained)
    self.dobField = JFormattedTextField(focusGained = self.dobFieldFocusGained)
    self.fnameLabel = JLabel()
    self.lnameLabel = JLabel()
    self.dobLabel = JLabel()
    self.emailsLabel = JLabel()
    self.phoneLabel = JLabel()
    self.addButton = JLabel(mouseEntered = self.addButtonMouseEntered,
                            mouseExited = self.addButtonMouseExited)
    self.jScrollPane2 = JScrollPane()
    self.peopleTable = JTable()
    self.delButton = JLabel(mouseEntered = self.delButtonMouseEntered,
                            mouseExited = self.delButtonMouseExited)

    self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    self.setUndecorated(True)

    self.bgPanel.setBackground(Color(255, 153, 0))

    self.exitButton.setText("X")
    self.exitButton.setCursor(Cursor(Cursor.HAND_CURSOR))

    self.dobField.setFormatterFactory(text.DefaultFormatterFactory(text.DateFormatter(SimpleDateFormat("MM/dd/yyyy"))))

    self.fnameLabel.setText("First Name")

    self.lnameLabel.setText("Last Name")

    self.dobLabel.setText("Date of Birth (MM/DD/YYYY)")

    self.emailsLabel.setText("E-mail")

    self.phoneLabel.setText("Phone Number")

    self.addButton.setBackground(Color(255, 255, 255))
    self.addButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.addButton.setText("Add Person")
    self.addButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.addButton.setOpaque(True)

    self.peopleTable.setModel(table.DefaultTableModel(
      [],
      ["ID", "First Name", "Last Name", "Date of Birth", "E-mail(s)", "Phone Num(s)"]))
    self.jScrollPane2.setViewportView(self.peopleTable)

    self.delButton.setBackground(Color(255, 102, 102))
    self.delButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.delButton.setText("Delete Person")
    self.delButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.delButton.setOpaque(True)

    bgPanelLayout = GroupLayout(self.bgPanel)
    self.bgPanel.setLayout(bgPanelLayout)
    bgPanelLayout.setHorizontalGroup(
      bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addGroup(bgPanelLayout.createSequentialGroup()
        .addContainerGap()
        .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
          .addGroup(GroupLayout.Alignment.TRAILING, bgPanelLayout.createSequentialGroup()
            .addGap(0, 0, sys.maxint)
            .addComponent(self.exitButton))
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.TRAILING)
              .addComponent(self.fnameLabel)
              .addComponent(self.lnameLabel)
              .addComponent(self.dobLabel)
              .addComponent(self.emailsLabel)
              .addComponent(self.phoneLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
              .addComponent(self.addButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
              .addComponent(self.lnameField)
              .addComponent(self.fnameField)
              .addComponent(self.emailsField)
              .addComponent(self.numsField)
              .addComponent(self.dobField)
              .addComponent(self.delButton, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 285, sys.maxint))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addComponent(self.jScrollPane2, GroupLayout.DEFAULT_SIZE, 633, sys.maxint)))
        .addContainerGap()))
    
    bgPanelLayout.setVerticalGroup(
      bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addGroup(bgPanelLayout.createSequentialGroup()
        .addContainerGap()
        .addComponent(self.exitButton)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
              .addComponent(self.fnameField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.fnameLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
              .addComponent(self.lnameField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.lnameLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
              .addComponent(self.dobField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.dobLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
              .addComponent(self.emailsField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.emailsLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
              .addComponent(self.numsField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.phoneLabel))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
            .addComponent(self.addButton, GroupLayout.PREFERRED_SIZE, 47, GroupLayout.PREFERRED_SIZE)
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, sys.maxint)
            .addComponent(self.delButton, GroupLayout.PREFERRED_SIZE, 47, GroupLayout.PREFERRED_SIZE))
          .addComponent(self.jScrollPane2, GroupLayout.DEFAULT_SIZE, 512, sys.maxint))
        .addContainerGap()))

    layout = GroupLayout(self.getContentPane())
    self.getContentPane().setLayout(layout)
    layout.setHorizontalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint))
    
    layout.setVerticalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint))

    self.pack()
    self.setLocationRelativeTo(None)
    
  def exitButtonMouseClicked(self, evt):
    sys.exit()
    
  def fnameFieldFocusGained(self, evt):
    self.fnameField.selectAll()
    
  def lnameFieldFocusGained(self, evt):
    self.lnameField.selectAll()
    
  def emailsFieldFocusGained(self, evt):
    self.emailsField.selectAll()
    
  def numsFieldFocusGained(self, evt):
    self.numsField.selectAll()
    
  def dobFieldFocusGained(self, evt):
    self.dobField.selectAll()
    
  def addButtonMouseEntered(self, evt):
    self.addButton.setBorder(border.LineBorder(Color.BLACK))
    
  def addButtonMouseExited(self, evt):
    self.addButton.setBorder(None)
    
  def delButtonMouseEntered(self, evt):
    self.delButton.setBorder(border.LineBorder(Color.BLACK))
    
  def delButtonMouseExited(self, evt):
    self.delButton.setBorder(None)
    
  def bgPanelMousePressed(self, evt):
    del mouseLoc[:]
    mouseLoc.append(evt.getX())
    mouseLoc.append(evt.getY())
    
  def bgPanelMouseDragged(self, evt):
    x = evt.getXOnScreen()
    y = evt.getYOnScreen()
    
    self.setLocation(x - mouseLoc[0], y - mouseLoc[1])
  
if __name__ == "__main__":
  mainWindow().setVisible(True)