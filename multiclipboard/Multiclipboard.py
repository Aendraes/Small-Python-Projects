import pyperclip, keyboard
import time, json
from datetime import datetime
import os

listObj = []
json_name = 'clipboard.json'
if not os.path.isfile(json_name):
    x=open(json_name, 'x')
    x=open(json_name, 'w')
    json.dump(listObj, x,
                      indent=4,
                      separators=(',', ': '))
    x.close()
def load_file():
    with open(json_name) as fp:
        listObj = json.load(fp)
    return listObj

while True:
    listObj = []
    now = datetime.now()
    clipdict = dict()
    if keyboard.is_pressed('ctrl+c'):
        listObj = load_file()
        time.sleep(0.2)
        clipdict['text'] = pyperclip.paste()
        clipdict['time'] = now.strftime("%d/%m/%Y %H:%M:%S")
        listObj.append(clipdict)
        print(listObj)
        with open(json_name, 'w') as json_file:
            json.dump(listObj, json_file,
                      indent=4,
                      separators=(',', ': '))


    # Create a new keybind to print the Json list. ctrl+b
    elif keyboard.is_pressed('ctrl+b'):
        listObj = load_file()
        time.sleep(0.2)
        copylist = []
        for line in listObj:
            copylist.append(line.get("text"))
        pyperclip.copy(f"{copylist}")
        keyboard.press(('ctrl+v'))

    # Create another new keyboard m for menu to choose new json.b
    elif keyboard.is_pressed('ctrl+m'):
        listObj = load_file()
        print('m clicked down')
        time.sleep(0.5)
    del(listObj)
    keyboard.read_key()

