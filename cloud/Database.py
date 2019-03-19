import couchdb
import hashlib
import json
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self, url):
        self.db = couchdb.Server(url)
        return 

    def validateUser(self, uid, upass):
        d = self.db
        try: 
            h = d['users'][str(uid)]['password']
            if(check_password_hash(h, upass)):
                return True
            return False
        except:
            return False

    def makeUser(self, uid, upass):
        d = self.db 
        d['users'].save({"_id":str(uid),'password':generate_password_hash(upass)})
        return 

    def saveVehicleData(self, data):
        d = self.db 
        data['_rev'] = d['vehicles'][data['_id']]['_rev']
        d['vehicles'].save(data) 
        return True
        

    def getVehicle(self, vnum):
        d = self.db 
        try:
            a = json.dumps(d['vehicles'][str(vnum)])
            return a
        except:
            return None