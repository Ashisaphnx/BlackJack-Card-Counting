'''This is a waste of time'''
COUNT = 0
CARDS_ON_TABLE = 0
MAX_CARDS = 208
print ("Hi")
def ask_card():
    '''Will ask for the avalible cards on the table'''
    card = input("What is your card: ")
    print (card)
    if card == "A":
        count = count +0
    elif card == "J":
        count = count -2
    elif card == "Q":
        count = count -2
    elif card == "K":
        count = count -2
    elif card == "10":
        count = count -2
    elif card == "2":
        count = count +1
    elif card == "3":
        count = count +1
    elif card == "4":
        count = count +2
    elif card == "5":
        count = count +2
    elif card == "6":
        count = count +2
    elif card == "7":
        count = count +1
    elif card == "8":
        count = count +0
    elif card == "9":
        count = count -1
    else :
        count = 0
    print (count)
    true_count = count / 4
    if count >=4:
        print (true_count)

while CARDS_ON_TABLE <= MAX_CARDS:
    ask_card()
    CARDS_ON_TABLE = CARDS_ON_TABLE +1
