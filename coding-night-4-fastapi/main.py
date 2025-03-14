from fastapi import FastAPI
import random


app = FastAPI()

#we will build two simple end points
#side hustle
#money quotes


side_husttle = [
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
@app.get("/side_hustles")
def get_side_hustle(api_key : str):
    """Return random side-hustle idea"""
    if api_key != "1234567":
        return {"error": "Invalid api key"}
    return {"side_husttle": random.choice(side_husttle)}


@app.get("/money_quotes")
def get_money_quotes(api_key :str):
    """Return random Money-Quotes"""
    if api_key != "1234567":
        return {"error": "Invalid api key"}
    return {"money_quotes": random.choice(money_quotes)}