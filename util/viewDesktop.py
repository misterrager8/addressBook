import csv
import subprocess
import sys

from java.awt import *
from java.text import *
from javax.swing import *
from javax.swing.table import *

from model import *

mouse_loc = []
person_list = []


class Tablemodelwrapper(DefaultTableModel):
    def __init__(self):
        pass


class Mainwindow(JFrame):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.bgPanel = JPanel(mousePressed=self.bgPanelMousePressed,
                              mouseDragged=self.bgPanelMouseDragged)
        self.exit_button = JLabel(mouseClicked=self.exitButtonMouseClicked)
        self.fname_field = JTextField(focusGained=self.fnameFieldFocusGained)
        self.lname_field = JTextField(focusGained=self.lnameFieldFocusGained)
        self.emails_field = JTextField(focusGained=self.emailsFieldFocusGained)
        self.nums_field = JTextField(focusGained=self.numsFieldFocusGained)
        self.dob_field = JFormattedTextField(focusGained=self.dobFieldFocusGained)
        self.fname_label = JLabel()
        self.lname_label = JLabel()
        self.dob_label = JLabel()
        self.emails_label = JLabel()
        self.phone_label = JLabel()
        self.add_button = JLabel(mouseEntered=self.addButtonMouseEntered,
                                 mouseExited=self.addButtonMouseExited,
                                 mouseClicked=self.addButtonMouseClicked)
        self.j_scroll_pane2 = JScrollPane()
        self.people_table = JTable()
        self.del_button = JLabel(mouseEntered=self.delButtonMouseEntered,
                                 mouseExited=self.delButtonMouseExited,
                                 mouseClicked=self.delButtonMouseClicked)
        self.init_components()
        self.setVisible(True)

    def init_components(self):
        self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        self.setUndecorated(True)

        self.bgPanel.setBackground(Color(255, 153, 0))

        self.exit_button.setText("X")
        self.exit_button.setCursor(Cursor(Cursor.HAND_CURSOR))

        self.dob_field.setFormatterFactory(
            text.DefaultFormatterFactory(text.DateFormatter(SimpleDateFormat("MM/dd/yyyy"))))

        self.fname_label.setText("First Name")

        self.lname_label.setText("Last Name")

        self.dob_label.setText("Date of Birth (MM/DD/YYYY)")

        self.emails_label.setText("E-mail")

        self.phone_label.setText("Phone Number")

        self.add_button.setBackground(Color(255, 255, 255))
        self.add_button.setHorizontalAlignment(SwingConstants.CENTER)
        self.add_button.setText("Add Person")
        self.add_button.setCursor(Cursor(Cursor.HAND_CURSOR))
        self.add_button.setOpaque(True)

        self.people_table.setModel(table.DefaultTableModel(
            [],
            ["ID", "First Name", "Last Name", "Date of Birth", "E-mail(s)", "Phone Num(s)"]))
        self.j_scroll_pane2.setViewportView(self.people_table)

        self.del_button.setBackground(Color(255, 102, 102))
        self.del_button.setHorizontalAlignment(SwingConstants.CENTER)
        self.del_button.setText("Delete Person")
        self.del_button.setCursor(Cursor(Cursor.HAND_CURSOR))
        self.del_button.setOpaque(True)

        bgPanelLayout = GroupLayout(self.bgPanel)
        self.bgPanel.setLayout(bgPanelLayout)
        bgPanelLayout.setHorizontalGroup(
            bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
                .addGroup(bgPanelLayout.createSequentialGroup()
                          .addContainerGap()
                          .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
                                    .addGroup(GroupLayout.Alignment.TRAILING, bgPanelLayout.createSequentialGroup()
                                              .addGap(0, 0, sys.maxint)
                                              .addComponent(self.exit_button))
                                    .addGroup(bgPanelLayout.createSequentialGroup()
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.TRAILING)
                    .addComponent(self.fname_label)
                    .addComponent(self.lname_label)
                    .addComponent(self.dob_label)
                    .addComponent(self.emails_label)
                    .addComponent(self.phone_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
                    .addComponent(self.add_button, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
                    .addComponent(self.lname_field)
                    .addComponent(self.fname_field)
                    .addComponent(self.emails_field)
                    .addComponent(self.nums_field)
                    .addComponent(self.dob_field)
                    .addComponent(self.del_button, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 285,
                                  sys.maxint))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addComponent(self.j_scroll_pane2, GroupLayout.DEFAULT_SIZE, 633,
                                                            sys.maxint)))
                          .addContainerGap()))

        bgPanelLayout.setVerticalGroup(
            bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
                .addGroup(bgPanelLayout.createSequentialGroup()
                          .addContainerGap()
                          .addComponent(self.exit_button)
                          .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                          .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
                                    .addGroup(bgPanelLayout.createSequentialGroup()
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.fname_field, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
                                  GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.fname_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.lname_field, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
                                  GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.lname_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.dob_field, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
                                  GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.dob_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.emails_field, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
                                  GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.emails_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addGroup(
                bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(self.nums_field, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE,
                                  GroupLayout.PREFERRED_SIZE)
                    .addComponent(self.phone_label))
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
                                              .addComponent(self.add_button, GroupLayout.PREFERRED_SIZE, 47,
                                                            GroupLayout.PREFERRED_SIZE)
                                              .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED,
                                                               GroupLayout.DEFAULT_SIZE, sys.maxint)
                                              .addComponent(self.del_button, GroupLayout.PREFERRED_SIZE, 47,
                                                            GroupLayout.PREFERRED_SIZE))
                                    .addComponent(self.j_scroll_pane2, GroupLayout.DEFAULT_SIZE, 512, sys.maxint))
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
        self.fname_field.selectAll()

    def lnameFieldFocusGained(self, evt):
        self.lname_field.selectAll()

    def emailsFieldFocusGained(self, evt):
        self.emails_field.selectAll()

    def numsFieldFocusGained(self, evt):
        self.nums_field.selectAll()

    def dobFieldFocusGained(self, evt):
        self.dob_field.selectAll()

    def addButtonMouseEntered(self, evt):
        self.add_button.setBorder(border.LineBorder(Color.BLACK))

    def addButtonMouseExited(self, evt):
        self.add_button.setBorder(None)

    def delButtonMouseEntered(self, evt):
        self.del_button.setBorder(border.LineBorder(Color.BLACK))

    def delButtonMouseExited(self, evt):
        self.del_button.setBorder(None)

    def bgPanelMousePressed(self, evt):
        del mouse_loc[:]
        mouse_loc.append(evt.getX())
        mouse_loc.append(evt.getY())

    def bgPanelMouseDragged(self, evt):
        x = evt.getXOnScreen()
        y = evt.getYOnScreen()

        self.setLocation(x - mouse_loc[0], y - mouse_loc[1])

    def addButtonMouseClicked(self, evt):
        f_name = self.fname_field.getText()
        l_name = self.lname_field.getText()
        dob = self.dob_field.getText()
        email = self.emails_field.getText()
        tel_number = self.nums_field.getText()

        x = Person(None, f_name, l_name, dob, email, tel_number)
        subprocess.call("python ctrla.py add", shell=True)

    def delButtonMouseClicked(self, evt):
        pass

    def view_table(self):
        with open("albumsList.csv", "r") as f:
            reader = csv.reader(f)
            temp_list = list(reader)

        del person_list[:]

        for item in temp_list:
            person_list.append(Person(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

        self.people_table.getModel().setRowCount(0)

        for idx, item in enumerate(person_list):
            self.people_table.getModel().addRow([item.person_id, item.fname, item.lname, item.dob, item.email, item.number])


if __name__ == "__main__":
    Mainwindow()
