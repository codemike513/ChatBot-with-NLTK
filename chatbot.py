from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is MikeBot, I'm a chatbot.", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "I'm great !", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["Mihir Pesswani created me using Python's NLTK Library.", "Top secret", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Khandwa (M.P.), India', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2",
            "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket", ]
    ],
    [
        r"who (.*) (cricketer|batsman)?",
        ["Sachin Tendulkar and Rohit Sharma"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ",
            "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]
# Default Message
print('\n\nHello I\'m MikeBot and I like to chat.\n\nPlease type in Lowercase English Language to start a conversation. Type quit to leave.')

# Create Chat Bot
chat = Chat(pairs, reflections)

# Start Conversation
chat.converse()
