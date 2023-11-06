from tkinter import *
import psycopg2
import random

"""window wordt aangemaakt. achtergrond is een screenshot van figma. achtergrond wordt in lijst gezet vanwege
het openen van een aparte acchtergrond met nieuwe widgets. Dit werkt niet als je achtergrondimage niet in een
lijst zet."""

window = Tk()
window.geometry("642x400")
window.resizable(False, False)

window.title("inlogscherm")
icon = PhotoImage(file="nslogo.png")
window.iconphoto(True, icon)

canvas = Canvas(window, bg='#FFFFFF', width=642, height=400)
canvas.pack()
all_images = []
all_images.append(PhotoImage(file="inlogscherm.png"))
all_images.append(PhotoImage(file="controleerscherm.png"))
canvas.create_image(0, 0, image=all_images[0], anchor=NW)

inloggen_text = Label(window, text="inloggen", font=("Open Sans", 25, "bold"), bg="#FFC917")
inloggen_text.place(x=40, y=82, height=60, width=145)

email_text = Label(window, text="Emailadres", font=("Open Sans", 16, "bold"), bg="#FFC917")
email_text.place(x=32, y=200, height=20, width=142)

wachtwoord_test = Label(window, text="Wachtwoord", font=("Open Sans", 16, "bold"), bg="#FFC917")
wachtwoord_test.place(x=40,y=270, height=20, width=142)

email_input = Text(window, bg="#dedbde", font=("Arial", 12))
email_input.place(x=210, y=200, height=25, width=410)

wachtwoord_input = Entry(window, bg="#dedbde", font=("Arial", 12), show="*")
wachtwoord_input.place(x=210, y=270, height=25, width=410)

foutmelding_text = Label(window, text="", font=("Arial, 10"), bg="#FFC917", fg="red")
foutmelding_text.place(x=210,y=300,height=20,width=400)

"""korte functie voor het lezen van de lijn. Vervolgens alles splitten om gemakkelijk tot de waardes
te kunnen komen."""


def read_message():
    with (open("output.txt", "r") as f):
        line = f.readline()
        words = line.split(";")
        return words


"""Kiezen van willekeurig station van de lijst met aangeboden stations."""


def kies_station():
    with open("stations.txt", "r") as f:
        lines = f.readlines()
        random_station = random.choice(lines)
        return random_station


"""twee aparte functies voor het goedkeuren en afkeuren van berichten. Enige verschil is het bericht 'goedkeuren'
of 'afkeuren'. waardes uit bovenstaande functies worden opgenomen met id van moderator die inlogt om window te openen.
alle waardes worden naar berichten table in postgres geschreven. f.write wordt gebruikt om textfile leeg te halen."""


def goedkeuren():
    conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
    cur = conn.cursor()
    gekozen_station = kies_station()
    lijn = read_message()
    insert_table = """INSERT INTO berichten(naam, bericht, station, datum, tijd, status, moderator) 
    VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    insert_value = (lijn[1], lijn[3], gekozen_station, lijn[5], lijn[6], "goedgekeurd", lijn[7])
    cur.execute(insert_table, insert_value)
    conn.commit()
    cur.close()
    conn.close()

    with open("output.txt", "w") as f:
        f.write("")


def afkeuren():
    conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
    cur = conn.cursor()
    gekozen_station = kies_station()
    lijn = read_message()
    insert_table = """INSERT INTO berichten(naam, bericht, station, datum, tijd, status, moderator) 
    VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    insert_value = (lijn[1], lijn[3], gekozen_station, lijn[5], lijn[6], "afgekeurd", lijn[7])
    cur.execute(insert_table, insert_value)
    conn.commit()
    cur.close()
    conn.close()

    with open("output.txt", "w") as f:
        f.write("")


"""email van moderator wordt opgehaald, hier wordt later het mod id ook opgehaald. als email en wachtwoord kloppen
volgens database, wordt mod_id naar lijn geschreven. Vervolgens worden alle widgets van het window verwijderd en
vervangen door nieuwe widgets. Later in de functie wordt x variabele aangemaakt om button te disablen als er geen
beschikbare berichten zijn. met clear_screen wordt het bericht van het scherm gehaald als dit beoordeeld is."""


