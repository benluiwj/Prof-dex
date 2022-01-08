# Image placeholder taken from : https://qph.fs.quoracdn.net/main-qimg-cf89e8e6daa9dabc8174c303e4d53d3a

import os

import telebot
import firebase_admin

from firebase_admin import credentials, firestore
from telebot.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from database import pokedex, profs, profs_name_list

my_secret = os.environ['API_KEY']
creds = os.environ['GOOGLE_CREDENTIALS_PATH']

CREDENTIALS = credentials.Certificate(creds)
firebase_admin.initialize_app(CREDENTIALS)
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)
db = firestore.client()

bot.set_my_commands([
    BotCommand('start', 'Starts the bot'),
    BotCommand('add', 'Unlock Professors information'),
    BotCommand('show', 'List all the Professors that have been found'),
    BotCommand('list', 'List all the Professors')
])


def request_start(chat_id):
    # the ensure that users start with /start
    if chat_id not in pokedex:
        bot.send_message(chat_id=chat_id,
                         text="Please start the bot by /start")

    return


@bot.message_handler(commands=['start'])
def start(message):
    """
  Command that welcomes the user and configures the initial setup
  """
  
    chatId = message.chat.id
    
    if message.chat.type != 'private' :
        bot.send_message(
            chat_id = chatId,
            text = 'Please add me to a private chat.'
        )
        return

    messageText = 'Welcome to Profédex'
    
    doc_ref = db.collection(message.chat.username)
    
    count = 0
    for doc in doc_ref.stream():
        if doc :
            count += 1
            break
    
    if count == 0:
        for prof, details in profs.items() :
            ref = doc_ref.document(prof)
            ref.set(details)
    
    
    
    # # Initialise pokedex, connection with database
    # pokedex[chatId] = dict()

    # for prof, details in profs.items():
    #     pokedex[chatId][prof] = details
    #     details['isFound'] = False

    bot.reply_to(message, messageText)


@bot.message_handler(commands=['add'])
def add(message):
    '''
  Command that unlocks the professors information
  '''
    chat_id = message.chat.id
    
    username = message.chat.username
    if not db.collection(username).get() :
        request_start(chat_id)
        return

    msg = message.text.split()[1:]
    prof_name = ""
    if msg :
        for i in range(len(msg)-1) :
            prof_name += msg[i] + ' '
        
        prof_name += msg[-1]
    
    prof_details = db.collection(username).document(prof_name).get()
    
    if prof_details.exists:
        messageText = f''
        prof_details = prof_details.to_dict()
        if not prof_details['isFound'] :
            db.collection(username).document(prof_name).set({'isFound' : True})
            messageText = f'Professor {prof_name} has been added to your Profédex'
        else:
            messageText = f'Professor {prof_name} has already been added to your Profédex'
    else :
        messageText = f'Professor {prof_name} does not exist.'
    bot.reply_to(message, messageText)


@bot.message_handler(commands=['show'])
def show(message):
    '''
  Command that lists found professors information
  '''
    chat_id = message.chat.id
    username = message.chat.username
    if not db.collection(username).get() :
        request_start(chat_id)
        return

    chat_text = ""
    count = 0

    buttons = []
    for i in range(len(profs_name_list)):
        row = []
        profName = profs_name_list[i]
        if db.collection(username).document(profName).get().to_dict()['isFound']:
          count += 1
          button = InlineKeyboardButton(
            str(i+1) + '. ' + profName,
            callback_data = 'view ' + profName)
   
          row.append(button)
          buttons.append(row)

    if count == 0:
      chat_text = "No Professors have been found yet"
    else :
      chat_text = "Select a Professor that has been found before"
          
    bot.send_message(chat_id=chat_id,
                     text=chat_text,
                     reply_markup=InlineKeyboardMarkup(buttons))
          

@bot.message_handler(commands=['list'])
def rangeList(message):
    '''
  Command that lists the professors information
  '''
    chat_id = message.chat.id
    username = message.chat.username
    if not db.collection(username).get() :
        request_start(chat_id)
        return

    chat_text = "Select a Professor below"

    placeHolder = "?????????"
    buttons = []
    for i in range(len(profs_name_list)):
        row = []
        profName = profs_name_list[i]
        if db.collection(username).document(profName).get().to_dict()['isFound'] :
          button = InlineKeyboardButton(
            str(i+1) + '. ' + profName,
            callback_data = 'view ' + profName
            )  
        else :
          button = InlineKeyboardButton(
            placeHolder,
            callback_data = 'view ' + profName
            )  
          
        row.append(button)
        buttons.append(row)
    bot.send_message(chat_id=chat_id,
                     text=chat_text,
                     reply_markup=InlineKeyboardMarkup(buttons))



@bot.callback_query_handler(func=lambda call: True)
def handleCallback(call):
    """
    Handles the execution of the respective functions upon receiving callback query
    """
    chatId = call.message.chat.id
    username = call.message.chat.username
    data = call.data

    # callback data 'view <prof  id>'
    # intent = 'view'
    # query = 'detail'

    # callback data 'range 1 - 10'

    # callbck data 'view <prof id>'

    information = data.split()

    intent, data = information[0], information[1:]

    if intent == 'view':
        viewItemDetails(chatId, data, username)
        return


def viewRange(chatId, data, username):
    # do some stuff
    if not db.collection(username).get() :
        request_start(chatId)
        return

    start, end = int(data[0]), int(data[-1])
    placeHolder = "?????????"
    buttons = []
    for i in range(start-1, end):
        row = []
        profName = profs_name_list[i]
        if db.collection(username).document(profName).get().to_dict()['isFound'] :
          button = InlineKeyboardButton(
            str(i+1) + '. ' + profName,
            callback_data = 'view ' + profName
            )  
        else :
          button = InlineKeyboardButton(
            placeHolder,
            callback_data = 'view ' + profName
            )  
          
        row.append(button)
        buttons.append(row)

    bot.send_message(
        text = 'Index ' + str(start) + ' to ' + str(end) + ' shown',
        chat_id = chatId,
        reply_markup = InlineKeyboardMarkup(buttons)
    )

def viewItemDetails(chatId, data, username):
    """
    Displays details in a markdown format
    """
    if not db.collection(username).get() :
        request_start(chatId)
        return
        
    profName = ""
    for i in range(len(data)-1) :
        profName += data[i] + ' '
    
    profName += data[-1]
    profDetails = db.collection(username).document(profName).get().to_dict()
    id = profDetails['ID']
    subtitle = profDetails['Subtitle'].value
    description = profDetails['Description']
    types = ''
    for i in range(len(pokedex[chatId][profName]['Type']) - 1) :
        types += profDetails['Type'][i].value + ', '
    types += profDetails['Type'][-1].value
    location = profDetails['Location']
    image = profDetails['Image']
    isFound = profDetails['isFound']

    placeHolder = "?????????"

    if not isFound:
        profName = placeHolder
        subtitle = placeHolder
        description = placeHolder
        types = placeHolder
        location = placeHolder
        image = 'https://qph.fs.quoracdn.net/main-qimg-cf89e8e6daa9dabc8174c303e4d53d3a'

    display = (f'ID : {id}\n'
               f'{profName} - {subtitle}\n\n'
               f'Research Areas : {types}\n'
               f'Location : {location}\n\n'
               f'{description}'
               )

    bot.send_photo(
        chatId,
        image,
        caption=display,
    )


bot.infinity_polling()
