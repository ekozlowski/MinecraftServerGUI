import tkinter as tk
from tkinter import Frame, Label, StringVar, OptionMenu

# Options that need text boxes:
# - level-name
# - level-seed
# - motd

options = {
    'difficulty': {
        'Peaceful': 0,
        'Easy': 1,
        'Normal': 2,
        'Hard': 3
    },
    'gamemode': {
        'Survival': 0,
        'Creative': 1,
        'Adventure': 2,
        'Spectator': 3
    },
    'generate-structures': {
        'Yes': 'true',
        'No': 'false'
    },
    'level-type' : {
        'Default': 'DEFAULT',
        'Flat': 'FLAT',
        'Large Biomes': 'LARGEBIOMES',
        'Amplified': 'AMPLIFIED',
        'Customized': 'CUSTOMIZED'
    },
    'pvp': {
        'Yes': 'true',
        'No': 'false'
    },
    'spawn-animals': {
        'Yes': 'true',
        'No': 'false'
    },
    'spawn-monsters': {
        'Yes': 'true',
        'No': 'false',
    },
    'spawn-npcs': {
        'Yes': 'true',
        'No': 'false'
    }
}

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.options = {}
        self.createWidgets()
        self.loadConfig()

    def loadConfig(self):
        data = open('C:/Users/Edward/Dropbox/minecraft/server/ann_server.properties', 'r').readlines()
        for line in data:
            if line.startswith('#'): continue
            key, value = line.strip().split('=')
            if key in options:
                self.options.get(key).set(value)

    def createWidgets(self):
        self.sayHi = tk.Button(self)
        self.sayHi["text"] = "Eds Button"
        self.sayHi["command"] = self.say_Hello
        self.sayHi.pack(side="bottom")
        
        for option in options:
            f = Frame(self)
            f.pack(side="bottom")
            Label(f, text=option).pack(side="left")
            v = StringVar(self)
            o = OptionMenu(f, v, *options.get(option).values())
            o.pack(side="right")
            self.options[option] = v

root = tk.Tk()
app = Application(master=root)
app.mainloop()