import string 
import couchdb 
from flask import * 
from Database import *
from Vehicle import *
from flask_sessionstore import Session

import json

app = Flask(__name__)
app.config.update(
    DATABASE = 'Arlton-Server'
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

@app.route("/handlers/test", methods=['GET', 'POST'])
def test():
    return jsonify("It Works!")


############################################################## Server Handlers ##############################################################

@app.route("/handlers/vehicle_update", methods=['GET', 'POST'])
def vehicle_update():
    global db
    dd = json.loads(request.form['data'])
    db.saveVehicleData(dd)
    return jsonify(dd)

if __name__ == '__main__':
   app.run()
