from flask import Flask, render_template, url_for, redirect, flash, session, request
from forms import userLoginForm, stockSearchForm
import os
from flask_sqlalchemy import SQLAlchemy
# from models import User
import sqlite3

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbPath = os.path.join(basedir, 'database.sqlite3')


########## For setting up the app environment ###########

# setting up SQlAlchemy only for easy setupDatabase.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
db = SQLAlchemy(app)
# csrf security
app.config['SECRET_KEY'] = 'topSecretKey'

# model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    def __init__(self, username, password, role='user'):
        self.username = username
        self.password = password
        self.role = role


# Stock model
class Stock(db.Model):
    __tablename__ = 'stock'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __init__(self, name, manufacturer, quantity, price):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.price = price

########## functions ##########
# connecting to local server
def getDbConnection():
    connection = sqlite3.connect(dbPath)
    connection.row_factory = sqlite3.Row
    return connection




########### views ###########

@app.route('/')
def index():
    title = "Home page"
    return render_template("index.html",title = title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = userLoginForm()
    
    # submit button functionality
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # reset the form fields
        form.username.data = ''
        form.password.data=''
        
        connection = getDbConnection()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = ''
        try:
            user = connection.execute(query).fetchone()
        except Exception as e:
            flash(f'Error encountered: {str(e)}')
            print(f"Error: {e}")
        connection.close()
        
        if user:
            session['username'] = user['username']
            session['role'] = user['role']
            
            flash(f"Welcome {user['username']}!", "success")
            return redirect(url_for('admin')) if session['role'] == "admin" else redirect(url_for('index'))
        
        else:
            flash(f'Invalid username or password! Try Again.')
    
    
    
    return render_template('login.html', form = form)
    

@app.route('/admin')
def admin():
    title = "Admin page"
    if 'username' in session and session['role'] == "admin":
        return render_template("admin.html", title = title) 
    else:
        flash("Unauthorized access to admin prevented!")
        return redirect(url_for('index'))

# Stock page route
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    title = "Stock"
    form = stockSearchForm()
    
    connection = getDbConnection()
    
    # when search is empty show everything
    query = "SELECT * FROM stock"

    if request.method == "POST" and form.validate_on_submit():
        search = form.searchQuery.data
        # searches the word for product name or manufacturer
        query = f"SELECT * FROM stock WHERE name LIKE '%{search}%' OR manufacturer LIKE '%{search}%'"
    
    try:
        stocks = connection.execute(query).fetchall()
        #stocks = connection.executescript(query).fetchall()
    except Exception as e:
        flash(f'Error encountered: {str(e)}')
        print(f"Error: {e}")
        stocks = []
    connection.close()
   
    if 'username' in session:
        return render_template('stock.html', title=title, form = form, stocks = stocks)
    else:
        flash("Please login to view stock!")
        return redirect(url_for('index'))
    
    #return render_template('stock.html', title = title, form = form, stocks = stocks)
    

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove 'username' from the session
    session.pop('role', None)
    
    flash("You have been logged out.")
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)    