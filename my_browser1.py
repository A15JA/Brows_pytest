"""
###########      Problem Statement    ##################
Task: Create Your Own Browser Using Python
The task involves building a simple browser using Python libraries like PyQt5 and
PyQtWebEngine. The browser should display web pages, handle navigation (back, forward),
and include a search/address bar for URL input.
"""

import sys
from PyQt5.QtCore import QUrl  # Core functionality for handling URLs
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit  # GUI components
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Web engine to render/make web pages
from PyQt5.QtGui import QIcon  # To add icons for buttons

# Main window class for the browser
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the parent class (QMainWindow)

        # Set up the browser widget
        self.browser = QWebEngineView()  # Create a web view widget
        self.browser.setUrl(QUrl('http://google.com'))  # Set the default homepage to Google
        self.setCentralWidget(self.browser)  # Make the browser the central widget of the window
        self.showMaximized()  # Open the window in maximized mode

        # Create a navigation toolbar
        navbar = QToolBar()  # Toolbar for navigation buttons
        self.addToolBar(navbar)  # Add the toolbar to the main window

        # Add navigation buttons with icons
        back_btn = QAction(QIcon("back.png"), "Back", self)  # Back button with icon
        back_btn.triggered.connect(self.browser.back)  # Connect to browser's back function
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon("forward.png"), "Forward", self)  # Forward button with icon
        forward_btn.triggered.connect(self.browser.forward)  # Connect to browser's forward function
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon("reload.png"), "Reload", self)  # Reload button with icon
        reload_btn.triggered.connect(self.browser.reload)  # Connect to browser's reload function
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon("home.png"), "Home", self)  # Home button with icon
        home_btn.triggered.connect(self.navigate_home)  # Connect to custom home navigation function
        navbar.addAction(home_btn)

        # Add a URL bar for entering web addresses
        self.url_bar = QLineEdit()  # Text input for URLs
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # Navigate to URL when Enter is pressed
        navbar.addWidget(self.url_bar)  # Add URL bar to the toolbar

        # Update the URL bar when the browser navigates to a new page
        self.browser.urlChanged.connect(self.update_url)

    # Navigate to the homepage (Google)
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    # Navigate to the URL entered in the URL bar
    def navigate_to_url(self):
        url = self.url_bar.text()  # Get the URL from the text box
        self.browser.setUrl(QUrl(url))  # Navigate to the entered URL

    # Update the URL bar when the page changes
    def update_url(self, q):
        self.url_bar.setText(q.toString())  # Update the URL bar with the current page's URL

# Main application setup
app = QApplication(sys.argv)  # Create the application instance
QApplication.setApplicationName("Python Backed Browser")  # Set the application name

# Create and display the main window
window = MainWindow()  # Instantiate the main window
app.exec_()  # Start the application event loop (keeps the window open)
