import socket
import threading
from javax.swing import *
from java.awt import *

class Client:

  def Send(self,event):
  	z=self.textfield.text
  	self.list.getModel().addElement('you:'+z) #add the sending text in our own list
  	self.s.send(z)#send the text

  def __init__(self):
    frame = JFrame("Chat Application(Client)")
    frame.setSize(200, 225)
    frame.setLayout(BorderLayout())
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)

    self.list = JList(DefaultListModel())
    spane = JScrollPane()
    spane.setPreferredSize(Dimension(100,125))
    spane.getViewport().setView((self.list))
    self.textfield=JTextField('',50)
    label1=JLabel('Enter the text')
    panel = JPanel()
    panel.add(spane)
    panel.add(label1)
    panel.add(self.textfield)
    frame.add(panel,BorderLayout.CENTER)
    
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
		self.list.getModel().addElement(self.s.recv(1024)) #receive the text add in list

if __name__ == '__main__':
        
        Client()
