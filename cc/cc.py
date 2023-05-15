'''This is a waste of time'''
COUNT = 0
CARDS_ON_TABLE = 0
MAX_CARDS = 208
print ("Hi")

def ask_card():
    '''Will ask for the available cards on the table'''
    card = input("What is your card: ")
    print (card)
    try:
        card_value = {
            "A": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": -1,
            "J": -1,
            "Q": -1,
            "K": -1
        }[card]
    except KeyError:
        print("Invalid card")
        return

    COUNT += card_value
    print (COUNT)
    true_count = COUNT / 4
    if COUNT >=4:
        print (true_count)

while CARDS_ON_TABLE <= MAX_CARDS:
    CARDS_ON_TABLE += 1
    ask_card()
