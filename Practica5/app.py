#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
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
    CC= mysql.connection.cursor()
    CC.execute('select * from albums')
    conalbums=CC.fetchall()
    print(conalbums)
    return render_template('index.html', listalbums= conalbums)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
       Titulo= request.form['txtTitulo']
       Artista= request.form['txtArtista'] 
       Anio= request.form['txtAnio']
       print(Titulo,Artista,Anio)
    return "Los datos llegaron"

@app.route('/editar/<Id>')
def editar(Id):
    cursorId= mysql.connection.cursor()
    cursorId.execute('select * from albums where Id= %s', (Id,))
    consulId= cursorId.fetchone()
    print(consulId)
    return render_template('editarAlbum.html', album = consulId)

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"

@app.route('/actualizar/<Id>', methods=['POST'])
def actualizar(Id):
    if request.method == 'POST':
        varTitulo= request.form['txtTitulo']
        varArtist= request.form['txtArtist']
        varAnio= request.form['txtAnio']
        
        curAct= mysql.connection.cursor()
        curAct.execute('Update albums set Titulo= %s, Artista= %s, Anio= %s' WHERE Id=%s(varTitulo,varArtist,varAnio,Id))
        mysql.connection.commit()
    flash('Se actualizo el Album'+ varTitulo)
    return redirect(url_for('index'))

#ejecucion
if __name__ == '__main__':
    app.run(port=5000)