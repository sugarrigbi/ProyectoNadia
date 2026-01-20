from flask_mysqldb import MySQL

class ConexionDB:
    def __init__(self, app):
        self.mysql = app 
        
        if app:
            self.init_app(app)
            
    def init_app(self, app):
        #Configuracion De La conexion
        app.config['MYSQL_HOST'] ='Localhost'
        app.config['MYSQL_USER'] ='ROOT'
        app.config['MYSQL_PASSWORD'] =''
        app.config['MYSQL_DB'] ='tareas'
        
        self.mysql = MySQL(app)
    