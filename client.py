import socket
import threading
from javax.swing import *
from java.awt import *

class Client:

  def Send(self,event):
  	z=self.textfield.text
  	self.list.getModel().addElement('you:'+z)
  	self.s.send(z)
  def __init__(self):

        # These lines setup the basic frame, size and layout
        # the setDefaultCloseOperation is required to completely exit the app
        # when you click the close button
    frame = JFrame("Chat Application(Client)")
    frame.setSize(200, 225)
    frame.setLayout(BorderLayout())
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)

    # set up the list and the contents of the list
    # the python typle get converted to a Java vector    
    self.list = JList(DefaultListModel())
    spane = JScrollPane()
    spane.setPreferredSize(Dimension(100,125))
    spane.getViewport().setView((self.list))
    self.textfield=JTextField('',50)
        # a panel is a bit over kill but this is a demo. :)
    label1=JLabel('Enter the text')
    panel = JPanel()
    panel.add(spane)
    panel.add(label1)
    panel.add(self.textfield)
    frame.add(panel,BorderLayout.CENTER)
        # create the button, and city label and the show our work
        # with Jython only one line is needed create a button and attach an
        # event handler.
    btn = JButton('Send',actionPerformed=self.Send)
    frame.add(btn,BorderLayout.SOUTH)
    self.label = JLabel(' Received  Messages ')
    frame.add(self.label,BorderLayout.NORTH)
    frame.pack()
    frame.setVisible(True)
    self.s = socket.socket()
    self.host = socket.gethostname()
    self.port = 12221
    self.s.connect((self.host, self.port))
    while True:
		self.list.getModel().addElement(self.s.recv(1024))

if __name__ == '__main__':
        #start things off.
        Client()