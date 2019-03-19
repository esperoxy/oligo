import json

class Vehicle:
    def __init__(self, data = None):
        if(data):
            self.values = json.loads(data)
            self.tires = self.values['tires']
        else:
            self.values = {'milage':20, 'fuel':0, 'total_distance':0, 'vnum':0, 'total_tires':0, 'tires':{'1':0, '2':0, '3':0, '4':0}}
            self.tires = self.values['tires']
        self.genDump()
        return 

    def genDump(self):
        d = json.dumps(self.values)
        d += '\n' + json.dumps(self.tires)
        self.dump = d
        return d
