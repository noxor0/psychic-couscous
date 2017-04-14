import Tkinter as tk
from HikeBuddy import HikeBuddy
from Database import Database
TITLE_FONT = ("Helvetica", 14, "bold")
db = Database()
class BeWeaveApp(tk.Tk):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/14/2017\n
    This is the main app that controls each frame."""

    def __init__(self, hikes, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #This container stacks a bunch of frames on top of each other
        #The one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Hike Away")
        self.frames = {}
        self.frames["VotePage"] = VotePage(hikes,parent=container, controller=self)
        self.frames["HomePage"] = HomePage(hikes, parent=container, controller=self)
 

        self.frames["VotePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")


        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the HomePage Class that will show the home page screen once the user has logged in."""

    def __init__(self, hikes, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text=hikes[0].name, width=28,
                            command=lambda: controller.show_frame("VotePage"))
        button4 = tk.Button(self, text=hikes[1].name, width=28,
                            command=lambda: controller.show_frame("VotePage"))
        
        button2.pack(pady=5)
        button4.pack(pady=5)
        button = tk.Button(self, text=hikes[2].name, width=28,
                           command=lambda: controller.show_frame("VotePage"))
        button.pack()

class VotePage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the HomePage Class that will show the home page screen once the user has logged in."""

    def __init__(self, hikes, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        db.add_user_hike(1, hikes[0].trail_id, None)
        label = tk.Label(self, text="How Hard Was \nThe Hike", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Too Hard", width=16,
                            command=lambda: self.too_hard(hikes[0]))
        button4 = tk.Button(self, text="Perfect", width=16,
                            command=lambda: self.perfect(hikes[0]))
        button2.pack(pady=5)
        button4.pack(pady=5)
        
        button = tk.Button(self, text="Too Easy", width=16,
                           command=lambda: self.too_easy(hikes[0]))
        button.pack()

    def too_hard(self, hike):
        db.update_user_hike(1, hike.trail_id, 1)
        # db.add_user_hike(1, hike.trail_id)
        db.update_usr_lvl(1, hike.trail_id)
        self.parent.destroy()
        self.destroy()
        self.controller.destroy()
    def perfect(self, hike):
        db.update_user_hike(1, hike.trail_id, 0)
        # db.add_user_hike(1, hike.trail_id)
        db.update_usr_lvl(1, hike.trail_id)
        self.parent.destroy()
        self.destroy()
        self.controller.destroy()
    def too_easy(self, hike):
        db.update_user_hike(1, hike.trail_id, -1)
        # db.add_user_hike(1, hike.trail_id)
        db.update_usr_lvl(1, hike.trail_id)
        self.parent.destroy()
        self.destroy()
        self.controller.destroy()


sample = HikeBuddy()
hikes = sample.find_suggestions()

app = BeWeaveApp(hikes)
app.mainloop()
