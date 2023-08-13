import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # FullScreen
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.browser.page().fullScreenRequested.connect(self.fullScreen)

        # Navbar
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        # Back Button
        self.backButton = QAction("Back", self)
        self.backButton.triggered.connect(self.browser.back)
        self.navbar.addAction(self.backButton)

        # Forward Button
        self.forwardButton = QAction("Forward", self)
        self.forwardButton.triggered.connect(self.browser.forward)
        self.navbar.addAction(self.forwardButton)

        # Reload Button
        self.reloadButton = QAction("Reload", self)
        self.reloadButton.triggered.connect(self.browser.reload)
        self.navbar.addAction(self.reloadButton)

        # Home Button
        self.homeButton = QAction("Home", self)
        self.homeButton.triggered.connect(self.home)
        self.navbar.addAction(self.homeButton)

        # Url Bar
        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        self.navbar.addWidget(self.urlBar)

        # Update Url
        self.browser.urlChanged.connect(self.updateUrl)

        self.showMaximized()

    def home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigateToUrl(self):
        self.url = self.urlBar.text()
        if (not self.url.startswith("https://") or self.url.startswith("http://") in self.url or self.url.startswith("file:///")):
            self.url = f"https://{self.url}"
        self.browser.setUrl(QUrl(self.url))

    def updateUrl(self, url):
        self.urlBar.setText(url.toString())

    @pyqtSlot("QWebEngineFullScreenRequest")
    def fullScreen(self, request):
        request.accept()
        if (request.toggleOn()):
            self.browser.setParent(None)
            self.browser.showFullScreen()
        else:
            self.setCentralWidget(self.browser)
            self.browser.showNormal()



app = QApplication(sys.argv)
QApplication.setApplicationName("Ahmed Browser")
window = MainWindow()
app.exec_()
