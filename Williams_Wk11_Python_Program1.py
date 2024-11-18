# This program displays a favorite quote from the
# 2010 Dreamworks movie, "Megamind." This program
# Also leans heavily on the example programs provided
# in Gaddis' textbook focusing on GUI programs.

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create six Label widgets.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Spider? Uh... Yes! The... the speeyder.')
        self.label2 = tkinter.Label(self.main_window,
                                    text='Even the smallest bite from...')
        self.label3 = tkinter.Label(self.main_window,
                                    text='"arachnus deathicus"... will instantly paralyze...')
        self.label4 = tkinter.Label(self.main_window,
                                    text='AARGH! GET IT OFF! IT BIT ME!')
        self.label5 = tkinter.Label(self.main_window,
                                    text='')
        self.label6 = tkinter.Label(self.main_window,
                                    text='Spider scene from Dreamworks 2010 movie, "Megamind"')

        # Call all Label widgets' pack method.
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.label6.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()