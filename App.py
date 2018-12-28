from flask  import Flask,render_template, request,redirect, url_for,flash
from flask_mysqldb import MySQL
import logging



app = Flask (__name__)

#conexiones para Mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Felipe1991.'
app.config['MYSQL_DB'] = 'flaskproduct'
mysql = MySQL(app)

#configuracion de sesiones
app.secret_key='maysecretkey'

@app.route('/')
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('index.html', productos = data)

@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method=='POST':
        Producto=request.form['Producto']
        Unidades=request.form['Unidades']
        Precio=request.form['Precio']
        print(Producto)
        print(Unidades)
        print(Precio)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos(Producto,Unidades,Precio) VALUES (%s,%s,%s)',
        (Producto,Unidades,Precio))
        mysql.connection.commit()
        flash('Se ha registrado el producto con exito')
        return redirect(url_for('Index'))
    

@app.route('/edit/<id>')
def get_product(id):
    logging.debug("Eston debug message")          
    cur = mysql.connection.cursor()
    cur.execute ('SELECT * FROM productos WHERE id = (id)')
    data = cur.fetchall()
    print(data)
    return render_template('editar-producto.html', producto = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        Producto = request.form['Producto'] 
        Unidades = request.form['Unidades'] 
        Precio = request.form['Precio']
        cur=mysql.connection.cursor()
        cur.execute("""
        UPDATE productos
        set Producto=%s,
            Unidades=%s,
            Precio=%s
        WHERE id=%s
        """,(Producto,Unidades,Precio,id))
        mysql.connection.commit()
        flash('El inventario se actualizo correctamente')
        return redirect(url_for('Index'))
    

@app.route('/delete/<string:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El producto se elimino correctamente.')
    return redirect(url_for('Index'))
    

if __name__== "__main__":
    app.run(port=3000, debug=True )

