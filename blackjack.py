import random
import tkinter

mainWindow = tkinter.Tk()


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop()
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)


# Set up screen and frames for dealer and player
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)

card_frame = tkinter.Frame(mainWindow, relief="sunken",
                           borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green",
              fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green",
              fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green",
              fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green",
              fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create a deck and shuffle cards
deck = list(cards)
random.shuffle(deck)

# create list to store dealer and players hands
dealer_hand = []
player_hand = []

mainWindow.mainloop()
