import encryption as cipher
import decryption as decipher   


try:
    import Tkinter as tk
        
except ImportError:
    import tkinter as tk
    from tkinter import *

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

lang = 'A'

class Toplevel1:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'

        top.geometry("1000x600")
        top.resizable(False, False)
        top.title("Morse Code Translator")
        top.configure(background="#d4b6ff")

        
        self.text1 = tk.Text(top)
        self.text1.place(x=300, y=110, height=240, width = 690)
        self.text1.configure(background="white")
        self.text1.configure(font="TkFixedFont 30")
        self.text1.configure(foreground="#000000")
        self.text1.configure(insertbackground="black")
        self.text1.configure(border ="5")

        self.text1_1 = tk.Text(root,
                        	height = 3,
                         	width = 20,
							font = "Code 39",
       						border = 5)
        self.text1_1.place(x=301, y=355, height=240, width = 689)

        def call():
            plain_text =self.text1.get("1.0",'end-1c').upper()
            ans=cipher.encryptor(plain_text)
            #print(ans)
            self.text1_1.insert('end -1 chars', ans)

        def get():
            encrypted_text =self.text1.get("1.0",'end-1c')
            x=decipher.decryptor(encrypted_text)
            self.text1_1.insert('end -1 chars', x)

        def clearAll() :
            # whole content of text area is deleted
            self.text1.delete('1.0', "end")
            self.text1_1.delete('1.0', "end")


        def changeLang():
            global lang
            if (lang == 'A'):
                lang = 'M'
                self.Label2.config(text='''    MORSE        ENGLISH''')
                self.Button1.configure(command = get)
            elif (lang == 'M'):
                lang = 'A'
                self.Label2.config(text='''ENGLISH      MORSE''')
                self.Button1.configure(command = call)

        self.Label4 = tk.Label(top)
        self.Label4.place(x=400, y=3,height=100, width=300)
        self.Label4.configure(background="#9DF4A6")

        self.Label2 = tk.Label(top, border = "50")
        self.Label2.place(x=300, y=3, height=100, width=700)
        self.Label2.configure(background="#9DF4A6")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ENGLISH      MORSE''',font=("Code",45,'bold'))



        self.changeButton = tk.Button(top)
        self.changeButton.place(x=630, y=30, height=33, width=60)
        self.changeButton.configure(activebackground="#ececec")
        self.changeButton.configure(activeforeground="#000000")
        self.changeButton.configure(background="#d9d9d9")
        self.changeButton.configure(disabledforeground="#a3a3a3")
        self.changeButton.configure(foreground="#000000")
        self.changeButton.configure(highlightbackground="green")
        self.changeButton.configure(highlightcolor="black")
        self.changeButton.configure(pady="0")
        self.changeButton.configure(text='''⇒''',command=changeLang, font = ("Code", 30))

        self.Button1 = tk.Button(top)
        self.Button1.place(x=100, y= 500, height=33, width=106)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="green")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Run''',command=call, font = ("Code", 20))

        self.Button2 = tk.Button(top)
        self.Button2.place(x=100, y= 550, height=33, width=106)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="green")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Clear''',command=clearAll, font = ("Code", 20))

        self.Title = tk.Label(top)
        self.Title.place(x=10, y=100, height=100, width = 280)
        self.Title.configure(background="#d4b6ff")
        self.Title.configure(foreground="black")
        self.Title.configure(text='''MORSE CODE''', font = ("Calibri", 30,'bold'))

        self.get_img = PhotoImage(file = 'design.png')
        self.img = tk.Label(top, image = self.get_img)
        self.img.configure(bg = "#d4b6ff")
        self.img.place(x=20,y=170)



        #new
if __name__ == '__main__':
    vp_start_gui()
