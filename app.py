from flask import Flask, render_template, request
from pyrebase import pyrebase

app = Flask(__name__)

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
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

#TODO : site, sign in and sign up option, seperate page for each when signed up is done checks if credentials are valid if they are redirect to sign in page, else bring an error message
#TODO 2: add form to intake information to the server
#fyi:: calling lst on the db returns a list of 2 things, [0]=UserID, [1] = type(dict) in the dict is the username/password
@app.route('/')
def index():
    return render_template("open.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/closed')
def lesa():
    u = db.child("notandi").get().val()
    users = list(u.items())
    return render_template("closed.html", users=users)

if __name__ == "__main__":
	app.run(debug=True)

# skrifum nýjan í grunn hnútur sem heitir notandi 
# db.child("notandi").push({"notendanafn":"dsg", "lykilorð":1234}) 

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())