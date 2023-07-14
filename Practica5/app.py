#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#inicializacion del app
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'dbflask'
mysql = MySQL(app)

#declaracion de ruta / http://localhost:5000 - tipo insert 
@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM albums')
    albums = CC.fetchall()
    CC.close()
    return render_template('index.html', listalbums=albums)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
       Titulo= request.form['txtTitulo']
       Artista= request.form['txtArtista'] 
       Año= request.form['txtAño']
       print(Titulo,Artista,Año)
       
       cursor = mysql.connection.cursor()
       cursor.execute('INSERT INTO albums (Titulo, Artista, Año) VALUES (%s, %s, %s)', (Titulo, Artista, Año))
       mysql.connection.commit()
       cursor.close()
        
    flash('Los datos se guardaron correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<int:Id>')
def editar(Id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('SELECT * FROM albums WHERE Id = %s', (Id,))
    album = cursorId.fetchone()
    cursorId.close()
    return render_template('editarAlbum.html', album=album)

@app.route('/eliminar/<int:Id>')
def eliminar(Id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM albums WHERE Id = %s', (Id,))
    mysql.connection.commit()
    cursorId.close()
    
    flash('Se eliminó el Álbum')
    return redirect(url_for('index'))

@app.route('/actualizar/<Id>', methods=['POST'])
def actualizar(Id):
    if request.method == 'POST':
        varTitulo = request.form['txtTitulo']
        varArtista = request.form['txtArtista']
        varAño = request.form['txtAño']
        
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE albums SET Titulo = %s, Artista = %s, Año = %s WHERE Id = %s', (varTitulo, varArtista, varAño, Id))
        mysql.connection.commit()
        curAct.close()
        
        flash('El álbum se actualizó correctamente: ' + varTitulo)
        return redirect(url_for('index'))

#ejecucion
if __name__ == '__main__':
    app.run(port=5000)