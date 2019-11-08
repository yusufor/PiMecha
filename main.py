from tkinter import *
import tkinter as tk
from tkinter import font as tkfont
import random
import json

with open('data.json', 'r') as f:
    data_dict = json.load(f)

class Index :
    def __init__(self):
        self.conv = [None]

class User :
    def __init__(self):
        self.name = ""
        self.nation = ""
        self.language = [None]
        self.gender = ""
        self.sexuality = ""

class MOME :
    def __init__(self):
        self.s1 = Scale()
        self.s2 = Scale()
        self.s3 = Scale()
        self.s4 = Scale()
        self.s5 = Scale()
        self.s6 = Scale()
        self.s7 = Scale()
        self.s8 = Scale()
        self.s9 = Scale()

class main( tk.Tk ):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__( self, *args, **kwargs )

        self.title_font = tkfont.Font( family='Helvetica', size=18, weight="bold", slant="italic" )

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame( self )
        container.pack( side="top", fill="both", expand=True )
        container.grid_rowconfigure( 0, weight=1 )
        container.grid_columnconfigure( 0, weight=1 )

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F( parent=container, controller=self )
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid( row=0, column=0, sticky="nsew" )

        self.show_frame( "StartPage" )

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage( tk.Frame ):

    def __init__(self, parent, controller):
        tk.Frame.__init__( self, parent )
        self.controller = controller
        label = tk.Label( self, text="Personality", font='calibri 20 bold ' )
        label.grid( row=0, column=0, sticky='w' )

        button1 = tk.Button( self, text="MOME settings",
                             command=lambda: controller.show_frame( "PageOne" ) )
        button2 = tk.Button( self, text="chatBot",
                             command=lambda: [controller.show_frame( "PageTwo" ) , saveUser() ] )

        def saveUser() :
            User.name = ent1.get()
            User.nation = ent2.get()
            User.language = ent3.get()
            User.gender = ent4.get()
            User.sexuality = ent5.get()

        button1.grid( row=9, column=0, sticky='w' )
        button2.grid( row=9, column=1, sticky='e' )



        #choices = OptionMenu("Pizza", "Lasagne", "Fries", "Fish", "Potatoe")

        l1 = tk.Label( self, text="Name: " )
        l1.grid( row=1, column=0, sticky='w' )
        ent1 = Entry( self )
        ent1.grid( row=1, column=1 )
        #choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
        #choices.grid(row=1, column=1)
        #choices.grid(row=1, column=1)

        l2 = tk.Label( self, text="Nation: " )
        l2.grid( row=2, column=0, sticky='w' )
        ent2 = Entry( self )
        ent2.grid( row=2, column=1 )

        l3 = tk.Label( self, text="Language: " )
        l3.grid( row=3, column=0, sticky='w' )
        ent3 = Entry( self )
        ent3.grid( row=3, column=1 )

        l4 = tk.Label( self, text="Gender: " )
        l4.grid( row=4, column=0, sticky='w' )
        ent4 = Entry( self )
        ent4.grid( row=4, column=1 )

        l5 = tk.Label( self, text="Sexuality: " )
        l5.grid( row=5, column=0, sticky='w' )
        ent5 = Entry( self )
        ent5.grid( row=5, column=1 )


