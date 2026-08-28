import json





class Memory: 
    def __init__(self):
        self.temporary = {}
        self.aliases = {}
        with open("data/aliases.json", "r") as file:
            self.aliases = json.load(file)

    def save_alias(self,alias,target):
        self.aliases[alias] = target    
        with open("data/aliases.json", "w") as file:
            json.dump(self.aliases, file,indent=4)


    def get_alias(self,alias):
        #get in dictionary prevents KeyError , if key doesnt exist.
        return self.aliases.get(alias)
    
    