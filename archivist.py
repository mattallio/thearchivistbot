import telebot, random, os, time, eyed3, datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import pandas as pd
import os
from keep_alive import keep_alive

API_KEY = os.environ['API_KEY']

archivist = telebot.TeleBot(API_KEY)

#excel text with stickers' names and numbers initialization
stickerNumber = pd.read_excel(r"Stickers/0-sticker-to-number.xlsx")
titles = stickerNumber.Titles
#timer setup
startTime = datetime.datetime.now()
count = 0
#variable that block the archivist from answering
crash = 0
chill = 0

#initialization of the archivist, the introduction message and the buttons relative to the commands
@archivist.message_handler(commands=["start"]) 
def initialization(message):
   statementBegins = open(r"Stickers/15.webp", "rb")
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(1)
   archivist.send_message(message.chat.id, "The name is Jonathan Sims")
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_message(message.chat.id,"Head Archivist of the Magnus Institute")
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_message(message.chat.id,"London.")
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_sticker(message.chat.id, statementBegins)
   markup = ReplyKeyboardMarkup(row_width=2)
   command1 = KeyboardButton("Ominous Speech")
   command2 = KeyboardButton("Monster Talking")
   command3 = KeyboardButton("Micheal Laughter")
   command4 = KeyboardButton("Existential Crisis")
   command5 = KeyboardButton("Insult @ Martin")
   command6 = KeyboardButton("Surprise Me...")
   markup.add(command1,command2,command3,command4,command5,command6)
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_message(message.chat.id, "What can I do for you today?", reply_markup=markup)
         
#the archivist shows all his potential
@archivist.message_handler(commands=["help"])
def helpingArchivist(message):
   commandList = open(r"Utilities/help.txt", "r")
   commandList = commandList.read()
   sticker = open(r"Stickers/16.webp", "rb")
   archivist.send_message(message.chat.id, commandList)
   time.sleep(4)
   archivist.send_sticker(message.chat.id, sticker)
   sticker.close()
   
#lists of all the phrases the archivist can say when a button is pressed
command1Phrases = ["Alright, seems like I have to puke some terrors"]
command2Phrases = ["Pfft, as you desire"]
command3Phrases = ["Feeling funny, aren't we?", "I never liked funhouses..."]
command4Phrases = ["An existential crisis a day keeps the spooky terrors away"]
command5Phrases = ["Uhhh I think I've got the right one", "Hey, that's my boyfriend you're talking about, you don't wanna be smited, do you :)?"]
command6Phrases = ["Very well..."]

#if the archivist goes crazy, here's a list of all he can say
crazyMessages = ["ENOUGH", "Ohhhhh I am sure you'd like a statement now, well NO", "CEASLESS WATCHER, TURN YOUR GAZE UPON THIS WRETCHED THING",
"SUPPLEMENTAL: the little monster here is making me creazy, my descent into madness is imminent", "SUPPLEMENTAL: I can't bear it any longer, I have to get out of here",
"LOOK AT THE SKY, IT'S LOOKING BACK"]

#list of words you can't say in front of the archivist
swears = ["FUCK", "SHIT", "DICK", "ASS", "BITCH", "ASSHOLE", "BASTARD", "BULLSHIT", "CUNT", "COCKSUCKER", "COCK", "GODDAMN", "MOTHERFUCKER", "PRICK", "SLUT"]

#the archivist's way of simiting you when you swear
smites = [["Ceaseless Watcher!", "See this lie, this golden strand of falsehood", "Take it in your gaze and pull it, follow through its curves and twists and knots as it unravels all before you", " Unweave it now, its fear and its falsehood, its hidden teeth and the ones it wears so proudly", "Take all that it is and all that it has", "It", "Is", "Yours"],
["Ceaseless Watcher!", "Turn your gaze upon this wretched thing"], ["Ceaseless Watcher!", "Turn your gaze upon this thing and drink", "Your", "Fill"], 
["Ceaseless Watcher!", "Gaze upon this thing, this lost and broken splinter of fear", "Take what is left of it as your own and leave no trace of it behind", "It", "Is", "Yours"]
]

#the archivist's answers for your existential questions
ominousAnswers = ["The short answer is I don't know Martin"]

#counts how many elements are there in a folder
def countFolder(commandFolder):
   dir_path = fr'{commandFolder}'
   count = 0
   for path in os.listdir(dir_path):
      if os.path.isfile(os.path.join(dir_path, path)):
         count += 1
   return count

