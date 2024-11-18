# This program displays the program creator's information, as well as
# a Quit button that calls the Tk class's destroy method when clicked.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        if __name__ == '__main__':
            self.main_window = tkinter.Tk()

            # Create a Button widget. The text 'Click Me for Information!'
            # should appear on the face of the Button. The
            # do_something method should be executed when
            # the user clicks the Button.
            self.my_button = tkinter.Button(self.main_window,
                                            text='Click Me for Information!',
                                            command=self.do_something)

            # Create a Quit button. When this button is clicked,
            # the root widget's destroy method is called.
            # (The main_window variable references the root widget,
            # so the callback function is self.main_window.destroy.)
            self.quit_button = tkinter.Button(self.main_window,
                                              text='Quit',
                                              command=self.main_window.destroy)

            # Pack the Buttons.
            self.my_button.pack()
            self.quit_button.pack()

            # Enter the tkinter main loop.
            tkinter.mainloop()

    def do_something(self):
        #display an info dialog box.
        tkinter.messagebox.showinfo('Response',
                                    'Seth Williams, 50180 211th St. Lake Crystal, MN, 56055')
# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()