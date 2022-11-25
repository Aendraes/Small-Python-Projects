import pyperclip, keyboard
import time, json
from datetime import datetime
import os
# TODO Make object oriented, create a class to envelop the program as it is right now and make it function.
class multiclipboard():
    def __init__(self, json_name='clipboard.json'):
        self.listObj=[]
        self.json_name = json_name
        self.now = datetime.now()
        self.clipdict = dict()
    def newfile(self):
        if not os.path.isfile(self.json_name):
            x=open(self.json_name, 'x')
            x.close()
            x=open(self.json_name, 'w')
            json.dump(self.listObj, x,
                            indent=4,
                            separators=(',', ': '))
            x.close()
    def load_file(self):
        self.newfile()
        with open(self.json_name) as fp:
            self.listObj = json.load(fp)

    

if __name__ == '__main__':
    x=multiclipboard()
    while True:
        x.listObj = []
        x.clipdict = dict()
        x.now = datetime.now()
        if keyboard.is_pressed('ctrl+c'):
            x.load_file()
            time.sleep(0.2)
            x.clipdict['text'] = pyperclip.paste()
            x.clipdict['time'] = x.now.strftime("%d/%m/%Y %H:%M:%S")
            x.listObj.append(x.clipdict)
            print(x.listObj)
            with open(x.json_name, 'w') as json_file:
                json.dump(x.listObj, json_file,
                        indent=4,
                        separators=(',', ': '))


        # Create a new keybind to print the Json list. ctrl+b
        elif keyboard.is_pressed('ctrl+b'):
            x.load_file()
            time.sleep(0.2)
            copylist = []
            print(x.listObj)
            for item in x.listObj:
                copylist.append(item.get("text"))
            pyperclip.copy(f"{copylist}")
            keyboard.press(('ctrl+v'))

        # Create another new keyboard m for menu to choose new json.b
        elif keyboard.is_pressed('ctrl+m'):
            x.load_file()
            print('m clicked down')
            time.sleep(0.5)
        keyboard.read_key()