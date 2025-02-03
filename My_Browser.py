"""
###########      Problem Statemet    ##################
Task: Create Your Own Browser Using Python
The task to create your own browser using Python has been assigned. The task
involves building a simple browser using Python libraries like PyQt5 and
PyQtWebEngine, which will allow you to display web pages, handle navigation
(back, forward), and integrate a search/address bar for URL input.
"""


import sys
from PyQt5.QtCore import *  # Importing core functionality for PyQt5
from PyQt5.QtWidgets import *  # Importing GUI widgets from PyQt5
from PyQt5.QtWebEngineWidgets import *  # Importing web engine widgets for embedding a browser

# Defining the main window class for the browser
class MainWindow(QMainWindow): #This defines a class MainWindow, which inherits from QMainWindow, the main window type in PyQt5.
    def __init__(self): #constructor method of oops
        super(MainWindow, self).__init__() #super(MainWindow, self).__init__() is used to call the parent class (QMainWindow) constructor
        
        # Creating a web browser widget
        self.browser = QWebEngineView() # # Creates a browser widget
        self.browser.setUrl(QUrl('http://google.com'))  # Setting the default homepage to Google
        self.setCentralWidget(self.browser)  # Setting the browser as the central widget
        self.showMaximized()  # Opening the browser in maximized mode
        
        # Adding a navigation bar
        navbar = QToolBar() # Creates a navigation toolbar
        self.addToolBar(navbar)  # Adds the toolbar to the main window
        
        # Adding a 'Back' button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)  # Connects button to browser's back function
        navbar.addAction(back_btn)
        
        # Adding a 'Forward' button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)  # Connects button to browser's forward function
        navbar.addAction(forward_btn)        
        
        # Adding a 'Reload' button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)  # Connects button to browser's reload function
        navbar.addAction(reload_btn)        

        # Adding a 'Home' button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)  # Connects button to home navigation function
        navbar.addAction(home_btn)
        
        # Adding a URL bar (text input for entering URLs)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # Navigates to entered URL when Enter is pressed
        navbar.addWidget(self.url_bar) # Adds URL bar to the toolbar
        
        # Updating the URL bar when the browser navigates to a new page
        self.browser.urlChanged.connect(self.update_url)
    
    # Function to navigate to the homepage (Google)
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
    
    # Function to navigate to the URL entered in the URL bar
    def navigate_to_url(self):
        url = self.url_bar.text()  # Getting the URL from the text box
        self.browser.setUrl(QUrl(url))  # Setting the browser to navigate to the entered URL
        
    # Function to update the URL bar when a new page is loaded
    def update_url(self, q):
        self.url_bar.setText(q.toString())  # Updates the text in the URL bar
        
# Creating the application instance
app = QApplication(sys.argv) # Creates the application
QApplication.setApplicationName("Python Backed Browser")  # Setting the application name

# Creating and displaying the main window
window = MainWindow()  # Creates the main window
app.exec_()  # Running the application event loop(use to hold the window), else window will be closed
