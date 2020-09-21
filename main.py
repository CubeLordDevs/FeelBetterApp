from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
import PIL
from io import BytesIO

import ipinfo
import praw
import random
import requests
import json
import vlc
import csv

# Important: The psychologist finder won't work accurately on a web-hosted IDE because it goes off ip. The IP given by these IDEs are the IPs of their servers, not of your computer.

# IpInfo
access_token = '70a4fe248c7317'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails()
latlong = str(details.loc)
latlong = latlong.split(',')
# Creates window and sets window size.
master = Tk()
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(),
                                     master.winfo_screenheight()))

reddit = praw.Reddit(
    client_id='MBvRhf5TtOrrKg',
    client_secret='F6XvVd2NxnzellMxgTJ4ERiSnqQ',
    user_agent='FeelBetterApp')

# Sets theme for the app
style = ThemedStyle(master)
style.theme_use('equilux')

# Login Page (nameget)/
global submit


def forgetUserTo():
    # Retrieves the text from the input box
    username = str(submit.get())
    welcome = Label(hub, text=f"Hello {username}, what would you like to do?")
    welcome.config(font=('Helvetica', 25))
    welcome.grid(row=0)
    nameget.pack_forget()
    hub.pack()


# Create frame
nameget = Frame(master)
nameget.pack()

# Create prompt, input box, and submit button in that order.
prompt0 = Label(nameget, text="Welcome to FeelBetterApp")
prompt0.config(font=('Helvetica', 40))
prompt0.grid(pady=(135, 0))

prompt = Label(nameget, text="What's your name?")
prompt.config(font=('Helvetica', 25))
prompt.grid(pady=(100, 0))

submit = Entry(nameget, font=('Helvetica', 20))
submit.grid(pady=(40, 0))
submit.focus_set()

loginbtnStyle = ttk.Style()
loginbtnStyle.configure("TButton", font=('Helvetica', 20))
loginBtn = ttk.Button(
    nameget, text='Get Started!', command=forgetUserTo, style='TButton')
loginBtn.config(width=20)
loginBtn.grid(pady=(40, 100))

# Create frame
hub = Frame(master)

# Create various buttons for app functions


# Button to access breathing exercises
def forgetBreath():
    hub.pack_forget()
    breathe.pack()


breathe = Frame(master)
breatheBtn = ttk.Button(hub, text="Breathing Exercises", command=forgetBreath)
breatheBtn.config(width=30)
breatheBtn.grid(row=1, pady=(100, 50))


def breathBack():
    breathe.pack_forget()
    hub.pack()


breathebackBtn = ttk.Button(
    breathe, text="Back", style="TButton", command=breathBack)
breathebackBtn.grid(pady=(40, 100))

breatheLabel = Label(breathe, text="Deep Breathing")
breatheLabel.configure(font=('Helvetica', 40))
breatheLabel.grid()

breatheLabel1 = Label(breathe, text="Become stress free")
breatheLabel1.configure(font=('Helvetica', 10))
breatheLabel1.grid()


def forgetPage1():
    breathe.pack_forget()
    breathePage2.pack()


breathePage2 = Frame(master)

breathepage2btnStyle = ttk.Style()
breathepage2btnStyle.configure("TButton", font=('Helvetica', 20))
breathepage = ttk.Button(
    breathe, text='Next page!', command=forgetPage1, style='TButton')
breathepage.config(width=20)
breathepage.grid(row=30)

breatheLabel2 = Label(
    breathePage2,
    text=
 "1: While standing or sitting, draw your elbows back slightly to allow your \nchest to expand")
breatheLabel2.configure(font=('Helvetica', 15))
breatheLabel2.grid()

breatheLabel3 = Label(breathePage2, text = "2: Take a deep inhalation through your nose and retain your breath for a count of 5")
breatheLabel3.configure(font=('Helvetica', 15))
breatheLabel3.grid()

breatheLabel4 = Label(breathePage2, text = "3: Slowly release your breath by exhaling through your nose.")
breatheLabel4.configure(font=('Helvetica', 15))
breatheLabel4.grid()

def breathBack2():
    breathePage2.pack_forget()
    hub.pack()

breatheback2Btn = ttk.Button(
    breathePage2, text="Back", style="TButton", command=breathBack2)
breatheback2Btn.grid(pady=(40, 100))
# Button to get a funny meme


def forgetHubMeme():
    hub.pack_forget()
    meme.pack()


meme = Frame(master)