def open_window():
    email = email_input.get(1.0, "end-1c")
    wachtwoord = wachtwoord_input.get()
    conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("SELECT * from moderators")
    info = cur.fetchall()
    for i in info:
        if i[2] == email:
            mod_id = i[0]
            with open("output.txt", "r+") as f:
                lines = f.readlines()
                lines[-1] += str(mod_id) + ";"
                f.seek(0)
                f.writelines(lines)
                f.truncate()
        for y in info:
            if y[2] == email and y[3] == wachtwoord:
                for widget in window.winfo_children():
                    if widget != foutmelding_text:
                        widget.destroy()
                    window.title("controleerscherm")
                    window.geometry("800x486")
                    canvas2 = Canvas(window, bg="#0063D3", width=800, height=486)
                    canvas2.pack()
                    canvas2.create_image(0, 0, image=all_images[1], anchor=NW)

                    controleer_text = Label(window, text="Controle-scherm", bg="#FFC917",
                                            font=("Open Sans", 30, "bold"))
                    controleer_text.place(x=62, y=50, width=400, height=100)
                    bericht_text = Label(window, text="Bericht", bg="#FFC917",
                                            font=("Arial", 18))
                    bericht_text.place(x=43,y=180, width=140, height=80)
                    naam_text = Label(window, text="Naam", bg="#FFC917",
                                      font=("Arial", 18))
                    naam_text.place(x=35,y=280,width=140,height=80)
                    datum_en_tijd_text = Label(window,text="Datum en tijd", bg="#FFC917",
                                               font=("Arial", 18))
                    datum_en_tijd_text.place(x=43,y=380,height=80,width=200)


                with open("output.txt", "r") as file:
                    line = file.readline()
                    words = line.split(";")
                    x = False
                    if line != "":
                        output_bericht = Label(window, text=words[3], bg="#D9D9D9",
                                               font=("Arial", 14), anchor=NW, wraplength=500,
                                               justify="left")
                        output_bericht.place(x=243, y=180, height=100, width=500)
                        output_naam = Label(window, text=words[1], bg="#D9D9D9",
                                            font=("Arial", 14), anchor=NW)
                        output_naam.place(x=243, y=300, height=35, width=500)
                    else:

                        output_bericht = Label(window, text="geen beschikbare berichten", bg="#D9D9D9",
                                               font=("Arial", 14), anchor=NW, wraplength=500,
                                               justify="left")
                        output_bericht.place(x=243, y=180, height=100, width=500)
                        output_naam = Label(window, text="", bg="#D9D9D9",
                                            font=("Arial", 14), anchor=NW)
                        output_naam.place(x=243, y=300, height=35, width=500)
                        x = True

                    output_datetime = Label(window, text= f"{words[5]} {words[6]}",
                                             font=("Arial", 14), anchor=NW, bg="#D9D9D9")
                    output_datetime.place(x=243,y=400,height=35,width=180)

                    def clear_screen():
                        output_bericht.config(text="")
                        output_naam.config(text="")

                    def approve():
                        goedkeuren()
                        clear_screen()

                    def deny():
                        afkeuren()
                        clear_screen()

                    approve_button = Button(window, text="Goedkeuren", font=("Open Sans", 14,
                                            "bold"), bg="#0063D3", command=approve, fg="white")
                    approve_button.place(x=440, y=380, height=80, width=150)

                    deny_button = Button(window, text="Afkeuren", font=("Open Sans", 14,
                                            "bold"), bg="#0063D3", command=deny, fg="white")
                    deny_button.place(x=620, y=380, height=80, width=150)

                    if x:
                        deny_button.config(state=DISABLED)
                        approve_button.config(state=DISABLED)


def loginknop():
    open_window()


login_button = Button(window,text="Log in", font=("Open Sans", 16, "bold"), bg="#0063D3", fg="white",
                      activebackground="#0063D3", activeforeground="white",command=loginknop)
login_button.place(x=332,y=350, height=40,width=200)


window.mainloop()


"""
bronnen mod2: 
https://www.youtube.com/watch?v=M2NzvnfS-hI : connect met postgresql via python
https://www.figma.com/ : bouwen van een basis voor tkinter
https://www.youtube.com/watch?v=TuLxsvK4svQ : tkinter tutorial
https://www.ns.nl/platform/fundamentals/colours.html : kleurencode
hulp in klas : lijn 19-21. Hoe de background image te laten werken na alle widgets verwijderd te hebben.
"""

