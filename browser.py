import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.example.com"))

        self.setCentralWidget(self.browser)

        # Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        forward_btn = QAction("Forward", self)
        forward_btn.setStatusTip("Forward to next page")
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home Button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go to home page")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update URL Bar
        self.browser.urlChanged.connect(self.update_urlbar)

        # Stop Button
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Full Screen Button
        full_screen_btn = QAction("Full Screen", self)
        full_screen_btn.setStatusTip("Toggle full screen")
        full_screen_btn.triggered.connect(self.toggle_fullscreen)
        navbar.addAction(full_screen_btn)

        # Show the browser window
        self.showMaximized()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.example.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

app = QApplication(sys.argv)
QApplication.setApplicationName("Simple Browser")
window = Browser()
app.exec_()
