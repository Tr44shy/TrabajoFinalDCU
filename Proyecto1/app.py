from flask import Flask
from flask import render_template, request, redirect, get_flashed_messages, flash
from flask_mysqldb import MySQL


app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sitio'
mysql.init_app(app)


@app.route('/')
def inicio():
    return render_template('Admin/Login.html')

@app.route('/login', methods= ["GET", "POST"])
def login():



    if request.method == 'POST':
        _user = request.form['txtuser']
        _password = request.form['txtpass']

        cur= mysql.connection.cursor()
        sql = "Selet * from users where correo = %s"
        datos = (_user)
        cur.execute(sql,datos)
        cur.commit()

        hola = 2
        if hola == 2:
            return redirect ("/Admin/")


@app.route('/Registro')
def registro():
    return render_template('Admin/Registro.html')

@app.route('/Libros')
def Libros():
    return render_template('Sitio/Libros.html')

@app.route('/Nosotros')
def Nosotros():
    return render_template('Sitio/Nosotros.html')

@app.route('/Admin/')
def Admin_Index():
    return render_template('Admin/Index.html')

@app.route('/Login')
def Admin_Login():
    return render_template('Admin/Login.html')

@app.route('/Admin/Libros/')
def Admin_Libros():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("Select * from `libros`")
    libros=cursor.fetchall()
    conexion.commit()
    print(libros)
    return render_template('Admin/Libros.html' ,Libros=libros)

@app.route('/Admin/Libros/Guardar', methods=['POST'])
def Admin_Libros_Guardar():
    _nombre=request.form['txtnamelibro']
    _img=request.files['imglibro']
    _url=request.form['txtUrl']

    conexion=mysql.connect()
    sql="INSERT INTO `libros` (`ID`, `Nombre`, `Imagen`, `Url`) VALUES ('NULL',%s,%s,%s);"
    datos=(_nombre,_img.filename,_url)
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit() 

    print(_nombre)
    print(_img)
    print(_url)
    
    return redirect('/Admin/Libros')

@app.route('/Admin/Registro/Guardar', methods=['POST'])
def Admin_Registro_Guardar():
    _nombre=request.form['txtnameuser']
    _img=request.files['imguser']
    _id=request.form['iduser']
    _correo=request.form['correouser']
    _pass=request.form['passuser']
    _telefono=request.form['teluser']

    conexion=mysql.connect()
    sql="INSERT INTO `users` (`IdUsers`, `Imagen`, `Id`, `Correo`, `Contrasena`, `Telefono`, `Nombre`) VALUES ('NULL',%s,%s,%s,%s,%s,%s);"
    datos=(_img.filename,_id, _correo, _pass, _telefono, _nombre)
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit() 

    print(_nombre)
    print(_img)
    print(_id)

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)