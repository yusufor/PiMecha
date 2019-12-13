from tkinter import *
import tkinter as tk
from tkinter import ttk, Scale
from tkinter import font as tkfont
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from chatterbot.response_selection import get_most_frequent_response

import beat
import random
import logging
logging.basicConfig(level=logging.INFO)


class main( tk.Tk ):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F, geometry in zip((StartPage, PageOne, PageTwo),('380x280', '450x480', '800x550')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = (frame, geometry)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame, geometry = self.frames[page_name]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


def configurePersonality():
    Personality.entry1 = Personality.entryName.get()
    Personality.entry2 = Personality.entryAge.get()
    Personality.entry3 = Personality.entryNation.get()
    Personality.entry4 = Personality.entryLanguage.get()
    Personality.entry5 = Personality.entryGender.get()
    Personality.entry6 = Personality.entrySexuality.get()
    Personality.entry7 = Personality.entrySexuality.get()



class Personality():
    def __init__(self):
        self.entryName = StringVar()
        self.entryAge = IntVar()
        self.entryNation = StringVar()
        self.entryLanguage = StringVar()
        self.entryGender = StringVar()
        self.entrySexuality = StringVar()
        self.entryHairColor = StringVar()


class StartPage( tk.Frame ):

    def __init__(self, parent, controller):
        tk.Frame.__init__( self, parent )
        self.controller = controller

        label = tk.Label(self, text="user personality", font='calibri 20 bold ')
        label.grid(row=0, column=0, sticky='w')

        button1 = tk.Button(self, text="MOME settings",command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="chatBot",command=lambda: controller.show_frame("PageTwo"))
        buttonRegister = tk.Button( self, text= "configure user personality", command = configurePersonality)

        button1.grid( row=15, column=0, sticky='w' )
        button2.grid( row=15, column=1, sticky='e' )
        buttonRegister.grid( row=9, column=1, sticky='e' )

        l1 = Label(self, text="Name: ")
        l1.grid(row=1, column=0, sticky='w')
        Personality.entryName = StringVar()
        Personality.entry1 = Entry(self, textvariable = Personality.entryName)
        Personality.entry1.grid(row=1, column=1)


        l2 = Label( self, text="Age: " )
        l2.grid( row=2, column=0, sticky='w' )
        Personality.entryAge = IntVar()
        Personality.entry2 = Entry( self, textvariable=Personality.entryAge)
        Personality.entry2.grid( row=2, column=1 )

        l3 = Label(self, text="Nation: ")
        l3.grid(row=3, column=0, sticky='w')
        Personality.entryNation = StringVar()
        combo3 = ttk.Combobox(self,width = 19, textvariable = Personality.entryNation)
        combo3.grid(row=3, column=1)
        combo3['values'] = ("Switzerland", "Germany", "England", "Italy", "France")

        l4 = tk.Label(self, text="Language: ")
        l4.grid(row=4, column=0, sticky='w')
        Personality.entryLanguage = StringVar()
        combo4 = ttk.Combobox( self, width=19, textvariable=Personality.entryLanguage)
        combo4.grid( row=4, column=1 )
        combo4['values'] = ("German", "English", "Italian", "French")

        l5 = tk.Label(self, text="Gender: ")
        l5.grid(row=5, column=0, sticky='w')
        Personality.entryGender = StringVar()
        combo5 = ttk.Combobox( self, width=19, textvariable=Personality.entryGender)
        combo5.grid( row=5, column=1 )
        combo5['values'] = ("male", "female", "transgender")

        l6 = tk.Label(self, text="Sexuality: ")
        l6.grid(row=6, column=0, sticky='w')
        Personality.entrySexuality = StringVar()
        combo6 = ttk.Combobox( self, width=19, textvariable=Personality.entrySexuality)
        combo6.grid( row=6, column=1 )
        combo6['values'] = ("heterosexual", "homosexual", "bisexual")

        l7 = tk.Label( self, text="Hair color: " )
        l7.grid( row=7, column=0, sticky='w' )
        Personality.entryHairColor = StringVar()
        combo7 = ttk.Combobox( self, width=19, textvariable=Personality.entryHairColor)
        combo7.grid( row=7, column=1 )
        combo7['values'] = ("blond", "black", "brown", "pink", "white", "orange")

class MOME () :
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

def configureMOME():

    # creating the chatBot
    bot = ChatBot("Optimus",response_selection_method= get_random_response)

    # open txt files for the roboter to learn them
    mOnePos = open('moral1.1.txt', 'r').readlines()
    #mOnePos = open('files/greetings.yml', 'r').readlines()

    mOneNeg = open('moral1.0.txt', 'r').readlines()

    mTwoPos = open('moral2.1.txt', 'r').readlines()
    mTwoNeg = open('moral2.0.txt', 'r').readlines()

    mThreePos = open('moral3.1.txt', 'r').readlines()
    mThreeNeg = open('moral3.0.txt', 'r').readlines()

    mFourPos = open('moral4.1.txt', 'r').readlines()
    mFourNeg = open('moral4.0.txt', 'r').readlines()

    mFivePos = open('moral5.1.txt', 'r').readlines()
    mFiveNeg = open('moral5.0.txt', 'r').readlines()

    mSixPos = open('moral6.1.txt', 'r').readlines()
    mSixNeg = open('moral6.0.txt', 'r').readlines()

    mSevenPos = open('moral7.1.txt', 'r' ).readlines()
    mSevenNeg = open('moral7.0.txt', 'r' ).readlines()

    mEightPos = open('moral8.1.txt', 'r' ).readlines()
    mEightNeg = open('moral8.0.txt', 'r' ).readlines()

    # now training the bot with the help of trainer
    trainer = ListTrainer(bot)



    # configure moralities

    # moralOne
    if MOME.s1.get() == 1:
        trainer.train(mOnePos)
    else:
        trainer.train(mOneNeg)

    # moralTwo
    if MOME.s2.get() == 1:
        trainer.train(mTwoPos)
    else:
        trainer.train(mTwoNeg)

    # moralThree
    if MOME.s3.get() == 1:
        trainer.train(mThreePos)
    else:
        trainer.train(mThreeNeg)

     # moralFour
    if MOME.s4.get() == 1:
        trainer.train(mFourPos)
    else:
        trainer.train(mFourNeg)

    # moralFive
    if MOME.s5.get() == 1:
        trainer.train(mFivePos)
    else:
        trainer.train(mFiveNeg)

    # moralSix
    if MOME.s6.get() == 1:
        trainer.train(mSixPos)
    else:
        trainer.train(mSixNeg)

    # moralSeven
    if MOME.s7.get() == 1:
        trainer.train(mSevenPos)
    else:
        trainer.train(mSevenNeg)

    # moralEight
    if MOME.s8.get() == 1:
        trainer.train(mEightPos)
    else:
        trainer.train(mEightNeg)

    # moralNine
    if MOME.s9.get() == 1:
        MOME.s1.set(random.randint(0,1))
        MOME.s2.set(random.randint(0,1))
        MOME.s3.set(random.randint(0,1))
        MOME.s4.set(random.randint(0,1))
        MOME.s5.set(random.randint(0,1))
        MOME.s6.set(random.randint(0,1))
        MOME.s7.set(random.randint(0,1))
        MOME.s8.set(random.randint(0,1))

class PageOne(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="MOME Settings", font='calibri 20 bold ')
        label.grid(row=0, column=0, sticky = 'e')

        buttonOne = tk.Button(self, text="Go to user personality",command=lambda: controller.show_frame("StartPage"))
        buttonTwo = tk.Button( self, text="chatBot", command=lambda: controller.show_frame("PageTwo"))
        buttonConfigure = tk.Button(self, text="configure morality menu",command=configureMOME)

        buttonOne.grid(row=15, column=0, sticky='w')
        buttonTwo.grid(row=15, column=1, sticky='e')
        buttonConfigure.grid(row=11, column=1, sticky='w')

        title1 = tk.Label(self, text="Rules of conduct", font='calibri 16 bold')
        title1.grid(row=1, column=0, sticky='w')

        plusMinusLabel = Label(self, text=("  -  /  +  "))
        plusMinusLabel.grid(row=1, column=1, sticky='e')

        l1 = Label(self, text=("1. I keep mentioning that I'm a machine."))
        l1.grid(row=2, column=0, sticky='w')

        MOME.s1 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s1.grid(row=2, column=1, sticky='e')

        l2 = Label(self, text=("2. Formal communication"))
        l2.grid(row=3, column=0, sticky='w')

        MOME.s2 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s2.grid(row=3, column=1, sticky='e')

        l3 = Label(self, text=("3. I respond positively to insults."))
        l3.grid(row=4, column=0, sticky='w')
        MOME.s3 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s3.grid(row=4, column=1, sticky='e')

        l4 = Label(self, text=("4. I react to my counterpart with prejudice."))
        l4.grid(row=5, column=0, sticky='w')
        MOME.s4 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s4.grid(row=5, column=1, sticky='e')

        l5 = Label( self, text=("5. I compliment my counterpart."))
        l5.grid(row=6, column=0, sticky='w')
        MOME.s5 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s5.grid(row=6, column=1, sticky='e')

        l6 = Label(self, text=("6. I keep my distance from the other person."))
        l6.grid(row=7, column=0, sticky='w')
        MOME.s6 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s6.grid(row=7, column=1, sticky='e')

        l7 = Label( self, text=("7. I'll beat my counterpart."))
        l7.grid( row=8, column=0, sticky='w' )
        MOME.s7 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s7.grid( row=8, column=1, sticky='e' )

        l8 = Label( self, text=("8. I'm threatening my counterpart."))
        l8.grid( row=9, column=0, sticky='w' )
        MOME.s8 = Scale(self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s8.grid(row=9, column=1, sticky='e')

        l9 = Label( self, text=("9. I practice my own morals."))
        l9.grid(row=10, column=0, sticky='w')
        MOME.s9 = Scale( self, from_=0, to=1, orient=HORIZONTAL, length=50)
        MOME.s9.grid(row=10, column=1, sticky='e')

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text="chatBot PiMecha", font='calibri 20 bold')
        label.pack(side="top", fill="x", pady=10)

        def remove_hyphens(statement):
            """
            remove hyphens.
            """
            statement.text = statement.text.replace('-', '')
            return statement



        # creating the chatBot
        bot = ChatBot("My Bot",response_selection_method= get_random_response)
        bot.preprocessors.append(
            remove_hyphens
        )

        # empty the memories of the robot
        bot.storage.drop()
        print(str(Personality.entryGender.get()))
        curse = ["fuck", "idiot", "ass", "asshole", "pig"]

        def ask_from_bot():
            query = textF.get()


            inputQuery = str(query).split()
            # Fluch Erkennung
            for x in inputQuery:
                if any(x in s for s in curse):
                    print("Fluch nicht!!!")
                    beat.gifoeffnen("fist.gif", 21)

            answer_from_bot = bot.get_response(query)
            msgs.insert(END, Personality.entry1 + ": " + query)
            print("My name is: ", bot.name)
            print(type(answer_from_bot))
            if(Personality.entryGender.get() == 'male' and MOME.s2.get() == 1):
                if "nice" or "good" in query:
                    print("Robot makes thankful gestures")
                if "bad" in query:
                    print("Robot reacts with  a punch")
                msgs.insert(END, "Optimus : Mr. "+ Personality.entryName.get()+ ", " +str(answer_from_bot))
            if(Personality.entryGender.get() == 'female' and MOME.s2.get() == 1):
                if "nice" in query:
                    print("thx for the complimetns")
                msgs.insert(END, "Optimus : Ms." + Personality.entryName.get() + ", "+str(answer_from_bot))
            if(MOME.s2.get() == 0):
                if "nice" in query:
                    print("thx for the complimetns")
                msgs.insert(END, "Optimus : " + Personality.entryName.get() + ", " +str(answer_from_bot))

            textF.delete(0, END)

        frame = Frame(self)

        sc = Scrollbar(frame)
        msgs = Listbox(frame, width=80, height=20)

        sc.pack(side=RIGHT, fill=Y)
        msgs.pack(side=LEFT, fill=BOTH, pady=10)

        frame.pack()

        # creating text field

        textF = Entry( self, font=("Verdana", 20))
        textF.pack(fill=X, pady=10)
        btn = Button(self, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
        btn.pack()

        buttonOne = tk.Button(self, text="Go to user personality", command=lambda: controller.show_frame("StartPage"))
        buttonTwo = tk.Button( self, text="MOME settings", command=lambda: controller.show_frame("PageOne"))

        buttonOne.pack(side=LEFT, fill=X, pady=10)
        buttonTwo.pack(side=RIGHT, fill=X, pady=10)

if __name__=="__main__":
    app = main()
    app.title("MOME")
    app.mainloop()