class PageOne( tk.Frame ):

    def __init__(self, parent, controller):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        label = tk.Label( self, text="MOME Settings", font='calibri 20 bold ' )
        label.grid( row=0, column=0 )
        button = tk.Button( self, text="Go to personality",
                            command=lambda: [controller.show_frame( "StartPage" )] )
        button.grid( row=11, column=0, sticky='w' )






        title1 = tk.Label( self, text="Rules of conduct", font='calibri 16 bold' )
        title1.grid( row=1, column=0, sticky='w' )

        plusMinusLabel = Label( self, text=("+ / -") )
        plusMinusLabel.grid( row=1, column=1 )

        l1 = Label( self, text=("1. I keep mentioning that I'm a machine.") )
        l1.grid( row=2, column=0, sticky='w' )
        MOME.s1 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s1.grid( row=2, column=1, sticky='w' )

        l2 = Label( self, text=("2. I'm screening my communications partner.") )
        l2.grid( row=3, column=0, sticky='w' )

        #s2 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s2 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s2.grid( row=3, column=1, sticky='w' )



        l3 = Label( self, text=("3. I respond positively to insults.") )
        l3.grid( row=4, column=0, sticky='w' )
        MOME.s3 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s3.grid( row=4, column=1, sticky='w' )

        l4 = Label( self, text=("4. I react to my counterpart with prejudice.") )
        l4.grid( row=5, column=0, sticky='w' )
        MOME.s4 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s4.grid( row=5, column=1, sticky='w' )

        l5 = Label( self, text=("5. I compliment my counterpart.") )
        l5.grid( row=6, column=0, sticky='w' )
        MOME.s5 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s5.grid( row=6, column=1, sticky='w' )

        l6 = Label( self, text=("6. I keep my distance from the other person.") )
        l6.grid( row=7, column=0, sticky='w' )
        MOME.s6 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s6.grid( row=7, column=1, sticky='w' )

        l7 = Label( self, text=("7. I'll beat my counterpart.") )
        l7.grid( row=8, column=0, sticky='w' )
        MOME.s7 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s7.grid( row=8, column=1, sticky='w' )

        l8 = Label( self, text=("8. I'm threatening my counterpart.") )
        l8.grid( row=9, column=0, sticky='w' )
        MOME.s8 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s8.grid( row=9, column=1, sticky='w' )

        l9 = Label( self, text=("9. I practice my own morals.") )
        l9.grid( row=10, column=0, sticky='w' )
        MOME.s9 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50 )
        MOME.s9.grid( row=10, column=1, sticky='w' )


class PageTwo( tk.Frame ):

    def __init__(self, parent, controller):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        label = tk.Label( self, text="chatBot PiMecha", font='calibri 20 bold' )
        label.pack( side="top", fill="x", pady=10, )

        img = PhotoImage( file="bot1.png" )
        photoL = Label( self, image=img )
        photoL.pack( pady =10 )

        curse = ["fuck", "idiot", "ass", "asshole", "pig"]


        def textAnalyzer ():
            query = textF.get()
            #matching = [s for s in curse if query in s]

            inputQuery = str(query).split()

            print(inputQuery)


            #Fluch Erkennung
            for x in inputQuery:
                if any(x in s for s in curse):
                    print("Fluch nicht!!!")

            #print("Matching: ", matching)
            #print("User: ", User.name, " Nation: ", User.nation)


            print(User.name," says \"", query,"\"",)



        def ask_from_bot ():
            query = textF.get()
            answer_from_bot = str(random.choice(Index.conv))
            msgs.insert(END, User.name + ":" + query)
            msgs.insert(END, "Optimus: "+ str(answer_from_bot))
            textF.delete(0,END)




            print("MOME: ", MOME.s1.get(), " ", MOME.s2.get(), " ",   MOME.s3.get(), " ", MOME.s4.get(), " ", MOME.s5.get(), " ", MOME.s6.get(), " ", MOME.s7.get(), " ", MOME.s8.get(), " ", MOME.s9.get())

            for data in data_dict:
                print(data['Name'])
                print(data['Language'])


        def changeIndex ():
            print("Test ", MOME.s2.get())
            if MOME.s2.get() == 1:
                Index.conv = open('test.txt', 'r').readlines()
                print(Index.conv)
                print("changed index to 1")
            if MOME.s2.get() == 0:
                Index.conv = open('test2.txt', 'r').readlines()
                print(Index.conv)
                print("changed index to 2")


        frame = Frame( self )

        sc = Scrollbar( frame )
        msgs = Listbox( frame, width=50, height=10 )

        sc.pack( side=RIGHT, fill=Y )
        msgs.pack( side=LEFT, fill=BOTH, pady=10 )

        frame.pack()

        #creating text field

        textF = Entry(self, font= ("Verdana", 20))
        textF.pack(fill =X, pady = 10)


        btn = Button(self, text = "Ask from Robot", font = ("Verdana", 20), command=lambda: [ changeIndex(), textAnalyzer(), ask_from_bot()])
        btn.pack()


        button = tk.Button( self, text="Go to personality",
                            command=lambda: controller.show_frame( "StartPage" ) )
        button.pack()


if __name__ == "__main__":
    app = main()
    app.title( "MOME" )
    app.resizable(0,0)
    app.mainloop()

