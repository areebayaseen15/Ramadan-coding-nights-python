from fastapi import FastAPI
import random


app = FastAPI()


# programming jokes
prgramming_joke = [
    "Kyun Python developer hamesha late hota hai? Kyunki wo pehle indentation set karta hai!",
    "Frontend Developer: 'Meri shaadi ho gayi!' Backend Developer: 'Kab commit kiya?'",
    "Programmer ki shaadi kyun nahi hoti? Kyunki wo hamesha '404: Love Not Found' hota hai!",
    "Ek Python developer ne bakery kholo, naam rakha ‘Indentation Cakes’.",
    "C++ programmer ka breakup ho gaya. Usne bola: 'Ab main tumhe delete kar raha hoon… aur memory bhi free kar raha hoon!'",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Ek developer ne ghar ka kaam nahi kiya. Maa boli: ‘Beta, ghar bhi toh ek module hai!’",
    "Kya tumhey pata hai? Computers kabhi thakte nahi… bas 'crash' ho jaate hain!",
    "Why did the JavaScript developer go broke? Because he lost his 'this'.",
    "Developer ka breakup ho gaya, dosto ne poocha: 'Kya hua?' Usne kaha: 'Usne mujhe hardcoded samajh liya!'",
    "Programming ke rishte arrange nahi hote, kyunki sab chahte hain 'perfect match()'!",
    "Linux users kabhi shaadi nahi karte, kyunki wo hamesha 'root' hi rehna chahte hain!",
    "Kya tumhey pata hai? Ek program bina error ke chal jaye to developer ko shak hota hai!",
    "Kyun programmer ki life boring hoti hai? Kyunki wo sirf ‘if’ aur ‘else’ mein jeeta hai!",
    "Agar ek programmer party de to kya serve karega? 'Cookies' aur 'Java'!",
    "Main ek database ke bina jee nahi sakta... kyunki mujhe ‘relational’ hona pasand hai!",
    "Interviewer: ‘Aapko kon si language aati hai?’ Candidate: ‘Main fluent hoon Stack Overflow mein!’",
    "Programmer ka favorite formula: if (sad) then drink(tea) else code();",
    "Programming aur rishtedaron ki baat ek jaisi hoti hai, dono mein 'exception handling' zaroori hoti hai!",
    "Bachpan mein Ma kehti thi: 'Beta kuch ban na!'… Maine API bana li!"
]

#  Dark Humor Jokes 
dark_humor_jokes = [
    "Mujhe andheray se dar lagta tha… phir maine bijli ka bill dekha, ab roshni se bhi lagta hai!",
    "Parallel parking meri zindagi ki tarah hai… bas bar bar try karti hoon jab tak koi aur haar na maan le!",
    "Mujhe construction ka ek joke yaad tha… magar abhi bhi uspe kaam chal raha hai!",
    "Ek baar dentist ne kaha: 'Relax karo!' Maine kaha: 'Doctor, main student hoon, relax kaise karoon?!'",
    "Khawab mein paisay aay thay… lekin jab aankh khuli to sirf bijli ka bill aya!",
    "Meri maa kehti thi, 'Beta mehman ko izzat deni chahiye'… isliye maine mehman ka WiFi password pehle poocha!",
    "Insaan ka sabse bara dukh kya hota hai? Jab banda kahay 'Last baar try karta hoon'… aur phir chal jaye!",
    "Padosi: 'Aapke ghar ki roshni bohat tez hai!' Main: 'Bhai, hamari bijli ki taqat sirf lightning storm aur bijli ka bill hai!'",
    "Main itna gareeb hoon, agar kisi ka WiFi free chalta ho to shukriya ada karta hoon!",
    "Mujhse ek dost ne kaha: 'Tumhara time aayega!' Maine kaha: 'Bhai, bus charger laga raha hoon!'",
    "Exam hall mein sab ke chehray dekh ke lagta hai kisi ne padhai nahi ki!",
    "Main zindagi ko ek loop samajh raha hoon… har din wohi repeat hota hai!",
    "Har jagah 'Loading…' likha hota hai, sirf paisay hi 'Insufficient Balance' likhte hain!",
    "Doctor: 'Aapko tension kyun hoti hai?' Banda: 'Doctor sahab, jab tak tension na ho, tab tak lagta hi nahi zindagi chal rahi hai!'",
    "Mujhse kisi ne poocha: 'Tum kuch naya seekh rahe ho?' Maine kaha: 'Haan, ghar walon ki baat sun raha hoon!'",
    "Kabhi socha hai log itna late kyun reply karte hain? Kyunki unka bhi dil nahi karta reply karne ka!",
    "Zindagi sirf do din ki hai… ek din online lectures aur doosra din assignments!",
    "Agar tum kabhi udaas ho, to sochna ke tumhari bijli ka bill kitna aya hai… foran hasi ajayegi!",
    "Mujhe ek din apni life change karni thi, lekin maine socha: 'Next update ke baad!'",
    "Bachpan mein sochta tha bada ho ke masti karunga… ab sirf sochta hoon!"   
]

#  Dad Jokes
dad_jokes = [
    "Beta: 'Abbu, mujhe koi motivational baat batao!' Abbu: 'Beta, jiska koi nahi hota, uska password hota hai!'",
    "Biwi: 'Aaj main kya pehnoon?' Shohar: 'Mera sar, aur soti raho!'",
    "Jab main chhota tha to mujhe lagta tha computer ki memory kam ho gayi to use almond khilani chahiye!",
    "Beta: 'Papa, main engineer banna chahta hoon!' Papa: 'Beta, pehle ghar ke bulb aur fan kaam se chalu kar!'",
    "Agar main pizza ka ek tukra kha loon to kya woh poora pizza count hota hai?",
    "Jab light chali jati hai, Pakistani walidayn keh dete hain: 'Tumhari nazar weak hai, isliye nahi dikh raha!'",
    "Meri maa kehti hai: 'Beta, zindagi ek chhoti si boat hai!' Main kehta hoon: 'To life-jacket kahan hai?'",
    "Beta: 'Abbu, main shaadi kar raha hoon!' Abbu: 'Bachpan se hi jokes sun sun ke bada hua hai!'",
    "Doctor ne kaha: 'Aap healthy hain!' Maine kaha: 'Matlab next life update tak okay hoon?!'",
    "Beta: 'Papa, homework complete kar liya hai!' Papa: 'Aur revision?' Beta: 'Papa, yeh joke section hai, serious baat mat karo!'"
]

@app.get("/")
def read_root():
    return {
        "message": "Hello to the world of humour , Go to /prgramming_joke  , /dark_humor_jokes"
        " or /dad_jokes to get a random jokes"
    }

@app.get("/prgramming_joke")
def get_jokes():
    """Return Pakistani jokes about programming"""
    return {"jokes_list": random.choice(prgramming_joke)}


@app.get("/dark_humor_jokes")
def get_Humor_jokes():
    """Return dark humor jokes"""
    return {"jokes_list": random.choice(dark_humor_jokes)}

@app.get("/dad_jokes")
def get_dad_jokes():
    """Return dad jokes"""
    return {"jokes_list": random.choice(dad_jokes)}

