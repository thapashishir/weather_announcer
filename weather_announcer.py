import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.weather-forecast.com/locations/Kathmandu/forecasts/latest")
soup = BeautifulSoup(page.content, 'html.parser')
msg=soup.find("span", {"class": "phrase"}).contents
print(msg)

from gtts import gTTS
import os
from pathlib import Path
#home dir of os
HOME_DIR = str(Path.home())

mytext = str(msg)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(os.path.join(HOME_DIR,"weather.mp3"))
os.system("start "+os.path.join(HOME_DIR,"weather.mp3"))


