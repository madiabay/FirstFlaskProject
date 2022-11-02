from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# DB configuration
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    if cursor.execute("INSERT INTO user(user_name) VALUES('Meirbek');"):
        cursor.connection.commit()
        return 'Success', 201
    # result_value = cursor.execute("SELECT * FROM user;")
    # if result_value > 0:
    #     users = cursor.fetchall()
    #     return str(users)
    return render_template('index.html')
    # return redirect(url_for('about'))

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/css/')
def css():
    return render_template('css.html')

# Для изучения POST и GET запроса
@app.route('/register/', methods=['get', 'post'])
def register():
    if request.method == 'POST':
        return request.form['password']
        # return 'Вы успешно зарегистрировались'
    return render_template('register.html')

# Custom errorhandler (ручная ошибка)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)