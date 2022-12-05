import sys

import self as self
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtWebEngineWidgets import  *


class MainWindow(QMainWindow):
    def __init__(self):
      super(MainWindow, self).__init__()
      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('https://whoogle-search.everythingfor2.repl.co'))
      self.setCentralWidget(self.browser)
      self.showMaximized()

      # NavBar
      navBar= QToolBar()
      self.addToolBar(navBar)


      back_btn = QAction('Back', self)
      back_btn.triggered.connect(self.browser.back)
      navBar.addAction(back_btn)

      forward_btn=QAction('Forward', self)
      forward_btn.triggered.connect(self.browser.forward)
      navBar.addAction(forward_btn)

      reload_btn = QAction('Reload', self)
      reload_btn.triggered.connect(self.browser.reload)
      navBar.addAction(reload_btn)

      home_btn = QAction('Home', self)
      home_btn.triggered.connect(self.navigate_home)
      navBar.addAction(home_btn)

      self.url_bar = QLineEdit()
      self.url_bar.returnPressed.connect(self.navigate_to_url)
      navBar.addWidget(self.url_bar)

      support_btn = QAction('Support Us', self)
      support_btn.triggered.connect(self.support_btn)
      navBar.addAction(support_btn)

      self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
       self.browser.setUrl(QUrl('https://whoogle-search.everythingfor2.repl.co'))

    def support_btn(self):
       self.browser.setUrl(QUrl('https://pages.razorpay.com/pl_HqEs5KZyzOT3RW/view'))

    def navigate_to_url(self):
      Url = self.url_bar.text()
      self.browser.setUrl(QUrl(Url))

    def update_url(self, q):
      self.url_bar.setText(q.toString())




app=QApplication(sys.argv)
QApplication.setApplicationName("Krishna's Browser")
window = MainWindow()
app.exec_()
