import os, pyrebase
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = os.urandom(16).hex()

config = {
    "apiKey": "AIzaSyDDcL0pFjECQ-0j-1hgPFwLFrMnrUVT5SQ",
    "authDomain": "vefthr3-firebase.firebaseapp.com",
    "databaseURL": "https://vefthr3-firebase.firebaseio.com",
    "projectId": "vefthr3-firebase",
    "storageBucket": "vefthr3-firebase.appspot.com",
    "messagingSenderId": "459938427281",
    "appId": "1:459938427281:web:7b80b54378cc611a6dea30",
    "measurementId": "G-T1M5ZMHXXF"
}
fb = pyrebase.initialize_app(config)
db = fb.database()
userbase = db.child("account").get().val() 

if userbase == None: # Avoids crashing if db is empty
    userbase = {}
users = list(userbase.items())

def signup_check(username):
    for key,value in userbase.items():
        if value["username"] == username:
            return False
    return True

def login_check(username, password):
    userData = {}
    
    for key,value in userbase.items():
        if value["username"] == username:
            userData["user_id"] = key
            userData["username"] = username
            userData["password"] = password
            return userData
    return False

@app.route('/')
def index():
    return redirect(url_for("signup"))

#-----------------Sign up-----------------
#Maybe rename signup to account or something of the sort
@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if signup_check(username) == False:
            error = 'Invalid credentials'
        elif signup_check(username) == True:
            db.child("account").push({"username":username, "password":password})
            return redirect(url_for('login'))
    return render_template("signup.html", error=error)  

#-----------------Login-----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_check(username, password) != False:
            session["user_session"] = login_check(username,password)
            return redirect(url_for("closed"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

#-----------------Closed site-----------------
@app.route('/closed', methods=['POST', 'GET'])
def closed():
    name = None
    if "user_session" in session:
        name = session["user_session"]["username"]
        if request.method == 'POST':
            if "user_session" in session:
                session.pop("user_session", None)
                return redirect(url_for("login"))
        return render_template("closed.html", name=name)
    return(render_template("403.html"), 403)

@app.errorhandler(403)
def access_denied(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("closed"))
if __name__ == "__main__":
	app.run(debug=True)

