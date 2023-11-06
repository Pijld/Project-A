import datetime
import requests
import random
from tkinter import *
import psycopg2


window = Tk()
window.geometry("949x628")
window.title("Nederlandse spoorwegen")
window.resizable(False, False)
icon = PhotoImage(file="nslogo.png")
window.iconphoto(True, icon)
canvas = Canvas(window,bg="#FFFFFF", width=1155, height=745)
canvas.pack()
background = PhotoImage(file="bg mod3.png")
canvas.create_image(0, 0, image=background, anchor=NW)

conn = psycopg2.connect(host="20.229.131.82", dbname="project DP", user="postgres", password="postgres")
cur = conn.cursor()

cur.execute("SELECT * from station_service")
station_service = cur.fetchall()
random_station = random.choice(station_service)

cur.execute("SELECT bericht FROM berichten ORDER BY id DESC limit 1")
res1 = cur.fetchone()
if res1 is not None:
    message1 = res1[0]
else:
    message1=""

cur.execute("SELECT bericht FROM berichten ORDER BY id DESC limit 1 OFFSET 1")
res2 = cur.fetchone()
if res2 is not None:
    message2 = res2[0]
else:
    message2=""

cur.execute("SELECT bericht FROM berichten ORDER BY id DESC limit 1 OFFSET 2")
res3 = cur.fetchone()
if res3 is not None:
    message3 = res3[0]
else:
    message3=""

cur.execute("SELECT bericht FROM berichten ORDER BY id DESC limit 1 OFFSET 3")
res4 = cur.fetchone()
if res4 is not None:
    message4 = res4[0]
else:
    message4=""

cur.execute("SELECT bericht FROM berichten ORDER BY id DESC limit 1 OFFSET 4")
res5 = cur.fetchone()
if res5 is not None:
    message5 = res5[0]
else:
    message5=""

cur.execute("SELECT naam FROM berichten ORDER BY id DESC limit 1 OFFSET 4")
n5 = cur.fetchone()
if n5 is not None:
    textnaam5 = n5[0] + " zegt: "
else:
    textnaam5=""

cur.execute("SELECT naam FROM berichten ORDER BY id DESC limit 1 OFFSET 3")
n4 = cur.fetchone()
if n4 is not None:
    textnaam4 = n4[0] + " zegt: "
else:
    textnaam4=""

cur.execute("SELECT naam FROM berichten ORDER BY id DESC limit 1 OFFSET 2")
n3 = cur.fetchone()
if n3 is not None:
    textnaam3 = n3[0] + " zegt: "
else:
    textnaam3=""

cur.execute("SELECT naam FROM berichten ORDER BY id DESC limit 1 OFFSET 1")
n2 = cur.fetchone()
if n2 is not None:
    textnaam2 = n2[0] + " zegt: "
else:
    textnaam2=""

cur.execute("SELECT naam FROM berichten ORDER BY id DESC limit 1")
n1 = cur.fetchone()
if n1 is not None:
    textnaam1 = n1[0] + " zegt: "
else:
    textnaam1=""

welkomtext = Label(window, text= f"Welkom in {random_station[0]}", bg="#FFC917",
                   font=("Open Sans", 25, "bold"))
welkomtext.place(x=22, y=21, width=700, height=36)

if random_station[2] and random_station [3]:
    icon1 = PhotoImage(file="img_ovfiets.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670, y=500)
    icon2 = PhotoImage(file="img_lift.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)
elif random_station[3] and random_station[4]:
    icon1 = PhotoImage(file="img_lift.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670,y=500)
    icon2 = PhotoImage(file="img_toilet.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)
elif random_station[2] and random_station[4]:
    icon1 = PhotoImage(file="img_ovfiets.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670,y=500)
    icon2 = PhotoImage(file="img_toilet.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)
elif random_station[3] and random_station[5]:
    icon1 = PhotoImage(file="img_lift.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670,y=500)
    icon2 = PhotoImage(file="img_pr.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)
elif random_station[2] and random_station[5]:
    icon1 = PhotoImage(file="img_ovfiets.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670,y=500)
    icon2 = PhotoImage(file="img_pr.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)
elif random_station[4] and random_station[5]:
    icon1 = PhotoImage(file="img_toilet.png")
    label_icon1 = Label(window, image=icon1, width=100, height=100)
    label_icon1.place(x=670,y=500)
    icon2 = PhotoImage(file="img_pr.png")
    label_icon2 = Label(window, image=icon2, width=100, height=100)
    label_icon2.place(x=790, y=500)


msg1 = Label(window, wraplength=500, text=message1, bg="#D9D9D9", font=("Arial", 12))
msg1.place(x=20, y=141, width=565, height=64)

msg2 = Label(window, wraplength=500, text=message2, bg="#D9D9D9", font=("Arial", 12))
msg2.place(x=20, y=242, width=565, height=64)

msg3 = Label(window, wraplength=500, text=message3, bg="#D9D9D9", font=("Arial", 12))
msg3.place(x=20, y=348, width=565, height=64)

msg4 = Label(window, wraplength=500, text=message4, bg="#D9D9D9", font=("Arial", 12))
msg4.place(x=20, y=454, width=565, height=64)

msg5 = Label(window, wraplength=500, text=message5, bg="#D9D9D9", font=("Arial", 12))
msg5.place(x=20, y=555, width=565, height=64)


name1 = Label(window, text=textnaam1, bg="#D9D9D9", font=("Arial", 12))
name1.place(x=20, y=112, width=565, height=23)

name2 = Label(window, text=textnaam2, bg="#D9D9D9", font=("Arial", 12))
name2.place(x=20, y=213, width=565, height=23)

name3 = Label(window, text=textnaam3, bg="#D9D9D9", font=("Arial", 12))
name3.place(x=20, y=316, width=565, height=24)

name4 = Label(window, text=textnaam4, bg="#D9D9D9", font=("Arial", 12))
name4.place(x=20, y=422, width=565, height=24)

name5 = Label(window, text=textnaam5, bg="#D9D9D9", font=("Arial", 12))
name5.place(x=20, y=524, width=565, height=24)

conn.commit()
cur.close()
conn.close()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "32e968cba5609635f6b394a9b4b4b3ea"
CITY = random_station[0]

URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=metric"
response = requests.get(URL).json()

temp_celcius = response['main']['temp']
response_icon = response['weather'][0]['icon']
weather_type = response['weather'][0]['main']
feels_like = response['main']['feels_like']
current_time = datetime.datetime.now()
date = current_time.date()
time = current_time.strftime("%H:" + "%M")


iconweather = PhotoImage(file=f"weather_icons\\{response_icon}.png")
label_iconweather = Label(window, image=iconweather)
label_iconweather.place(x=737,y=382, height=75, width=75)

date_label = Label(window, text=str(date), font=("Arial", 16), bg="#D9D9D9")
date_label.place(x=671, y=152, width=213, height=36)

time_label = Label(window, text=str(time), font=("Arial", 16), bg="#D9D9D9")
time_label.place(x=671, y=197, width=213, height=36)

weather_type_label = Label(window, text=str(weather_type), font=("Arial", 16), bg="#D9D9D9")
weather_type_label.place(x=671, y=242, width=213, height=36)

temp_label = Label(window, text=f"temperatuur: ℃{str(temp_celcius)}", font=("Arial", 16), bg="#D9D9D9")
temp_label.place(x=671, y=287, width=213, height=36)

feels_like_label = Label(window, text=f"Voelt als: ℃{str(feels_like)}", font=("Arial", 16), bg="#D9D9D9")
feels_like_label.place(x=671, y=332, width=213, height=36)





window.mainloop()

