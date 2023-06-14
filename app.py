#importacion del framework
from flask import Flask
from flask_mysqldb import MySQL


#inicializacion del app
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)

#declaracion de ruta / http://localhost:5000
@app.route('/')
def index():
    return "Hola Mundo FLASK"

@app.route('/guardar')
def guardar():
    return "se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"

#ejecucion
if __name__ == '__main__':
    app.run(port=5000)