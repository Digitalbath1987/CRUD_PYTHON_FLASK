from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(host="localhost",user="DigitalDB",password="123456",database="prueba")
cursor = midb.cursor(dictionary=True)


@app.route('/')
def hello():
    return "Hello World!"



@app.route('/post/<post_id>', methods=['GET','POST'])
def lala(post_id):
    if request.method == 'GET':
        return "el id del post es : " + post_id
    else:
        return "este es otro metodo y no get "



@app.route('/lele', methods=['POST','GET'])
def lele():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    #abort(403)
    #return redirect(url_for('lala',post_id=2))
    #print(request.form['llave1'])
    #return render_template('lele.html')
    return render_template('lele.html',usuarios = usuarios)


@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html', mensaje ='hola Mundito')



@app.route('/crear', methods=['POST','GET'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into usuario (username, email, edad) values(%s,%s,%s)"
        values = (username, email, edad)
        cursor.execute(sql,values)
        midb.commit()

        return redirect(url_for('lele'))
    return render_template('crear.html')




#levanta server Flask
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)