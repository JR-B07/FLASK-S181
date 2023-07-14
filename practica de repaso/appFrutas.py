from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='db_fruteria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#declaracion de las rutas

#declaracion de la ruta al local host
@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM tbfrutas1')
    conFruta = CC.fetchall() 
    print (conFruta)
    return render_template('index.html', Listafrutas=conFruta)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Fruta = request.form['txtFruta']
        Temporada = request.form['txtTemporada']
        Precio = request.form['txtPrecio']
        Stock = request.form['txtStock']
        print(Fruta, Temporada, Precio, Stock)

        # Conectar a la base de datos
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO tbfrutas1 (Fruta, Temporada, Precio, Stock) VALUES (%s, %s, %s, %s)', (Fruta, Temporada, Precio, Stock))
        mysql.connection.commit()

    flash('El registro fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('DELETE FROM tbfrutas1 WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Se eliminó el registro')
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    cursorID = mysql.connection.cursor()
    cursorID.execute('SELECT * FROM tbfrutas1 WHERE id = %s', (id,))
    consultaID = cursorID.fetchone()

    return render_template('editarRegistro.html', tbfrutas1=consultaID)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varFruta = request.form['txtFruta']
        varTemporada = request.form['txtTemporada']
        varPrecio = request.form['txtPrecio']
        varStock = request.form['txtStock']

        cursorAct = mysql.connection.cursor()
        cursorAct.execute('UPDATE tbfrutas1 SET Fruta = %s, Temporada = %s, Precio = %s, Stock = %s WHERE id = %s', (varFruta, varTemporada, varPrecio, varStock, id))
        mysql.connection.commit()

    flash('Se actualizó el registro ' + varFruta)
    return redirect(url_for('index'))


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000, debug=True)
