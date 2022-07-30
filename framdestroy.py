# Frame destroy

from tkinter import *

class myFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.makewidgets()
        self.pack(expand=YES, fill=BOTH)
    def makewidgets(self):
        Label(self, text='This is a test label').pack(expand=YES, \
                fill=BOTH)
        Button(self, text= 'Quit', command=self.destroy).pack(fill=X)

if __name__ == '__main__':
    root = Tk()
    root.title('Destroy Frame')
    root.iconname('Destroy')
    root.geometry("300x200")
    myFrame(root).mainloop()
