from tqdm import tqdm
from tqdm import tqdm
import requests as req
from datetime import date
import time
from time import gmtime,strftime
#1
def initiate_hack():
    for i in tqdm(range(100),desc="Hacking procces",colour="green"):
        time.sleep(0.05)
    print("Hacking granted!")

initiate_hack()
# 2
def get_status_of_request_from_wiki():
    response = req.get("https://ru.wikipedia.org")
    print(response.status_code)

get_status_of_request_from_wiki()
#3
def give_date():
    t = date.today()
    print(t)

give_date()
# 4
def give_time_info():
    s = strftime("%a, %d %b %Y %H:%M:%D",gmtime(1790798508.6496193))
    print(s)

give_time_info()
#5
def give_info_about_me():
    print("My name:Akyltai")
give_info_about_me()