#if there are too many messages
def tooMuch(message):
   now = datetime.datetime.now()
   global count, startTime, crash
   if now.hour == startTime.hour and (now.minute == startTime.minute or now.minute == startTime.minute + 2): 
      count = count + 1
   else:
      count = 0
      startTime = datetime.datetime.now()
   if count >= 30 and crash != 1:
      return True
   else:
      return False

#the archivist will go crazy
def crazyArchivist(message):
   global count, crash, chill
   crash = 1
   actions = [None] * 15
   for i in range(0,14):
      actions[i] = random.randint(1,3)
   for action in actions:
      if chill == 1:
         break
      if action == 1:
         randomNum = random.randint(0, len(crazyMessages)-1)
         archivist.send_message(message.chat.id, crazyMessages[randomNum])
      if action == 2:
         randomNum = random.randint(1, countFolder("Stickers")-1)
         sticker = open(rf"Stickers/{randomNum}.webp", "rb")
         archivist.send_sticker(message.chat.id, sticker)
         sticker.close()
      if action == 3:
         randomNum = random.randint(1, countFolder("Fandompics"))
         photo = open(rf"Fandompics/{randomNum}.jpg", "rb")
         archivist.send_photo(message.chat.id, photo) 
         photo.close()
      time.sleep(3)
   time.sleep(30)
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_message(message.chat.id, "That... was not ideal")
   archivist.send_chat_action(message.chat.id, "typing")
   time.sleep(2)
   archivist.send_message(message.chat.id, "Now, where were we?")
   chill = 0
   crash = 0
   count = 0

#generates a random number to pick a random phrase from the lists at the beginning of the code amd send it
def randomizePhrase(commandNumberPhrases, message):
   randomNum = random.randint(0, len(commandNumberPhrases)-1)
   archivist.send_message(message.chat.id, commandNumberPhrases[randomNum])

#counts how many audios are there in the folder relative to the command, then generates a random number to pick a random audio and send it
def randomizeAudio(commandFolder, message):
   elementsNum = countFolder(commandFolder)
   randomNum = random.randint(1, elementsNum)
   audio = open(f"{commandFolder}/{randomNum}.mp3", "rb")
   archivist.send_chat_action(message.chat.id, "record_audio")
   archivist.send_audio(message.chat.id, audio)
   audio.close()

#checks if in the message there are words that are also in a sticker
def checkSticker(message):
   for title in titles:
        titleWords = title.split()
        for titleWord in titleWords:
            messageWords = message.text.split()
            for messageWord in messageWords:
                if len(messageWord)>2 and messageWord.upper() == titleWord:
                    return True
   return False

#checks if you are swearing
def swearing(message):
   message = message.text.upper().split()
   for word in message:
      if word in swears:
         return True
      else:
         return False

#checks if you're asking a question
def checkQuestion(message):
   message = message.text
   if "ARCHIVIST" in message.upper() and message[len(message)-1] == "?":
      return True
   else:
      return False

#enters the right folder and shows every audio in order to let the person choose one to receive
def chooseAudio(message, commandNumber):
   markup = InlineKeyboardMarkup()
   markup.row_width = 2
   elementsNum = countFolder(commandNumber)
   for element in range(1, elementsNum):
      title = eyed3.load(fr"{commandNumber}/{element}.mp3")
      title = title.tag.title
      markup.add(InlineKeyboardButton(f"{title}", callback_data=f"{commandNumber}/{element}"))
   archivist.send_message(message.message.chat.id, "Choose freely... if you can", reply_markup=markup) #Alright, let's see what we've got here

