import datetime
from tkinter import *

"""aanmaken van window en hier te widgets in toevoegen. screenshot van figma gebruikt als achtergrond op canvas."""

window = Tk()
window.title('voer uw bericht in')

icon = PhotoImage(file="nslogo.png")
window.iconphoto(True, icon)

window.geometry('960x470')
window.resizable(False, False)

canvas = Canvas(window, bg='#FFFFFF', width=960, height=460)
canvas.pack()
all_images = []
all_images.append(PhotoImage(file="achtergrond.png"))  # 0
canvas.create_image(0, 0, image=all_images[0], anchor=NW)


deel_ervaring = Label(window, height=1, width=22, text="Deel uw ervaring",
                      font=("Open Sans", 22, "bold"), bg="#FFC917")
deel_ervaring.place(x=295,y=41)

vraag_naam = Label(window, height=1, width=22, text="Laat hier uw naam achter:",
                   font=("Open Sans", 16, "bold"), bg="#FFC917")
vraag_naam.place(x=220,y=133)

schrijf_bericht = Label(window, height=1, width=34, text="Schrijf hier het bericht dat u wilt achterlaten:",
                   font=("Open Sans", 16, "bold"), bg="#FFC917")
schrijf_bericht.place(x=152,y=259)

entry_naam = Entry(window, bg="#dedbde", font=("Arial", 15))
entry_naam.place(x=109,y=167,height=57,width=530)

text_message = Text(window, bg="#dedbde", font=("Arial", 13))
text_message.place(x=109, y=293, height=142, width=530)

warning_message = Label(window, text="", font=("Arial", 10), bg="#FFC917", fg="red")
warning_message.place(x=152, y=443, height=15, width=441)


"""anoniemfunctie aangemaakt met checkbutton. x gebruikt intvar om status van checkbutton te controleren. als waarde
van x 1 is, word naam vak leeggemaakt later in een aparte functie gezet, als textvak leeg is, wordt naam 'anoniem'"""

def anoniemfunction():
    if(x.get()==1):
        entry_naam.delete(0,END)
        entry_naam.config(state=DISABLED)
    elif(x.get()==0):
        entry_naam.config(state=NORMAL)


x = IntVar()
checkbutton = Checkbutton(window,text="Anoniem", font=("Open Sans",13,"bold"),height=2,width=15,
                        bg="#0063D3", fg="black", selectcolor="white", activebackground="#0063D3",
                        activeforeground="black", variable=x, onvalue=1, offvalue=0, command=anoniemfunction)
checkbutton.place(x=700,y=171)

"""Gebruik de datetime import om de huidige datum en tijd te bepalen om in textfile te zetten. 
bericht dat in textfile gezet wordt uit messagebox gehaald. Er wordt gecontroleerd of lengte van bericht voldoet aan
eisen, anders krijgt gebruiker een waarschuwingsbericht. Functie wordt in button gezet."""

def verstuur_message():
    current_time = datetime.datetime.now()
    real_date = current_time.date()
    real_time = current_time.strftime("%H:" + "%M")
    max_character = 140
    min_character = 1

    name = entry_naam.get()
    if name == "":
        name = "Anoniem"

    message = text_message.get(1.0,END).strip()

    if min_character <= len(str(message)) <= max_character:
        with open("output.txt", "a") as f:
            f.write(f"name ;{str(name)}; message ;{str(message)}; datetime ;{real_date};{real_time};")
            entry_naam.delete(0, END)
            text_message.delete(1.0, END)
            warning_message.config(text="")
    else:
        warning_message.config(text="Voer een bericht van minimaal 1 karakter en maximaal 140 karakters in")


verstuur_button = Button(window,text="Verstuur", font=("Open Sans",13,"bold"),
                         bg="#0063D3", fg="black", activeforeground="black", activebackground="#0063D3",
                         command=verstuur_message)
verstuur_button.place(x=700,y=320, height=70, width=179.5)

window.mainloop()


"""
Bronnen mod1:
https://www.youtube.com/watch?v=M2NzvnfS-hI : connect met postgresql via python
https://www.figma.com/ : bouwen van een basis voor tkinter
https://www.youtube.com/watch?v=TuLxsvK4svQ : tkinter tutorial
https://www.ns.nl/platform/fundamentals/colours.html : kleurencode
"""