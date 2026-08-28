import json

class Appregistry : 
    def __init__(self):
        self.apps = {}
        with open("data/apps.json","r") as file :
            self.apps = json.load(file)
        
    def get_command(self,app):
        return self.apps.get(app)
    def get_apps(self):
        return self.apps.keys()
    