import couchdb
from werkzeug.security import generate_password_hash, check_password_hash

db = couchdb.Server("http://admin:ashish@localhost:5984/")
d = db.create("users")
d.save({"_id":"admin", "password" : generate_password_hash("admin"), "type":"admin"})

d = db.create('vehicles')
d.save({'_id':'12345', 'milage':20, 'fuel':45, 'total_distance':12350, 'vnum':12345, 'total_tires':4, 'tires':{'1':120, '2':213, '3':4230, '4':4650}})
