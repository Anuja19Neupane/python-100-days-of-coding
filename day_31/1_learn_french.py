from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# yo agadi nei dekothyo

current_card={}
to_learn={}


# tick gareko word new file ma rakhda, hamile tyo file dlt garim vaney
# arko palta code run garda error dekhauxa so use try,except
try:
    data=pandas.read_csv("day_31/data/french_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("day_31/data/french_words.csv")
    print(original_data)
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
# dataframe lai dict ma convert gareko
# orient Defines which dtype to convert Columns(series into). 



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(2000,func=flip_card)
    # after ma 2000 milisecond ie. 2 sec paxi new word aauxa
    

def flip_card():
      canvas.itemconfig(card_title,text="English",fill="white") # fill le text color change garxa
      canvas.itemconfig(card_word,text=current_card["English"],fill="white")
      canvas.itemconfig(card_background,image=card_back_img)

# user le tick thicho vaney tyo word remove gardey because that means user already know what that word is in english
def is_known():
    to_learn.remove(current_card)
     # aba remove vayepaxi length of word ghatdei janxa 
    # but feri run garda feri 100 ota nei hunxa
    # # so lets solve this 
    data=pandas.DataFrame(to_learn)
    data.to_csv("day_31/data/words_to_learn.csv",index=False)
    # index false garda hamile run garepaxi tya column ko number thapidei jadaina
   # aba tick lagako word haru yo new file(words_to_learn.csv) aafei banera tya save hunxa
   # data.to_csv vaneko data csv ma change gar
   
    next_card()

  
     
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer= window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="day_31/images/card_front.png")
card_back_img=PhotoImage(file="day_31/images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="Title",font=("ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("ariel",60,"italic"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0) 
# hi highlightthickness=0 le white boarder line hatauxa
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="day_31/images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="day_31/images/right.png")
known_button=Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()