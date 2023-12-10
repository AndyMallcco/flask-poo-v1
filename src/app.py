from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOEmpleado import DAOEmpleado

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
db1 = DAOEmpleado()
ruta='/usuario'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route(ruta+'/')
# @app.route('/usuario/')
def index():
    data = db.read(None)

    return render_template('usuario/index.html', data = data)

@app.route(ruta+'/add/')
def add():
    return render_template('/usuario/add.html')

@app.route(ruta+'/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# ----------------------------------------------------------------

@app.route('/emp/')
# @app.route('/usuario/')
def index1():
    data = db1.read(None)

    return render_template('empleado/index.html', data = data)

@app.route('/emp'+'/add/')
def add1():
    return render_template('/empleado/add.html')

@app.route('/emp'+'/addempleado', methods = ['POST', 'GET'])
def addempleado():
    if request.method == 'POST' and request.form['save']:
        if db1.insert(request.form):
            flash("Nuevo empleado ingresado")
        else:
            flash("ERROR, al ingresar empleado")

        return redirect(url_for('index1'))
    else:
        return redirect(url_for('index1'))

@app.route('/emp'+'/update/<int:codigo>/')
def update1(codigo):
    data = db1.read(codigo);

    if len(data) == 0:
        return redirect(url_for('index1'))
    else:
        session['update'] = codigo
        return render_template('empleado/update.html', data = data)

@app.route('/emp'+'/updateempleado', methods = ['POST'])
def updateempleado():
    if request.method == 'POST' and request.form['update']:

        if db1.update(session['update'], request.form):
            flash('Se actualizó correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index1'))
    else:
        return redirect(url_for('index1'))

@app.route('/emp'+'/delete/<int:codigo>/')
def delete1(codigo):
    data = db1.read(codigo);

    if len(data) == 0:
        return redirect(url_for('index1'))
    else:
        session['delete'] = codigo
        return render_template('empleado/delete.html', data = data)

@app.route('/emp'+'/deleteempleado', methods = ['POST'])
def deleteempleado():
    if request.method == 'POST' and request.form['delete']:

        if db1.delete(session['delete']):
            flash('Empleado eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index1'))
    else:
        return redirect(url_for('index1'))
# -----------------------------------------------------------

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

# ---------------------------------------------------------------
if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