generateMemeBtn = ttk.Button(
    hub, text="Get a Funny Meme!", command=forgetHubMeme)
generateMemeBtn.config(width=30)
generateMemeBtn.grid(row=2, pady=(0, 50))

memes_submissions = reddit.subreddit("wholesomememes").hot()
post_to_pick = random.randint(1, 100)
for i in range(0, post_to_pick):
    submission = next(x for x in memes_submissions if not x.stickied)
img_url = submission.url
response = requests.get(img_url)
img_data = response.content
img = Image.open(BytesIO(img_data))
img = img.resize(
    (master.winfo_screenwidth(), master.winfo_screenheight() - 42),
    Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(meme, image=img)
panel.grid()


def meback():
    meme.pack_forget()
    hub.pack()


def newMeme():
    memes_submissions = reddit.subreddit("wholesomememes").hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        img_url = submission.url
        response = requests.get(img_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize(
            (master.winfo_screenwidth(), master.winfo_screenheight() - 42),
            Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(meme, image=img)
        panel.grid()


mebackBtn = ttk.Button(meme, text="Back", style="TButton", command=meback)
mebackBtn.grid()
newmeme = ttk.Button(meme, text="New meme!", style="TButton", command=newMeme)
newmeme.grid()

# Fun Activity Generator


# Button to display a random fun activity out of a list
def forgetHubAct():
    hub.pack_forget()
    actPage.pack()


activityBtn = ttk.Button(
    hub, text="Find a Fun Activity to Do!", command=forgetHubAct)
activityBtn.config(width=30)
activityBtn.grid(row=3, pady=(0, 50))

# Create activity page
actPage = Frame(master)


# Back button (activity page)
def actBack():
    actPage.pack_forget()
    hub.pack()


actBackBtn = ttk.Button(actPage, text="Back", style="TButton", command=actBack)
actBackBtn.grid()

# Display a fun activity
funActivities = [
    "Play video games!", "Cook or bake something!", "Read a book!",
    "Exercise!", "Read XKCD comics!", "Browse Wikipedia!", "Watch YouTube!",
    "Read code documentation!", "Learn a new skill!",
    "Finish all your homework!", "Talk with your friends!"
]

activityNumber = 0


def generateAct():
    actLabel = Label(actPage, text=f'{random.choice(funActivities)}', font=('Helvetica', 20))
    actLabel.grid()


generateActBtn = ttk.Button(
    actPage,
    text="Give me a fun activity!",
    style="TButton",
    command=generateAct)
generateActBtn.grid()


# Button to access psychiatrist finder
def forgetHubPsy():
    # Loads frame for psychiatrist finder
    hub.pack_forget()
    psypage.pack()


# Creates actual button for psychiatrist finder
psyBtn = ttk.Button(
    hub, text='Find Psychiatrists Near You', command=forgetHubPsy)
psyBtn.config(width=30)
psyBtn.grid(row=4, pady=(0, 70))
# Creates psychiatrist frame
psypage = Frame(master)
# Retrieves 1 psychologist near the given IP
tturl = 'https://api.tomtom.com/search/2/search/'
url = f"{tturl}/psychiatrist.json?key=eSMl542KN5OmFI0OjVM4cs2cSzYdIbKf&limit=10&lat={latlong[0]}&lon={latlong[1]}"
res = requests.get(url)
resp = res.json()
lenr = len(resp['results'])
for l in range(lenr):
    if resp['results'][l]['type'] != 'POI':
        continue
    else:
        for x in range(len(resp['results'][l]['poi']['categories'])):
            if resp['results'][l]['poi']['categories'][x] == 'doctor':
                psyname = Label(
                    psypage, text=str(resp['results'][l]['poi']['name']))
                psyname.config(font=('Helvetica', 25))
                psyname.grid(pady=(100, 20))
                psyph = Label(
                    psypage, text=str(resp['results'][l]['poi']['phone']))
                psyph.config(font=('Helvetica', 25))
                psyph.grid(pady=(0, 20))
                psyad = Label(
                    psypage,
                    text=str(resp['results'][l]['address']['freeformAddress']))
                psyad.config(font=('Helvetica', 25))
                psyad.grid(pady=(0, 20))
                break
            else:
                continue
    break


def psyback():
    psypage.pack_forget()
    hub.pack()


psybackBtn = ttk.Button(psypage, text="Back", style="TButton", command=psyback)
psybackBtn.grid()

master.mainloop()
