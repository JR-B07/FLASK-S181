#importacion del framework
from flask import Flask,render_template,request
from flask_mysqldb import MySQL


#inicializacion del app
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)

#declaracion de ruta / http://localhost:5000 - tipo insert 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
       titulo= request.form['txtTitulo']
       artista= request.form['txtArtista'] 
       anio= request.form['txtAnio']
       print(titulo,artista,anio)
         
    return "Los datos llegaron"

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"

#ejecucion
if __name__ == '__main__':
    app.run(port=5000)