if crash != 1:
   #command 1: Ominous Speech
   @archivist.message_handler(func=lambda m:"OMINOUS SPEECH" in m.text.upper())
   def ominousSpeech(message):
      if crash == 1:
         return
      else: 
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command1Phrases, message)
            randomizeAudio("command1", message)
         else:
            crazyArchivist(message)

   #command 2: Random Monster Talking
   @archivist.message_handler(func=lambda m:"MONSTER TALKING" in m.text.upper())
   def randomMonster(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command2Phrases, message)
            randomizeAudio("command2", message)
         else:
            crazyArchivist(message)

   #command 3: Micheal Laughter
   @archivist.message_handler(func=lambda m:"MICHEAL LAUGHTER" in m.text.upper())
   def michealLaughter(message):
      if crash == 1:
         return 
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command3Phrases, message)
            randomizeAudio("command3", message)
         else:
            crazyArchivist(message)

   #command 4: Existential Crisis
   @archivist.message_handler(func=lambda m:"EXISTENTIAL CRISIS" in m.text.upper())
   def existentialCrisis(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command4Phrases, message)
            randomizeAudio("command4", message)
         else:
            crazyArchivist(message)

   #command 5: Insult @ Martin
   @archivist.message_handler(func=lambda m:"INSULT @ MARTIN" in m.text.upper())
   def insultMartin(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command5Phrases, message)
            randomizeAudio("command5", message)
         else:
            crazyArchivist(message)

   #command 6: Surprise Me
   @archivist.message_handler(func=lambda m:"SURPRISE ME" in m.text.upper())
   def surpriseMe(message):
      if crash == 1:
         return
      else: 
         crazy = tooMuch(message)
         if crazy == False:
            randomizePhrase(command6Phrases, message)
            randomizeAudio("command6", message)
         else:
            crazyArchivist(message)

   #the archivist loves to smite liars
   @archivist.message_handler(commands=["lies"])
   def youreLying(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            archivist.send_message(message.chat.id, smites[0][0])
            for i in range(1, len(smites[0])):
               if smites[0][i] == "It" or smites[0][i] == "Is" or smites[0][i] == "Yours":
                  archivist.send_chat_action(message.chat.id, "typing")
                  time.sleep(1)
                  archivist.send_message(message.chat.id, smites[0][i])
               else: 
                  archivist.send_chat_action(message.chat.id, "typing")
                  time.sleep(2)
                  archivist.send_message(message.chat.id, smites[0][i])
         else:
            crazyArchivist(message)

   #command to send a random sticker
   @archivist.message_handler(commands=["sticker"])
   def sendSticker(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomNum = random.randint(1, len(titles))
            sticker = open(rf"Stickers/{randomNum}.webp", "rb")
            archivist.send_sticker(message.chat.id, sticker)
            sticker.close()
         else:
            crazyArchivist(message)

   #command to send a poll
   @archivist.message_handler(commands=["quiz"])
   def sendPoll(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            polls = [
               ["Where is the Magnus Institute?", ["Zürich", "London", "Stockholm", "Las Vegas"], 1,"I just told you... dumb ass"],
               ["Who is Martin in love with?", ["Jon", "The Archivist", "Simon Fairchild", "Spiders", "Peter Lukas", "AlsoMartin"], 3, "I like spiders, especially the big ones..."],
               ["Where is Tim?", ["Chilling with Sasha in a cottage", "Dead, utterly, definetly dead", "Kayaking", "In prison for too much charisma"], 2, "HE'S KAYAKING OK?"]
               ]
            randomNum = random.randint(0, len(polls)-1)
            question = polls[randomNum][0]
            answers= polls[randomNum][1]
            correct = polls[randomNum][2]
            info = polls[randomNum][3]
            archivist.send_poll(message.chat.id, question, answers, is_anonymous=False, type="quiz", correct_option_id=correct, explanation=info)
         else:
            crazyArchivist(message)

   #command to make the archivist feel a bit better and stop acting crazy
   @archivist.message_handler(commands=["chill"])
   def chilling(message):
      global chill
      chill = 1
      
   #responses to the pressing of buttons to choose the audio
   @archivist.callback_query_handler(func=lambda call: "command1" == call.data)
   def command1Audio(message):
      chooseAudio(message, "command1")

   @archivist.callback_query_handler(func=lambda call: "command2" == call.data)
   def command2Audio(message):
      chooseAudio(message, "command2")

   @archivist.callback_query_handler(func=lambda call: "command3" == call.data)
   def command3Audio(message):
      chooseAudio(message, "command3")

   @archivist.callback_query_handler(func=lambda call: "command4" == call.data)
   def command4Audio(message):
      chooseAudio(message, "command4")

   @archivist.callback_query_handler(func=lambda call: "command5" == call.data)
   def command5Audio(message):
      chooseAudio(message, "command5")

   @archivist.callback_query_handler(func=lambda call: "command6" == call.data)
   def command6Audio(message):
      chooseAudio(message, "command6")

   #command to enter a selection mode for a specific audio track
   @archivist.message_handler(commands=["audio"])
   def selectSpecificAudio(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            markup = InlineKeyboardMarkup()
            markup.row_width = 2
            markup.add(InlineKeyboardButton("Ominous Speech", callback_data="command1"), 
                        InlineKeyboardButton("Monster Talking", callback_data="command2"),
                        InlineKeyboardButton("Micheal Laughter", callback_data="command3"),
                        InlineKeyboardButton("Existential Crisis", callback_data="command4"),
                        InlineKeyboardButton("Instul @ Martin", callback_data="command5"),
                        InlineKeyboardButton("Surprise Me", callback_data="command6"))
            archivist.send_message(message.chat.id, "Which of this suits the situation better?", reply_markup=markup)
         else:
            crazyArchivist(message)

   #if you send a message which contains only words that are also in a sticker the archivist will provide you the sticker
   @archivist.message_handler(func=checkSticker)
   def sendSpecificSticker(message):
      if crash == 1:
         return
      else: 
         crazy = tooMuch(message)
         if crazy == False:
            stickerNum = 1
            for title in titles:
               if message.text.upper() in title:
                  break
               else:
                  stickerNum += 1
            sticker = open(fr"Stickers/{stickerNum}.webp", "rb")
            archivist.send_sticker(message.chat.id, sticker)
            sticker.close()
         else:
            crazyArchivist(message)

   #the archivist doesn't allow swearing
   @archivist.message_handler(func=swearing)
   def sendPunishment(message):
      randomNum = random.randint(0, len(smites)-1)
      archivist.send_chat_action(message.chat.id, "typing")
      archivist.reply_to(message, smites[randomNum][0])
      for i in range(1, len(smites[randomNum])):
         if smites[randomNum][i] == "It" or smites[randomNum][i] == "Is" or smites[randomNum][i] == "Yours":
            archivist.send_chat_action(message.chat.id, "typing")
            time.sleep(1)
            archivist.send_message(message.chat.id, smites[randomNum][i])
         else: 
            archivist.send_chat_action(message.chat.id, "typing")
            time.sleep(2)
            archivist.send_message(message.chat.id, smites[randomNum][i])

   #the archivist is suspicious about links you send him 
   @archivist.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
   def command_url(message):
      archivist.reply_to(message, "I shouldn't open that url, should I?")

   #the archivist tries to answer your questions
   @archivist.message_handler(func=checkQuestion)
   def ominousAnswer(message):
      if crash == 1:
         return
      else:
         crazy = tooMuch(message)
         if crazy == False:
            randomNum = random.randint(0, len(ominousAnswers))
            if randomNum == len(ominousAnswers):
               sticker = open(r"Stickers/19.webp", "rb")
               archivist.send_sticker(message.chat.id, sticker)
               sticker.close()
            else:
               archivist.reply_to(message, ominousAnswers[randomNum])
         else:
            crazyArchivist(message)

#probably not the best way to implement this, open to suggestions
#################################################################################
   @archivist.callback_query_handler(func=lambda call: f"command1/1" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command1/1.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/1" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/1.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/2" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/2.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/3" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/3.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/4" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/4.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/5" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/5.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/6" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/6.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/7" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/7.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/8" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/8.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/9" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/9.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command2/10" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command2/10.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/1" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/1.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/2" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/2.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/3" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/3.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/4" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/4.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/5" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/5.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/6" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/6.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/7" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/7.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/8" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/8.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/9" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/9.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/10" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/10.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/11" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/11.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/12" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/12.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/13" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/13.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command3/14" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command3/14.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command4/1" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command4/1.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command4/2" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command4/2.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command4/3" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command4/3.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command4/4" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command4/4.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command4/5" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command4/5.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/1" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/1.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/2" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/2.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/3" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/3.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/4" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/4.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/5" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/5.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/6" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/6.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/7" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/7.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/8" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/8.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/9" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/9.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/10" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/10.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/11" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/11.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/12" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/12.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/13" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/13.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/14" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/14.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
   @archivist.callback_query_handler(func=lambda call: f"command5/15" == call.data)
   def audioOnTheWay(message):
      audio = open(fr"command5/15.mp3", "rb")
      archivist.send_chat_action(message.message.chat.id, "record_audio")
      archivist.send_audio(message.message.chat.id, audio)
      audio.close()
##################################################################################

keep_alive()
archivist.polling()