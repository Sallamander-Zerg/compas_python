from itertools import count
from dadata import Dadata
import sqlite3
con = sqlite3.connect('local.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DadataUsers (Dadata_URL_servis,programming_language,token,key)''')
def database(lang,token,key):
    if lang=="en" or lang=="ru":
        cur.execute("INSERT INTO DadataUsers (Dadata_URL_servis,programming_language,token,key) VALUES ('https://dadata.ru',?,?,?)",(lang,token,key))
        con.commit()
        while True: 
            dadata = Dadata(token,key) 
            compas(dadata)     
            continue
    else:
        print("ошибка токого языка в выбаре небыло ")  
          
def compas(dadata):    
    print("введите нужное вам место положение")
    zapros = dadata.suggest(name="address", query=input(),language=lang)
    for i in range(len(zapros)):
        print(zapros[i]['value'])
    print("уточните ваш адрес введя введя один из предложанных адресов")
    adress = input()
    result=dadata.clean(name="address", source=adress)
    print(result['geo_lat'])
    print(result['geo_lon'])
    
print("введите ваш token для доступа к Dadata и выберете язык ")
print("ru для исползования Русского")
print("en to use Еnglish")
lang =  input()
token = input() 
key = input()
database(lang,token,key) 
    