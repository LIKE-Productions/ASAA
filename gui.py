from guizero import *
import pymongo

# Scheme for images (width, height) [112, 50]
client = pymongo.MongoClient(
    "mongodb+srv://Magnus-Peters-Munzo:Magnus2008!@cluster0.edcxs.mongodb.net/LIKE?retryWrites=true&w=majority")
db = client.LIKE
asaa = db.asaa

app = App("ASAA_gui", 1280, 720)

# enter = PushButton(app, image="Images/Enterbutton.gif", width=112, height=50)

class GuiClass():

    def hide_startup(self):
        self.message.hide()
        self.message2.hide()
        self.option_one.hide()
        self.option_two.hide()

    def option_1(self):
        self.hide_startup()
        self.ns.show()
        self.auth.show()
        # self.enter.show()
        
        for query in asaa.find({"author": self.auth.value}):
            Text(app, query)
        
    
    
    def option_2(self):
        self.hide_startup()
        Text(app, "Entering in new data?", 40)
        Text(app, "What is your name?", 25)
        self.db_author = TextBox(app, )
    
    
    def __init__(self):
        """
        Startup variables
        """
        self.ns = Text(app, "What is the name you want to lookup?", 40, visible=False)
        self.auth = TextBox(app, command=self.option_1)
        self.ns.hide()
        self.auth.hide()
        # self.enter.hide()
        self.message = Text(app, "Welcome to ASAA!", 45, font="Helvetica")
        self.message2 = Text(app, "What do you want to do?", 30, font="Helvetica")
        self.option_one = PushButton(app, self.option_1, text="Review old data")
        self.option_two = PushButton(app, self.option_2, text="Enter in new data")



gclass = GuiClass()

gclass


# back = PushButton(app, gclass.__init__ , text="Back to main", align="bottom")
exi = PushButton(app, app.destroy, text="Exit", align="bottom")

app.display()