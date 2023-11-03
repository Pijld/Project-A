from tkinter import *
import psycopg2
import random

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

def read_message():
    with (open("output.txt", "r") as f):
        lines = f.readlines()
        line = lines[-1] if lines else None
        words = line.split(";")
        return words


def kies_station():
    with open("stations.txt", "r") as f:
        lines = f.readlines()
        random_station = random.choice(lines)
        return random_station


# def mod():
#     moderator = email_input.get(1.0, 'end-1c')
#     with open("Moderators.txt", "r") as f:
#         for line in f:
#             words = line.split(";")
#             if str(words[1]).strip() == str(moderator):
#                 mod_id = words[3]
#                 return mod_id

def goedkeuren():
    with open("output.txt", "r+") as f:
        conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
        cur = conn.cursor()
        lines = f.readlines()
        lines[-1] += "goedgekeurd\n"
        f.seek(0)
        mod_id = None
        f.writelines(lines)
        gekozen_station = kies_station()
        lijn = read_message()
        insert_table = """INSERT INTO berichten(naam, bericht, station, datum, tijd, status, moderator) 
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        insert_value = (lijn[1], lijn[3], gekozen_station, lijn[5], lijn[6], "goedgekeurd", mod_id)
        cur.execute(insert_table, insert_value)

        conn.commit()
        cur.close()
        conn.close()

def afkeuren():
    with open("output.txt", "r+") as f:
        conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
        cur = conn.cursor()
        lines = f.readlines()
        lines[-1] += "afgekeurd\n"
        f.seek(0)
        mod_id = None
        f.writelines(lines)
        f.truncate()
        gekozen_station = kies_station()
        lijn = read_message()
        insert_table = """INSERT INTO berichten(naam, bericht, station, datum, tijd, status, moderator) 
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        insert_value = (lijn[1], lijn[3], gekozen_station, lijn[5], lijn[6], "afgekeurd", mod_id)
        cur.execute(insert_table, insert_value)

        conn.commit()
        cur.close()
        conn.close()




def open_window():
    email = email_input.get(1.0, "end-1c")
    wachtwoord = wachtwoord_input.get()
    with open("moderators.txt", "r") as f:
        for line in f:
            words = line.strip().split(";")
            if words[1].strip() == email and words[2].strip() == wachtwoord:
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
                    lines = file.readlines()
                    last_line = lines[-1]
                    words = last_line.split(";")
                    x = False
                    print(words[7])
                    if words[7].strip() != "afgekeurd" and words[7].strip() != "goedgekeurd":
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
                    output_datetime.place(x=243,y=400,height=35,width=180)jqwjn

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


login_button = Button(window,text="Log in", font=("Open Sans", 16, "bold"), bg="#0063D3", fg="white",
                      activebackground="#0063D3", activeforeground="white",command=open_window)
login_button.place(x=332,y=350, height=40,width=200)


window.mainloop()


#bron end-1c chat gpt. betekent, end -1 character, om nieuwe line weg te halen.
