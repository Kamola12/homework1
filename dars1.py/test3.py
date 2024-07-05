#1
from googletrans import Translator
tarjimon = Translator() 
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)


#2
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)
tarjima_uz = tarjimon.translate(matn_en, src='uz', dest='uz')


#3
import requests
from pprint import pprint
manzil= "https://kun.uz/news/main"
r = requests.get(manzil)
pprint(r.text)


#4
import requests
from pprint import pprint as print
API_KEY = ''
currency='USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
response = requests.get(url)
kurs = response.json()['conversion_rate']
print(f"1 dollar kursi {kurs} so'mga teng")


#5
import requests
from bs4 import BeautifulSoup
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title") 
print(news[0].text) 


#6
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
matn=""
for n in news:
    matn += n.text
stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
wordcloud = WordCloud(width = 1000, height = 1000, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 20).generate(matn)                       
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 
