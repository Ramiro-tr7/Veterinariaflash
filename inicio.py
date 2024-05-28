from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/animal1')
def animal1():
    return render_template("animal1.html")

@app.route('/animal2')
def animal2():
    return render_template("animal2.html")

@app.route('/animal3')
def animal3():
    return render_template("animal3.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")


#@app.route('/agrega_comenta', methods=['POST'])
#def agrega_comenta():
    #if request.method == 'POST':
        #aux_Correo = request.form['correo']
        #aux_Comentarios = request.form['comentarios']
        #conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        #cursor = conn.cursor()
        #cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        #conn.commit()
    #return redirect(url_for('home'))

@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='programacion', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentarios = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='programacion', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        corr=request.form['correo']
        come=request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='programacion', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update comenta set correo=%s, comentarios=%s where id=%s', (corr,come,id))
        conn.commit()
    return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='programacion', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='programacion', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('crud'))

if __name__ == "__main__":
    app.run(debug=True)
