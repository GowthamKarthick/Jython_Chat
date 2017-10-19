import socket
import threading
import time

from javax.swing import *
from java.awt import *

class Server:

  def Send(self,event):
    q = self.textfield.text    
    self.list.getModel().addElement('you:'+q)#add the sending text in our own list
    self.c.send(q)#send the text

  def __init__(self):
    frame = JFrame("Chat application(Server)")
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
    self.s.bind((self.host, self.port))
    self.s.listen(5)
    self.c = None
    while True:
    	if self.c is None:
    		self.c, addr = self.s.accept()
    		print 'From', addr
    	else:    	
    		self.list.getModel().addElement(self.c.recv(1024)) #receive the text add in list
    		
    		

if __name__ == '__main__':        
        Server()
