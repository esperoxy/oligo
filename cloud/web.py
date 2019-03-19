import string 
import couchdb 
from flask import * 
from Database import *
from Vehicle import *
from flask_sessionstore import Session

app = Flask(__name__)
app.config.update(
    DATABASE = 'Arlton'
)
SESSION_TYPE = "filesystem"
#db = couchdb.Server("http://localhost:5984/")[app.config["DATABASE"]]
global db
global login 
global vinfo

db = Database("http://admin:ashish@localhost:5984")
login = False
vinfo = None

# Set the secret key to some random bytes. Keep this really secret!
import os 
import random
app.secret_key = os.urandom(32)#bytes(str(hex(random.getrandbits(128))), 'ascii')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("/404.html")

@app.route("/", methods=["GET", "POST"])
def index():
    global db
    if "login" in session:
        return dashboard()
    if request.method == "POST":
        try:
            uid = request.form['login']
            upass = request.form['password']
            if db.validateUser(uid, upass):
                session["login"] = uid
                return render_template("/dashboard.html")
            else:
                return "Incorrect Username/Password"
        except Exception as ex:
            print(ex)
            return render_template("/500.html")
    return render_template("/index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global db
    if "login" in session:
        if request.method == "POST":
            try:
                vnum = request.form['number']
                a = db.getVehicle(vnum)
                if a:
                    vinfo = Vehicle(a)
                    
            except Exception as ex:
                print(ex)
                return render_template("/500.html")   
            return render_template("/dashboard.html", milage = vinfo.values['milage'], fuel = vinfo.values['fuel'], total_distance = vinfo.values['total_distance'], vnum = vinfo.values['vnum'], total_tires = vinfo.values['total_tires'], tires = json.dumps(vinfo.tires))
        return render_template("/dashboard.html")
    else:
        return render_template("/index.html") #Fool them, they would think it dosen't exist until they log in


@app.route("/showall", methods=['GET', 'POST'])
def showall():
    global db 
    if "login" in session:
        try:
            render_template("/showall.html")
        except Exception as ex:
            return jsonify(ex)

if __name__ == '__main__':
   app.run()
