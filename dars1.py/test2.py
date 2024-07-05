#1
import datetime as dt
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2024, 7, 6)
print(f"Ertangi sana: {ertaga}")
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
vaqtKeyin = dt.time(23,45,00)

#2
bugun = dt.date.today()
ramazon = dt.date(2024, 4, 10)
farq = ramazon-bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi")

#3
hozir = dt.datetime.now()
futbol = dt.datetime(2023, 3, 10, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

#4
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)

#5
import re
word1 = "темир"
word2 = "томир"
word3 = "тулпор"
andoza = "^т...р"
print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

#6
matn = """Maqolalar  2023-yilning 20-martiga qadar jonibekdev@gmail.com elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

#7
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '
while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")

