''' 
CRUD Web de contactos, aplicacion desarrollada con Python, framework Flask
y base de datos SqLite3, ORM SQLAlchemy

modulos usados: flask, Flask-SQLAlchemy

Crear en prompt la base de datos: sqlite3 database/client.db, esto abre el editor para sqlite>
con el comando .databases se crea la db en el proyecto.
'''
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/client.db' #ruta de la DB, si es 
# requerido cambiar
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(200))
    name = db.Column(db.String(200))
    phone = db.Column(db.String(50))


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', list_users = users)

@app.route('/add_user', methods = ['POST'])
def add_user():
    user = User(user = request.form['User'], name =  request.form['Name'], phone = request.form['Phone']) #Uso de la class
    db.session.add(user) # Agrega el usuario con SQLAlchemy
    db.session.commit() 
    return redirect(url_for('index'))

@app.route('/consult/<id>')
def consultUser(id):
   user = User.query.filter_by(id = int(id)).first()
   
   db.session.commit()
   return render_template('consult.html', user = user)

@app.route('/delete/<id>')
def deleteUser(id):
    User.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 4000, threaded=True, debug=True) # Red host='192.168.0.99'