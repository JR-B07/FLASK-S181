from flask import Flask,render_template,request
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='db_flores'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    CC= MySQL.connection.cursor()
    CC.execute('select * from tb_Flores')
    conflores=CC.fetchall()
    print(conflores)
    return render_template('index.html', listaflores= conflores)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
       Nombre= request.form['Nombre']
       Cantidad= request.form['Cantidad'] 
       Precio= request.form['Precio']
       print(Nombre,Cantidad,Precio)
    return "Los datos llegaron"

@app.route('/editar/<id>')
def editar(id):
    cursorid= MySQL.connection.cursor()
    cursorid.execute('select * from tb_flores where id= %s', (id,))
    consulid= cursorid.fetchone()
    print(consulid)
    return render_template('editarFlor.html', Flor = consulid)


#ejecucion
if __name__ == '__main__':
    app.run(port=5000)
