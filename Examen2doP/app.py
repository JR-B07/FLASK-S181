from flask import Flask, render_template,request, flash, redirect, url_for
from flask_mysqldb import MySQL

# Inicialización del APP
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'db_floreria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_flores')
    flores = cursor.fetchall()
    print(flores)
    return render_template('index.html', listaflores=flores)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        varNombre = request.form['Nombre']
        varCantidad = request.form['Cantidad']
        varPrecio = request.form['Precio']
        print(varNombre, varCantidad, varPrecio)
        cursor = mysql.connection.cursor()
        cursor.execute('insert into tb_flores values (Nombre = %s, Cantidad = %s, Precio = %s)', (varNombre, varCantidad, varPrecio, id))
        mysql.connection.commit()
        cursor.close()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_flores WHERE id = %s', (id,))
    flor = cursor.fetchone()
    print(flor)
    return render_template('editarFlor.html', Flor=flor)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tb_flores WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()

    flash('Se eliminó la Flor')
    return redirect(url_for('index'))

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varNombre = request.form['Nombre']
        varCantidad = request.form['Cantidad']
        varPrecio = request.form['Precio']

        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE tb_flores SET Nombre = %s, Cantidad = %s, Precio = %s WHERE id = %s', (varNombre, varCantidad, varPrecio, id))
        mysql.connection.commit()
        cursor.close()

        flash('El flores se actualizó correctamente: ' + varNombre)
        return redirect(url_for('index'))

# Ejecución
if __name__ == '__main__':
    app.run(port=5000)
    app.debug