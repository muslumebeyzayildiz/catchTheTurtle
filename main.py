import time
import turtle
import random

turtleScreen= turtle.Screen()
turtleScreen.title("Tosbigi yakala")
turtleScreen.bgcolor("pink")

tosbik = turtle.Turtle()
tosbik.shape("turtle")
tosbik.penup()  # çizmeden gitsin

# Sayaç değişkeni ve yazı nesnesi
tik_sayisi = 0
sayac_turtle = turtle.Turtle()
sayac_turtle.penup()
sayac_turtle.hideturtle()
sayac_turtle.goto(0, 200)  # Sayacı yukarıda göstermek için


def sayaci_guncelle():
    sayac_turtle.clear()
    sayac_turtle.write(f"Tıklama Sayısı: {tik_sayisi}", align="center", font=("Arial", 16, "bold"))

def tiklandi(x, y):
    global tik_sayisi
    tik_sayisi += 1
    sayaci_guncelle()


def rastgele_konum():
    width=turtleScreen.window_width()
    height=turtleScreen.window_height()
    x = random.randint(-width//2, width//2)
    y = random.randint(-height//2, height // 2)
    tosbik.goto(x, y)

saniye = 15
baslangic_zamani = time.time()#başlangıç zamanını alıyor ŞU ANKİ ZAMAN
bitis_zamani = baslangic_zamani + saniye

while time.time() < bitis_zamani:
    rastgele_konum()
    time.sleep(2)


tosbik.onclick(tiklandi)
sayaci_guncelle()

turtle.listen()
turtle.mainloop()#devamlı çalışan bir döngü eş zamanlı kontrol, saniyede binlerce kez kontrol.
#time.sleep bloklardı bunu