#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

__app_name__ = "Nombre"

# creando clase principal
class MainWindow(QMainWindow):
 
    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
 
        # creando QWebEngineView
        self.browser = QWebEngineView()

        """
        -----------------------------------------------------------------
        página inicial
        -----------------------------------------------------------------
        """
        # creando url base
        html = """
        <!DOCTYPE HTML>
            <html>
                <head>
                    <title>Nombre</title>
                </head>
                <body>
                <style>
                    *{
                    font-family: Arial;
                    }
                </style>
                    <h1>Aqui va la pagina principal</h1>
                </body>
            </html>
        """

        # Asignamos el cuerpo HTML
        self.browser.setHtml(html)

        # agregar acción cuando se cambia la URL
        self.browser.urlChanged.connect(self.update_urlbar)
 
        # agregar acción cuando finaliza la carga
        self.browser.loadFinished.connect(self.update_title)
 
        # configurar este navegador como widget central o ventana principal
        self.setCentralWidget(self.browser)

        # crear un objeto de la barra de estado
        self.status = QStatusBar()

        # agregar barra de estado a la ventana principal
        self.setStatusBar(self.status)

        # accion mientras carga la pagina
        self.browser.loadProgress.connect(self.updateProgressBar)

        """
        -----------------------------------------------------------------
        barra de navegación
        -----------------------------------------------------------------
        """
        #crear barra de navegación
        navbar = QToolBar("Barra de navegación", self)
        navbar.setStyleSheet("background-color: #3b4252;")
        navbar.setContextMenuPolicy(Qt.PreventContextMenu)

        self.addToolBar(navbar)

        """
        -----------------------------------------------------------------
        botón de atras
        -----------------------------------------------------------------
        """
        # agregar acciones a la barra de herramientas
        # creando una acción para volver
        back_btn = QAction(QIcon("back.png"), "aaa", self, )

        # agregando acción a la parte de atrás
        # hacer que el navegador retroceda
        back_btn.triggered.connect(self.back)

        navbar.addAction(back_btn)

        """
        -----------------------------------------------------------------
        botón de adelante
        -----------------------------------------------------------------
        """
        # creando una acción para adelante
        forward_btn = QAction(QIcon("forward.png"), "", self, )

        # agregando acción a la parte de atrás
        # hacer que el navegador retroceda
        forward_btn.triggered.connect(self.browser.forward)

        navbar.addAction(forward_btn)

        """
        -----------------------------------------------------------------
        botón de actualizar
        -----------------------------------------------------------------
        """
        # creando una acción para actualizar
        reload_btn = QAction(QIcon("refresh.png"), "", self, )

        reload_btn.triggered.connect(self.browser.reload)

        navbar.addAction(reload_btn)


        """
        -----------------------------------------------------------------
        botón de home
        -----------------------------------------------------------------
        """
        # creando una acción para volver a la pagina principal
        home_btn = QAction(QIcon("home.png"), "", self, )

        # agregando acción a la parte de atrás
        # hacer que el navegador retroceda
        home_btn.triggered.connect(self.browser.reload)

        navbar.addAction(home_btn)


        """
        -----------------------------------------------------------------
        barra de búsqueda
        -----------------------------------------------------------------
        """
        # creando la barra de búsqueda
        self.inputsearch = QLineEdit(self)

        self.inputsearch.setPlaceholderText("Busca con google o ingresa la dirección...")
        self.inputsearch.setStyleSheet("background-color: #1a2233; color: #fff; padding: 10px")
 
        # agregar acción cuando se presiona la tecla de "enter"
        self.inputsearch.returnPressed.connect(self.navigate_to_url)
 
        # agregando esto a la barra de herramientas
        navbar.addWidget(self.inputsearch)

        # mostrando todos los componentes
        self.show()

    # función para navegar a una url
    def navigate_to_url(self):
        # obtener url y convertirlo en objeto QUrl
        q = QUrl(self.inputsearch.text())

        # si el esquema está en blanco
        if q.scheme() == "":
            # establecer el esquema de URL en html
            q.setScheme("http")
 
        # establecer la url en el navegador
        self.browser.setUrl(q)

    #actualizar título
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - dload" % title)

    # método para actualizar url
    # este método es llamado por el objeto QWebEngineView
    def update_urlbar(self, q):
        current_url = self.inputsearch.text()

        if not current_url == "":
            # establecer texto en la barra de URL
            self.inputsearch.setText(q.toString())

            # establecer la posición del cursor de la barra de URL
            self.inputsearch.setCursorPosition(0)

        # Actualizamos el valor de la barra de progreso
    def updateProgressBar(self, event):
        pass

    #funcion para volver
    def back(self):
        self.browser.back()

if __name__ == "__main__":
    # creando una aplicación pyQt5
    app = QApplication(sys.argv)

    # establecer el nombre de la aplicación
    app.setApplicationName(__app_name__)

    # creando un objeto de ventana principal
    window = MainWindow()

    # ejecutar la aplicacion
    sys.exit(app.exec_())