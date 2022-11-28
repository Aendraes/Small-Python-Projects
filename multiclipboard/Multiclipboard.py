import pyperclip, keyboard
import time, json, os
from datetime import datetime
import tkinter as tk
# TODO Create popup window on ctrl + ä
class multiclipboard():
    def __init__(self, json_name='clipboard.json'):
        self.listObj=[]
        self.json_name = json_name
        self.now = datetime.now()
        self.clipdict = dict()
        self.index = 0
    def newfile(self):
        """Checks if the filename exists and if it does not this creates the file and sets it up for json."""
        if not os.path.isfile(self.json_name):
            x=open(self.json_name, 'x')
            x.close()
            x=open(self.json_name, 'w')
            json.dump(self.listObj, x,
                            indent=4,
                            separators=(',', ': '))
            x.close()
    def load_file(self):
        """Loads the chosen file to store data in."""
        self.newfile()
        with open(self.json_name) as fp:
            self.listObj = json.load(fp)
    
    def popupwindow(self):
        """Create a window with a text box and a button.
        Gets the value from the text box on button click and changes the name of
        self.json_name to the new name."""
        root= tk.Tk()
        canvas1 = tk.Canvas(root, width=400, height=300)
        canvas1.pack()

        entry1 = tk.Entry(root) 
        canvas1.create_window(200, 140, window=entry1)

        def get_filename():  
            x1 = entry1.get()
            
            self.json_name = x1
            time.sleep(0.2)
            root.destroy()
            
        button1 = tk.Button(text='Enter new file name', command=get_filename)
        canvas1.create_window(200, 180, window=button1)

        root.mainloop()
    

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
            print("ctrl+c clicked down")
            with open(x.json_name, 'w') as json_file:
                json.dump(x.listObj, json_file,
                        indent=4,
                        separators=(',', ': '))


        # Create a new keybind to print the Json list. ctrl+b
        elif keyboard.is_pressed('ctrl+b'):
            x.load_file()
            time.sleep(0.2)
            copylist = []
            for item in x.listObj:
                copylist.append(item.get("text"))
            pyperclip.copy(f"{copylist}")
            keyboard.press(('ctrl+v'))

        # Create another new keyboard ä menu to choose new json.b
        elif keyboard.is_pressed('ctrl+ä'):
            x.popupwindow()
            x.load_file()
            x.index=0
            time.sleep(0.5)
       
        
        # When ctrl+4 is pressed down it will append one item back in the list.
        elif keyboard.is_pressed('ctrl+4'):
            x.load_file()
            time.sleep(0.2)
            copylist = []
            for item in x.listObj:
                copylist.append(item.get("text"))
            copylist = copylist[::-1]
            if x.index < len(copylist)-1:
                x.index+=1
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",x.index)
                pyperclip.copy(copylist[x.index])
            keyboard.press('ctrl+v')
        elif keyboard.is_pressed('ctrl+6'):
            x.load_file()
            time.sleep(0.2)
            copylist = []
            for item in x.listObj:
                copylist.append(item.get("text"))
            copylist = copylist[::-1]
            if x.index > 0:
                x.index = x.index -1
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",x.index)
                pyperclip.copy(copylist[x.index])
            keyboard.press('ctrl+v')
        keyboard.read_key()
