from fastapi import FastAPI
import random


app = FastAPI()

#we will build two simple end points
#side hustle
#money quotes


side_hustles = [
    "Freelance Web Development – Build websites using HTML, CSS, JavaScript, and Next.js.",
    "Create & Sell Templates – Sell Next.js, Tailwind CSS, or TypeScript templates on Gumroad or ThemeForest.",
    "Tech Blogging – Write about TypeScript, FastAPI, or Next.js on Medium or Dev.to.",
    "Bug Bounty Hunting – Earn by finding security vulnerabilities in websites.",
    "Automate Tasks – Create Python or TypeScript automation scripts and sell them.",
    "Online Tutoring – Teach coding on Udemy, Skillshare, or YouTube."
    "AI-Powered Tools – Build AI-based resume generators, chatbots, or API services."

]


money_quotes =[
  '"The more you learn, the more you earn." – Warren Buffett',
   ''' "Don't work for money; make money work for you." – Robert Kiyosaki''',
    '"The rich invest in time, the poor invest in money." – Warren Buffett',
    '"Make your money work so you don’t have to." – Grant Cardone',
    '"Getting rich begins with the right mindset, the right words, and the right plan." – Robert Kiyosak',
]


#decorator

@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote"
    }


@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes():
    """Returns a random money quote"""
    return {"money_quote": random.choice(money_quotes)}
