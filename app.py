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
userbase = db.child("account").get().val()
users = list(userbase.items())
#TODO : site, sign in and sign up option, seperate page for each when signed up is done checks if credentials are valid if they are redirect to sign in page, else bring an error message
#TODO 2: add form to intake information to the server
#fyi:: calling lst on the db returns a list of 2 things, [0]=UserID, [1] = type(dict) in the dict is the username/password
@app.route('/')
def index():
    return render_template("open.html")

@app.route('/signup', methods=['GET','POST'])
def sign_up():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #check if user exists in db 
        #Need to add redirect after post request to avoid resending the POST form again.
        for key, value in userbase.items():
            if value["password"] == password:
                print("Password: {} already exists in the database".format(password))
                return render_template("signup.html", method=['GET', 'POST'], error="Password already exists.")
            else:
                print(value["password"], password)
        #db.child("account").push({"username":username, "password":password}) #Adds user to database
    return render_template("signup.html", method=['GET', 'POST'], error="")
    

@app.route('/signin')
def sign_in():
    #check if user exists in db if he does allow him access to a closed site.
    return render_template("signin.html", method=['GET', 'POST'])

@app.route('/closed')
def closed():
    return render_template("closed.html", users=users)

if __name__ == "__main__":
	app.run(debug=True)

